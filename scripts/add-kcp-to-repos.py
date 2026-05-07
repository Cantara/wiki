#!/usr/bin/env python3
"""
add-kcp-to-repos.py — Push knowledge.yaml + llms.txt to Cantara repos that lack them.

Usage:
  python3 scripts/add-kcp-to-repos.py              # dry-run (print what would happen)
  python3 scripts/add-kcp-to-repos.py --push        # actually push
  python3 scripts/add-kcp-to-repos.py --push --repo MessiSDK  # single repo

For repos with knowledge.yaml naming conflict (app config), pass --conflict-mode llms-only
to push llms.txt only (referencing wiki-hosted manifest).
"""

import argparse
import base64
import json
import subprocess
import sys
from datetime import date

TODAY = date.today().isoformat()

# Already have real KCP manifests — skip entirely
SKIP_REPOS = {
    'wiki', 'knowledge-context-protocol',
    'kcp-commands', 'kcp-memory', 'kcp-triage', 'kcp-dashboard',
    'xorcery', 'stingray',
    'Whydah', 'Whydah-UserStateService', 'Whydah-TypeLib',
    'Whydah-SecurityTokenService', 'Whydah-Java-SDK',
    'Whydah-UserIdentityBackend', 'maven-infrastructure', 'julebrus',
}

COMMIT_MSG_KCP  = "feat(kcp): add KCP v0.14 manifest for agent discoverability\n\nPart of the Cantara-wide agentic web initiative. Agents can now navigate\nthis repo via knowledge.yaml. Signing key delegated to wiki.cantara.no.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
COMMIT_MSG_LLMS = "feat(kcp): add llms.txt for agent discoverability\n\nPoints agents to the wiki.cantara.no-hosted KCP manifest for this repo.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"


def gh_json(args):
    r = subprocess.run(['gh'] + args, capture_output=True, text=True)
    if r.returncode != 0:
        return None
    return json.loads(r.stdout)


def file_sha(repo, path, branch):
    r = subprocess.run(
        ['gh', 'api', f'/repos/Cantara/{repo}/contents/{path}',
         '--jq', '.sha'],
        capture_output=True, text=True
    )
    return r.stdout.strip() if r.returncode == 0 else None


def push_file(repo, branch, path, content, message, dry_run=True):
    if dry_run:
        print(f"    [DRY] would push {path}")
        return True
    sha = file_sha(repo, path, branch)
    encoded = base64.b64encode(content.encode()).decode()
    payload = {'message': message, 'content': encoded, 'branch': branch}
    if sha:
        payload['sha'] = sha
    r = subprocess.run(
        ['gh', 'api', '--method', 'PUT',
         f'/repos/Cantara/{repo}/contents/{path}', '--input', '-'],
        input=json.dumps(payload), capture_output=True, text=True
    )
    ok = r.returncode == 0
    if not ok:
        print(f"    ❌ {path}: {r.stderr.strip()[:120]}")
    return ok


def generate_knowledge_yaml(repo, description, language, stars):
    desc = (description or f'{repo} — Cantara open source library').strip()
    lang = language or 'Java'
    # Indent long descriptions
    if len(desc) > 80:
        desc = '\n    '.join([desc[i:i+76] for i in range(0, len(desc), 76)])
    stars_comment = f"  stars: {stars}" if stars else ""
    return f"""version: "0.14"

entity:
  name: {repo}
  type: open-source-library
  description: >
    {desc}

authority:
  owner: Cantara — Norwegian Software Development Foundation
  repo: https://github.com/Cantara/{repo}
  license: Apache-2.0
  org_manifest: https://wiki.cantara.no/knowledge.yaml

discovery:
  provenance: canonical
  confidence: medium
  staleness_days: 30

signing:
  scheme: ed25519
  scope: this-manifest
  public_key: https://wiki.cantara.no/.well-known/kcp-signing-key.pub

kcp_version: "0.14"
project: {repo}
language: en
license: "Apache-2.0"
runtime: {lang}
indexing: open
updated: "{TODAY}"
{stars_comment}

units:

  - id: readme
    path: README.md
    intent: "What is {repo}, what does it do, and how do I install and use it?"
    scope: global
    audience: [human, agent, developer]
    validated: "{TODAY}"
    triggers: [overview, install, usage, {repo.lower()}, getting started]
"""


