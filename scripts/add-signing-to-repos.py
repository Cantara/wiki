#!/usr/bin/env python3
"""
add-signing-to-repos.py - Add signing workflow + KCP_SIGNING_KEY secret to all Cantara repos
that have a knowledge.yaml (real KCP manifest, not Maven config).

Actions per repo:
1. Set KCP_SIGNING_KEY repo secret
2. Push .github/workflows/sign-kcp.yml (caller for reusable workflow)
3. Update knowledge.yaml to add signature: URL field

Usage:
  python3 scripts/add-signing-to-repos.py              # dry-run
  python3 scripts/add-signing-to-repos.py --push        # actually push
  python3 scripts/add-signing-to-repos.py --push --repo MessiFilesystemProvider
"""

import argparse
import base64
import json
import os
import subprocess
import sys
from datetime import date

TODAY = date.today().isoformat()

# Repos that have their own signing workflow already
SKIP_REPOS = {
    'wiki', 'knowledge-context-protocol',
    'kcp-commands', 'kcp-memory', 'kcp-triage', 'kcp-dashboard',
    '.github',
}

CALLER_WORKFLOW = """\
name: Sign KCP Manifest

on:
  push:
    branches: [main, master]
    paths: [knowledge.yaml]

jobs:
  sign:
    uses: Cantara/.github/.github/workflows/sign-kcp.yml@main
    secrets: inherit
"""

COMMIT_WORKFLOW = "feat(kcp): add KCP manifest signing workflow\n\nCalls org-level reusable workflow to sign knowledge.yaml on every push.\nPublic key: https://wiki.cantara.no/.well-known/kcp-signing-key.pub\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"


def run(args, input=None):
    r = subprocess.run(args, capture_output=True, text=True, input=input)
    return r.returncode == 0, r.stdout.strip(), r.stderr.strip()


def file_sha(repo, path):
    ok, out, _ = run(['gh', 'api', f'/repos/Cantara/{repo}/contents/{path}', '--jq', '.sha'])
    return out if ok else None


def get_file_content(repo, path):
    ok, out, _ = run(['gh', 'api', f'/repos/Cantara/{repo}/contents/{path}', '--jq', '.content'])
    if not ok:
        return None
    try:
        return base64.b64decode(out).decode('utf-8', 'ignore')
    except Exception:
        return None


def push_file(repo, branch, path, content, message, dry_run):
    if dry_run:
        print(f"    [DRY] push {path}")
        return True
    sha = file_sha(repo, path)
    encoded = base64.b64encode(content.encode()).decode()
    payload = {'message': message, 'content': encoded, 'branch': branch}
    if sha:
        payload['sha'] = sha
    ok, _, err = run(
        ['gh', 'api', '--method', 'PUT', f'/repos/Cantara/{repo}/contents/{path}', '--input', '-'],
        input=json.dumps(payload)
    )
    if not ok:
        print(f"    ❌ {path}: {err[:120]}")
    return ok


def set_secret(repo, key_b64, dry_run):
    if dry_run:
        print(f"    [DRY] set secret KCP_SIGNING_KEY")
        return True
    ok, _, err = run(['gh', 'secret', 'set', 'KCP_SIGNING_KEY',
                      '--repo', f'Cantara/{repo}', '--body', key_b64])
    if not ok:
        print(f"    ❌ secret: {err[:120]}")
    return ok


def add_signature_field(yaml_content, repo, branch):
    """Insert signature: field into signing block if not present."""
    sig_url = f"https://raw.githubusercontent.com/Cantara/{repo}/{branch}/knowledge.yaml.sig"
    if 'signature:' in yaml_content:
        return yaml_content  # already has it
    # Insert after public_key: line
    lines = yaml_content.splitlines(keepends=True)
    out = []
    for line in lines:
        out.append(line)
        if line.strip().startswith('public_key:') and 'wiki.cantara.no' in line:
            indent = len(line) - len(line.lstrip())
            out.append(' ' * indent + f'signature: {sig_url}\n')
    return ''.join(out)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--push', action='store_true')
    parser.add_argument('--repo', help='Single repo to process')
    parser.add_argument('--limit', type=int, default=999)
    args = parser.parse_args()
    dry_run = not args.push

    if dry_run:
        print("DRY RUN — pass --push to execute\n")

    # Read the private key (base64) from env or file
    key_b64 = os.environ.get('KCP_SIGNING_KEY_B64')
    if not key_b64 and os.path.exists('/tmp/cantara-org-kcp.pem'):
        with open('/tmp/cantara-org-kcp.pem', 'rb') as f:
            key_b64 = base64.b64encode(f.read()).decode()
    if not key_b64 and not dry_run:
        print("ERROR: set KCP_SIGNING_KEY_B64 env var (base64-encoded Ed25519 private key)")
        sys.exit(1)

    # Get all active repos
    ok, out, _ = run(['gh', 'repo', 'list', 'Cantara', '--limit', '200', '--json',
                      'name,isArchived,defaultBranchRef'])
    repos = [r for r in json.loads(out) if not r['isArchived'] and r['name'] not in SKIP_REPOS]

    if args.repo:
        repos = [r for r in repos if r['name'] == args.repo]
    repos = repos[:args.limit]

    stats = {'workflow': 0, 'secret': 0, 'sig_field': 0, 'skipped': 0, 'errors': 0}

    for repo in repos:
        name = repo['name']
        branch = (repo.get('defaultBranchRef') or {}).get('name', 'main')

        # Only process repos with real KCP manifests
        content = get_file_content(name, 'knowledge.yaml')
        if not content:
            continue
        is_kcp = 'kcp_version' in content or 'entity:' in content or 'authority:' in content
        if not is_kcp:
            stats['skipped'] += 1
            continue

        print(f"🔐 {name} [branch={branch}]")

        # 1. Set repo secret
        ok = set_secret(name, key_b64 or 'DRY', dry_run)
        if ok:
            print(f"    ✅ KCP_SIGNING_KEY secret")
            stats['secret'] += 1
        else:
            stats['errors'] += 1

        # 2. Push caller workflow
        wf_sha = file_sha(name, '.github/workflows/sign-kcp.yml')
        if not wf_sha:
            ok = push_file(name, branch, '.github/workflows/sign-kcp.yml',
                           CALLER_WORKFLOW, COMMIT_WORKFLOW, dry_run)
            if ok:
                print(f"    ✅ sign-kcp.yml workflow")
                stats['workflow'] += 1
            else:
                stats['errors'] += 1
        else:
            print(f"    sign-kcp.yml already exists — skipping")

        # 3. Add signature: field to knowledge.yaml
        sig_url = f"https://raw.githubusercontent.com/Cantara/{name}/{branch}/knowledge.yaml.sig"
        if 'signature:' not in content:
            updated = add_signature_field(content, name, branch)
            ok = push_file(name, branch, 'knowledge.yaml', updated,
                           f"feat(kcp): add signature URL to knowledge.yaml\n\nPoints to {sig_url}\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
                           dry_run)
            if ok:
                print(f"    ✅ signature: field added")
                stats['sig_field'] += 1
            else:
                stats['errors'] += 1
        else:
            print(f"    signature: already present — skipping")

    print(f"\n{'DRY RUN ' if dry_run else ''}Summary:")
    print(f"  Secrets set:        {stats['secret']}")
    print(f"  Workflows pushed:   {stats['workflow']}")
    print(f"  Signature fields:   {stats['sig_field']}")
    print(f"  Skipped (non-KCP):  {stats['skipped']}")
    print(f"  Errors:             {stats['errors']}")


if __name__ == '__main__':
    main()
