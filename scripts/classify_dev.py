#!/usr/bin/env python3
"""Classify dev/ pages into sub-categories and update mkdocs.yml nav."""

import re
import os

MKDOCS_YML = "mkdocs.yml"

# Category definitions: (category_name, keywords)
# Keywords are matched case-insensitively against the filename (without path and extension)
CATEGORIES = [
    ("Agile Methods & Practices", [
        "agile", "scrum", "kanban", "xp", "sprint", "retrospective",
        "story", "backlog", "velocity", "planning", "stand-up", "lean",
        "standup", "pomodoro", "evo", "crystal", "waterfall",
    ]),
    ("Testing", [
        "test", "jigzaw", "tdd", "bdd", "mock", "spec", "junit",
        "testng", "selenium", "unitils", "jmeter",
    ]),
    ("CI/CD & Build", [
        "ci", "cd", "build", "jenkins", "hudson", "pipeline", "deploy",
        "release", "maven", "gradle", "ant", "nexus", "rpm",
        "continuous", "cargo", "jsw",
    ]),
    ("Web Development", [
        "html", "css", "javascript", "frontend", "ajax", "rest", "http",
        "api", "web", "cors", "csrf", "websocket", "angular", "w3c",
        "jetty", "tomcat", "webapp", "grails", "groovy", "jruby",
    ]),
    ("Security & Identity", [
        "security", "ldap", "iam", "oauth", "sso", "identity", "auth",
        "password", "ssl", "hdiv", "owasp", "attack",
    ]),
    ("Database & Storage", [
        "database", "sql", "jdbc", "hibernate", "jpa", "nosql", "mongodb",
        "couchdb", "persistence", "rdbms", "oracle",
    ]),
    ("Architecture & Design", [
        "architecture", "ddd", "pattern", "design", "microservice", "soa",
        "domain", "orthogonality", "single-responsibility",
    ]),
]


def classify_filename(filename):
    """Classify a filename into a category based on keyword matching.

    filename: just the filename part (no path), with extension stripped.
    Returns the category name, or "Other".
    """
    # Convert to lowercase for matching
    name_lower = filename.lower().replace("-", " ").replace("_", " ")

    for cat_name, keywords in CATEGORIES:
        for kw in keywords:
            # Match whole word boundaries
            if re.search(r'\b' + re.escape(kw.lower()) + r'\b', name_lower):
                return cat_name

    return "Other"


def main():
    with open(MKDOCS_YML, "r", encoding="utf-8") as f:
        content = f.read()
    lines = content.split("\n")

    # Find the "Agile Development" subsection within "Knowledge Base"
    # The structure is:
    #     - "Agile Development":
    #         - dev/... entries
    # We need to find this block and replace it

    # Find start of the Agile Development subsection
    dev_start = None
    dev_end = None
    dev_indent = None

    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == '- "Agile Development":':
            # Check that dev/ entries follow
            # Look at the next non-empty line
            for j in range(i + 1, min(i + 5, len(lines))):
                if lines[j].strip() and "dev/" in lines[j]:
                    dev_start = i
                    dev_indent = len(line) - len(line.lstrip())
                    break
            if dev_start is not None:
                break

    if dev_start is None:
        print("ERROR: Could not find 'Agile Development' section with dev/ entries!")
        return

    # Find the end of the dev section
    # It ends when we hit a line at the same or lesser indent level (that's not blank)
    for i in range(dev_start + 1, len(lines)):
        line = lines[i]
        if not line.strip():
            continue
        current_indent = len(line) - len(line.lstrip())
        if current_indent <= dev_indent:
            dev_end = i
            break

    if dev_end is None:
        dev_end = len(lines)

    print(f"Found dev section at lines {dev_start+1}-{dev_end} (indent={dev_indent})")

    # Extract all dev/ entries from this section
    dev_entries = []  # list of (display_name, path, original_line)
    dev_index_line = None

    for i in range(dev_start + 1, dev_end):
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            continue

        # Parse the entry: - "Display Name": dev/path.md
        # Or: - dev/index.md
        m = re.match(r'^- "([^"]+)":\s+(.+)$', stripped)
        if m:
            display_name = m.group(1)
            path = m.group(2)
            if "dev/" in path:
                dev_entries.append((display_name, path, stripped))
            continue

        m = re.match(r'^- (.+)$', stripped)
        if m:
            path = m.group(1).strip()
            if "dev/" in path:
                if path == "dev/index.md":
                    dev_index_line = stripped
                else:
                    dev_entries.append((path, path, stripped))

    print(f"Found {len(dev_entries)} dev/ entries (plus index)")

    # Classify each entry
    categorized = {}
    for cat_name, _ in CATEGORIES:
        categorized[cat_name] = []
    categorized["Other"] = []

    for display_name, path, orig_line in dev_entries:
        # Extract filename from path for classification
        filename = path.split("/")[-1]
        if filename.endswith(".md"):
            filename = filename[:-3]

        category = classify_filename(filename)
        categorized[category].append(orig_line)

    # Print classification stats
    print("\nClassification results:")
    for cat_name in [c[0] for c in CATEGORIES] + ["Other"]:
        count = len(categorized[cat_name])
        if count > 0:
            print(f"  {cat_name}: {count} pages")

    # Build the new dev section
    # Base indent is dev_indent (4 spaces typically)
    ind = " " * dev_indent
    new_lines = []
    new_lines.append(f'{ind}- "Agile Development":')
    new_lines.append(f'{ind}    - dev/index.md')

    category_order = [c[0] for c in CATEGORIES] + ["Other"]

    for cat_name in category_order:
        entries = categorized[cat_name]
        if not entries:
            continue
        new_lines.append(f'{ind}    - "{cat_name}":')
        for entry in sorted(entries):
            new_lines.append(f'{ind}        - {entry[2:]}')  # strip leading "- "

    # Replace the dev section in the file
    result_lines = lines[:dev_start] + new_lines + lines[dev_end:]
    result = "\n".join(result_lines)

    with open(MKDOCS_YML, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"\nWrote updated {MKDOCS_YML}")


if __name__ == "__main__":
    main()