def generate_llms_txt(repo, description, language, conflict=False):
    desc = (description or f'{repo} — Cantara open source library').strip()
    lang = language or 'Java'
    if conflict:
        manifest_note = f"""## Structured Navigation (for AI agents)

KCP v0.14 manifest for this repository (wiki-hosted):
https://wiki.cantara.no/knowledge/repos/{repo}.yaml

Signing key (delegated to Cantara org): https://wiki.cantara.no/.well-known/kcp-signing-key.pub"""
    else:
        manifest_note = f"""## Structured Navigation (for AI agents)

This repository ships a KCP v0.14 manifest:
https://raw.githubusercontent.com/Cantara/{repo}/main/knowledge.yaml

Signing key (delegated to Cantara org): https://wiki.cantara.no/.well-known/kcp-signing-key.pub"""

    return f"""# {repo}

> {desc}

Part of the [Cantara](https://wiki.cantara.no) open source ecosystem.
Apache-2.0. {lang}.

{manifest_note}

## Related

- [Cantara wiki](https://wiki.cantara.no) — Full project documentation
- [knowledge-context-protocol](https://github.com/Cantara/knowledge-context-protocol) — KCP spec
- [kcp-commands](https://github.com/Cantara/kcp-commands) — Claude Code hook
"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--push', action='store_true', help='Actually push (default: dry-run)')
    parser.add_argument('--repo', help='Process only this repo')
    parser.add_argument('--conflict-mode', choices=['skip', 'llms-only'], default='llms-only',
                        help='What to do for repos with naming conflicts (default: llms-only)')
    parser.add_argument('--limit', type=int, default=999, help='Max repos to process')
    args = parser.parse_args()

    dry_run = not args.push
    if dry_run:
        print("DRY RUN — pass --push to actually push files\n")

    # Fetch all active repos
    print("Fetching repo list from GitHub...")
    repos = gh_json(['repo', 'list', 'Cantara', '--limit', '200', '--json',
                     'name,description,primaryLanguage,stargazerCount,isArchived,defaultBranchRef'])
    if not repos:
        print("Failed to fetch repos"); sys.exit(1)

    active = [r for r in repos if not r['isArchived'] and r['name'] not in SKIP_REPOS]
    if args.repo:
        active = [r for r in active if r['name'] == args.repo]
    active = active[:args.limit]
    print(f"Processing {len(active)} repos...\n")

    stats = {'kcp_pushed': 0, 'llms_pushed': 0, 'skipped': 0, 'errors': 0}

    for repo in active:
        name = repo['name']
        desc = repo.get('description') or ''
        lang_obj = repo.get('primaryLanguage') or {}
        lang = lang_obj.get('name', 'Java') if lang_obj else 'Java'
        stars = repo.get('stargazerCount', 0)
        branch_ref = repo.get('defaultBranchRef') or {}
        branch = branch_ref.get('name', 'main')

        # Check existing knowledge.yaml
        existing_sha = file_sha(name, 'knowledge.yaml', branch)
        existing_llms = file_sha(name, 'llms.txt', branch)

        if existing_sha:
            # Check if it's a real KCP manifest or app config
            r = subprocess.run(
                ['gh', 'api', f'/repos/Cantara/{name}/contents/knowledge.yaml', '--jq', '.content'],
                capture_output=True, text=True
            )
            try:
                content = base64.b64decode(r.stdout.strip()).decode('utf-8', 'ignore')
                is_kcp = 'kcp_version' in content or 'entity:' in content or 'authority:' in content
            except Exception:
                is_kcp = False

            if is_kcp:
                print(f"⏭  {name}: real KCP manifest exists — skipping")
                stats['skipped'] += 1
                continue
            else:
                # Naming conflict
                if args.conflict_mode == 'skip':
                    print(f"⚠️  {name}: naming conflict — skipping")
                    stats['skipped'] += 1
                    continue
                else:
                    print(f"⚠️  {name} [conflict — llms.txt only, branch={branch}]")
                    if not existing_llms:
                        llms = generate_llms_txt(name, desc, lang, conflict=True)
                        ok = push_file(name, branch, 'llms.txt', llms, COMMIT_MSG_LLMS, dry_run)
                        if ok:
                            print(f"    ✅ llms.txt")
                            stats['llms_pushed'] += 1
                        else:
                            stats['errors'] += 1
                    else:
                        print(f"    llms.txt already exists — skipping")
                    continue

        print(f"➕ {name} [branch={branch}, lang={lang}, ⭐{stars}]")

        # Push knowledge.yaml
        ky = generate_knowledge_yaml(name, desc, lang, stars)
        ok = push_file(name, branch, 'knowledge.yaml', ky, COMMIT_MSG_KCP, dry_run)
        if ok:
            print(f"    ✅ knowledge.yaml")
            stats['kcp_pushed'] += 1
        else:
            stats['errors'] += 1

        # Push llms.txt (only if doesn't exist)
        if not existing_llms:
            llms = generate_llms_txt(name, desc, lang, conflict=False)
            ok = push_file(name, branch, 'llms.txt', llms, COMMIT_MSG_LLMS, dry_run)
            if ok:
                print(f"    ✅ llms.txt")
                stats['llms_pushed'] += 1
            else:
                stats['errors'] += 1
        else:
            print(f"    llms.txt already exists — skipping")

    print(f"\n{'DRY RUN ' if dry_run else ''}Summary:")
    print(f"  knowledge.yaml pushed: {stats['kcp_pushed']}")
    print(f"  llms.txt pushed:       {stats['llms_pushed']}")
    print(f"  skipped:               {stats['skipped']}")
    print(f"  errors:                {stats['errors']}")


if __name__ == '__main__':
    main()
