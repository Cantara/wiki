#!/usr/bin/env python3
"""
Generate GitHub Repo Index for Cantara Wiki.

Fetches all non-archived repos from the Cantara GitHub org and generates:
  - docs/repos/<repo-name>.md  (one page per repo)
  - docs/repos/index.md        (overview grouped by project family)
  - Updates mkdocs.yml nav section between sentinel comments

Usage:
    python scripts/generate_repo_index.py

Environment:
    GITHUB_TOKEN  — optional, raises rate limit from 60 to 5000 req/hr
"""

import base64
import fnmatch
import json
import os
import re
import sys
import textwrap
from pathlib import Path

try:
    import requests
except ImportError:
    sys.exit("Missing dependency: pip install requests")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

ORG = "Cantara"
API_BASE = "https://api.github.com"
DOCS_REPOS_DIR = Path("docs/repos")
MKDOCS_YML = Path("mkdocs.yml")
README_MAX_LINES = 500

# Repos (or glob patterns) that map to a wiki section slug
WIKI_MAPPING = {
    "Whydah": "whydah",
    "Whydah-*": "whydah",
    "Java-Auto-Update": "JAU",
    "ConfigService*": "JAU",
    "blitz*": "blitz",
    "Blitz*": "blitz",
    "Awesome-Competence-System*": "ACS",
    "IoT*": "iot",
    "iot*": "iot",
}

# Project family definitions — order matters (first match wins)
FAMILIES = [
    ("Whydah IAM/SSO",        lambda r: _matches_any(r["name"], ["Whydah*", "whydah*"])),
    ("ConfigService",         lambda r: _matches_any(r["name"], ["ConfigService*"])),
    ("Messi Messaging",       lambda r: _matches_any(r["name"], ["Messi*", "messi*"])),
    ("Java Auto-Update",      lambda r: _matches_any(r["name"], ["Java-Auto-Update", "JAU*"])),
    ("Xorcery",               lambda r: _matches_any(r["name"], ["xorcery*", "Xorcery*"])),
    ("Visuale",               lambda r: _matches_any(r["name"], ["visuale*", "Visuale*"])),
    ("Valuereporter",         lambda r: _matches_any(r["name"], ["Valuereporter*", "valuereporter*"])),
    ("RealEstate",            lambda r: _matches_any(r["name"], ["realestate*", "RealEstate*"])),
    ("Blitz",                 lambda r: _matches_any(r["name"], ["blitz*", "Blitz*"])),
    ("Go Tools",              lambda r: r.get("language") == "Go"),
    ("Terraform / Infra",     lambda r: r.get("language") == "HCL"
                                        or r["name"] in ("maven-infrastructure", "devops")),
    ("Other",                 lambda r: True),
]

# Sentinel markers used in mkdocs.yml
BEGIN_MARKER = "  # BEGIN_REPOS_NAV"
END_MARKER = "  # END_REPOS_NAV"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _matches_any(name: str, patterns: list[str]) -> bool:
    return any(fnmatch.fnmatch(name, p) for p in patterns)


def _wiki_section(name: str) -> str | None:
    for pattern, slug in WIKI_MAPPING.items():
        if fnmatch.fnmatch(name, pattern):
            return slug
    return None


def _should_fetch_readme(repo: dict) -> bool:
    if repo.get("fork") or repo.get("archived"):
        return False
    if repo.get("stargazers_count", 0) >= 1:
        return True
    if _wiki_section(repo["name"]):
        return True
    return False


def _session() -> requests.Session:
    s = requests.Session()
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        s.headers["Authorization"] = f"Bearer {token}"
    s.headers["Accept"] = "application/vnd.github+json"
    s.headers["X-GitHub-Api-Version"] = "2022-11-28"
    return s


# ---------------------------------------------------------------------------
# GitHub API calls
# ---------------------------------------------------------------------------

def fetch_repos(session: requests.Session) -> list[dict]:
    """Fetch all non-archived repos from the org."""
    repos = []
    url = f"{API_BASE}/orgs/{ORG}/repos"
    params = {"per_page": 100, "type": "public"}
    while url:
        resp = session.get(url, params=params)
        resp.raise_for_status()
        batch = resp.json()
        repos.extend(r for r in batch if not r.get("archived"))
        # Follow Link header for pagination
        link = resp.headers.get("Link", "")
        next_url = None
        for part in link.split(","):
            part = part.strip()
            if 'rel="next"' in part:
                next_url = part.split(";")[0].strip().lstrip("<").rstrip(">")
        url = next_url
        params = {}  # params already encoded in next_url
    return repos


def fetch_readme(session: requests.Session, repo_name: str) -> str | None:
    """Fetch and decode the README for a repo. Returns plain text or None."""
    url = f"{API_BASE}/repos/{ORG}/{repo_name}/readme"
    resp = session.get(url)
    if resp.status_code == 404:
        return None
    resp.raise_for_status()
    data = resp.json()
    content = base64.b64decode(data["content"]).decode("utf-8", errors="replace")
    lines = content.splitlines()
    if len(lines) > README_MAX_LINES:
        lines = lines[:README_MAX_LINES]
        lines.append(f"\n*(README truncated at {README_MAX_LINES} lines)*")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Markdown generation
# ---------------------------------------------------------------------------

def _topic_badges(topics: list[str]) -> str:
    if not topics:
        return ""
    return " ".join(f"`{t}`" for t in topics)


def render_repo_page(repo: dict, readme: str | None) -> str:
    name = repo["name"]
    desc = repo.get("description") or ""
    lang = repo.get("language") or "—"
    stars = repo.get("stargazers_count", 0)
    updated = (repo.get("updated_at") or "")[:10]
    homepage = repo.get("homepage") or ""
    topics = repo.get("topics") or []
    html_url = repo["html_url"]
    wiki_slug = _wiki_section(name)

    lines = [
        f"# {name}",
        "",
        desc if desc else "*No description provided.*",
        "",
        "| Field | Value |",
        "| --- | --- |",
        f"| **GitHub** | [{html_url}]({html_url}) |",
        f"| **Language** | {lang} |",
        f"| **Stars** | {stars} |",
        f"| **Last updated** | {updated} |",
    ]
    if homepage:
        lines.append(f"| **Homepage** | [{homepage}]({homepage}) |")
    if topics:
        lines.append(f"| **Topics** | {_topic_badges(topics)} |")
    lines.append("")

    if wiki_slug:
        lines += [
            '!!! tip "Related Wiki Pages"',
            f'    This project has documentation in the Cantara Wiki.',
            f'    See the [{wiki_slug.upper()} section](../{wiki_slug}/index.md).',
            "",
        ]

    if readme:
        lines += [
            "---",
            "",
            "## README",
            "",
            readme,
            "",
        ]

    return "\n".join(lines)


def render_index_page(repos: list[dict]) -> str:
    lines = [
        "# GitHub Repository Index",
        "",
        "All active (non-archived) public repositories in the "
        "[Cantara GitHub organisation](https://github.com/Cantara), "
        f"grouped by project family. {len(repos)} repositories total.",
        "",
        "---",
        "",
    ]

    # Group repos by family
    assigned: set[str] = set()
    groups: list[tuple[str, list[dict]]] = []
    for family_name, predicate in FAMILIES:
        members = [r for r in repos if r["name"] not in assigned and predicate(r)]
        if members:
            groups.append((family_name, members))
            assigned.update(r["name"] for r in members)

    for family_name, members in groups:
        anchor = family_name.lower().replace(" ", "-").replace("/", "").replace("--", "-")
        lines += [f"## {family_name}", ""]
        for r in sorted(members, key=lambda x: x["name"].lower()):
            desc = r.get("description") or ""
            stars = r.get("stargazers_count", 0)
            star_str = f" ★{stars}" if stars else ""
            desc_str = f" — {desc}" if desc else ""
            lines.append(f"- [{r['name']}]({r['name']}.md){star_str}{desc_str}")
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# mkdocs.yml update
# ---------------------------------------------------------------------------

def _repos_nav_block(repos: list[dict]) -> list[str]:
    """Return the lines of the repos nav block (with sentinels)."""
    lines = [
        BEGIN_MARKER,
        '  - "GitHub Repos":',
        '      - "All Repositories": repos/index.md',
    ]
    for r in sorted(repos, key=lambda x: x["name"].lower()):
        name = r["name"]
        title = name.replace("-", " ")
        lines.append(f'      - "{title}": repos/{name}.md')
    lines.append(END_MARKER)
    return lines


def update_mkdocs_nav(repos: list[dict]) -> None:
    text = MKDOCS_YML.read_text()
    nav_block = "\n".join(_repos_nav_block(repos))

    if BEGIN_MARKER in text and END_MARKER in text:
        # Replace existing block
        pattern = re.compile(
            re.escape(BEGIN_MARKER) + r".*?" + re.escape(END_MARKER),
            re.DOTALL,
        )
        new_text = pattern.sub(nav_block, text)
    else:
        # Insert after the "Home" nav entry
        home_line = '  - "Home": index.md'
        if home_line not in text:
            print(
                f"WARNING: could not find '{home_line}' in mkdocs.yml — "
                "skipping nav update"
            )
            return
        new_text = text.replace(
            home_line,
            home_line + "\n" + nav_block,
            1,
        )

    MKDOCS_YML.write_text(new_text)
    print(f"  Updated {MKDOCS_YML}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    session = _session()

    print("Fetching repos from GitHub …")
    repos = fetch_repos(session)
    print(f"  Found {len(repos)} non-archived public repos")

    DOCS_REPOS_DIR.mkdir(parents=True, exist_ok=True)

    # Generate individual repo pages
    for i, repo in enumerate(repos, 1):
        name = repo["name"]
        print(f"  [{i}/{len(repos)}] {name}", end="")
        readme = None
        if _should_fetch_readme(repo):
            print(" (fetching README)", end="")
            try:
                readme = fetch_readme(session, name)
            except Exception as exc:
                print(f" [README fetch failed: {exc}]", end="")
        print()
        page = render_repo_page(repo, readme)
        (DOCS_REPOS_DIR / f"{name}.md").write_text(page)

    # Generate index page
    index_page = render_index_page(repos)
    (DOCS_REPOS_DIR / "index.md").write_text(index_page)
    print(f"  Wrote {DOCS_REPOS_DIR}/index.md")

    # Update mkdocs.yml
    print("Updating mkdocs.yml nav …")
    update_mkdocs_nav(repos)

    print("Done.")


if __name__ == "__main__":
    main()
