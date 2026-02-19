#!/usr/bin/env python3
"""Restructure mkdocs.yml nav from flat Confluence spaces to grouped hierarchy."""

import re
import sys

MKDOCS_YML = "mkdocs.yml"


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    # Read the ORIGINAL mkdocs.yml from git to avoid reading our own output
    import subprocess
    content = subprocess.check_output(["git", "show", "HEAD:mkdocs.yml"],
                                       text=True)
    lines = content.splitlines(keepends=False)

    # Find the nav section
    nav_start = None
    nav_end = None
    for i, line in enumerate(lines):
        if line.rstrip() == "nav:":
            nav_start = i
            break

    # Everything after nav: until EOF is the nav section (no other top-level keys after)
    before_nav = lines[:nav_start]
    nav_lines = lines[nav_start:]

    # Parse top-level sections from nav
    # Top-level entries start with exactly "  - " (2 spaces + dash + space)
    # Also capture comments at the same level (for sentinels)
    sections = []  # list of (key, [lines])
    current_key = None
    current_lines = []

    for line in nav_lines[1:]:  # skip "nav:" line itself
        stripped = line.strip()

        # Check if this is a top-level entry or comment
        is_top_level_entry = re.match(r'^  - ', line) and not re.match(r'^    ', line)
        is_top_level_comment = re.match(r'^  # ', line)

        if is_top_level_entry:
            if current_key is not None:
                sections.append((current_key, current_lines))

            # Get key from the line
            m = re.match(r'^  - "([^"]+)":', line)
            if not m:
                m = re.match(r'^  - ([^:]+):', line)
            if m:
                current_key = m.group(1).strip()
            else:
                # Simple entry like - "Home": index.md
                m = re.match(r'^  - "([^"]+)":\s+', line)
                if m:
                    current_key = m.group(1)
                else:
                    current_key = stripped
            current_lines = [line]
        elif is_top_level_comment:
            # Comments at top level (like sentinel markers)
            if current_key is not None:
                current_lines.append(line)
            else:
                # Comment before first section - start a pseudo-section
                if current_key is None:
                    current_key = "__comment__"
                    current_lines = [line]
        else:
            # Content line - belongs to current section
            if current_key is not None:
                current_lines.append(line)

    if current_key is not None:
        sections.append((current_key, current_lines))

    # Build sections dictionary
    sections_dict = {}
    for key, slines in sections:
        sections_dict[key] = slines

    print(f"Found {len(sections)} top-level sections:")
    for key, slines in sections:
        print(f"  '{key}': {len(slines)} lines")

    # Extract repos entries from the GitHub Repos section
    # In the original, the structure is:
    #   # BEGIN_REPOS_NAV
    #   - "GitHub Repos":
    #       - "All Repositories": repos/index.md
    #       - ... more repos ...
    #   # END_REPOS_NAV
    # The sentinels are captured as part of the GitHub Repos section
    repos_inner_entries = []
    if "GitHub Repos" in sections_dict:
        gh_lines = sections_dict["GitHub Repos"]
        for line in gh_lines:
            stripped = line.strip()
            if "BEGIN_REPOS_NAV" in stripped or "END_REPOS_NAV" in stripped:
                continue
            if stripped.startswith('- "GitHub Repos"'):
                continue
            if stripped:
                repos_inner_entries.append(stripped)
        print(f"\nExtracted {len(repos_inner_entries)} repo entries")

    # Helper: get sub-entries for a section (skip the header line, skip sentinel comments)
    def get_entries(key):
        if key not in sections_dict:
            print(f"  WARNING: section '{key}' not found!")
            return []
        slines = sections_dict[key]
        entries = []
        for line in slines[1:]:  # skip header
            stripped = line.strip()
            if not stripped or "BEGIN_REPOS_NAV" in stripped or "END_REPOS_NAV" in stripped:
                continue
            # Calculate relative indentation
            orig_spaces = len(line) - len(line.lstrip())
            entries.append((stripped, orig_spaces))
        return entries

    # Helper: write entries at a given base indentation
    def write_entries(out, entries, base_indent, section_base=6):
        for stripped, orig_spaces in entries:
            relative = orig_spaces - section_base
            if relative < 0:
                relative = 0
            new_indent = base_indent + relative
            out.append(" " * new_indent + stripped)

    # Helper: write a subsection with one or more space keys
    def write_subsection(out, display_name, space_keys, entry_indent=8):
        out.append(f'    - "{display_name}":')
        for skey in space_keys:
            entries = get_entries(skey)
            write_entries(out, entries, entry_indent)

    # Build new nav
    new_nav = []
    new_nav.append("nav:")
    new_nav.append("  - Home: index.md")
    new_nav.append("")

    # === PROJECTS ===
    new_nav.append("  - Projects:")
    new_nav.append("    - projects/index.md")

    project_spaces = [
        ("Whydah (IAM/SSO)", ["Whydah (IAM/SSO)"]),
        ("Java Auto-Update & ConfigService", ["JAU"]),
        ("Blitz", ["Blitz"]),
        ("ACS (Competence System)", ["ACS"]),
        ("HTTPLoadTest Baseline", ["HLT"]),
        ("Enterprise Domain Repository", ["EDR", "EDRMDS"]),
        ("Evolving Service Adapter", ["ESE"]),
        ("Backward Compatibility Tester", ["BCT"]),
        ("MActor", ["mactor"]),
        ("LDAP Client", ["LDC"]),
        ("Drone Radar", ["drone"]),
        ("IoT", ["IoT"]),
    ]

    for display_name, space_keys in project_spaces:
        write_subsection(new_nav, display_name, space_keys)

    new_nav.append("")

    # === KNOWLEDGE BASE ===
    new_nav.append('  - "Knowledge Base":')
    new_nav.append("    - knowledge/index.md")

    kb_spaces = [
        ("Software Architecture", ["Software Architecture"]),
        ("Enterprise Architecture", ["Enterprise Architecture"]),
        ("Open Web Services & SOA", ["Open Web Services & SOA"]),
        ("Agile Development", ["Agile Development"]),
        ("Agile Release Strategies", ["ARS"]),
        ("Knowledge Management", ["Knowledge Management"]),
        ("Security", ["security"]),
        ("Behaviour Focused Architecture", ["BFA"]),
        ("Application Analysis", ["aa"]),
        ("ThinkTank", ["TANK"]),
        ("Open Data", ["Open Data"]),
        ("Puben", ["puben"]),
    ]

    for display_name, space_keys in kb_spaces:
        write_subsection(new_nav, display_name, space_keys)

    new_nav.append("")

    # === COMMUNITY & EVENTS ===
    new_nav.append('  - "Community & Events":')
    new_nav.append("    - community/index.md")

    community_spaces = [
        ("About Cantara", ["About"]),
        ("Platform Engineering", ["Platform Engineering", "pe"]),
        ("IASA Oslo", ["IASA"]),
        ("Communities In Action", ["CIA"]),
        ("Smidig Conference", ["Smidig", "smidigtonull"]),
        ("Community Leader Summit", ["CLSC"]),
        ("Mobile Code Camp 2011", ["MCC11"]),
        ("DevHouse", ["DevHouse"]),
        ("HTML5 Code Camp", ["FRONT"]),
        ("Oslo XP Meetup", ["XPM"]),
        ("Open Source Projects", ["OSS"]),
        ("Organizations", ["ORG"]),
        ("MTSG", ["MTSG"]),
    ]

    for display_name, space_keys in community_spaces:
        write_subsection(new_nav, display_name, space_keys)

    new_nav.append("")

    # === OPERATIONS ===
    new_nav.append("  - Operations:")
    new_nav.append("    - operations/index.md")

    ops_spaces = [
        ("System Administration", ["sysadm"]),
    ]

    for display_name, space_keys in ops_spaces:
        write_subsection(new_nav, display_name, space_keys)

    new_nav.append("")

    # === GITHUB REPOS ===
    new_nav.append('  - "GitHub Repos":')
    new_nav.append("    - repos/index.md")
    new_nav.append("    # BEGIN_REPOS_NAV")

    for entry in repos_inner_entries:
        new_nav.append("    " + entry)

    new_nav.append("    # END_REPOS_NAV")
    new_nav.append("")

    # === ARCHIVE ===
    new_nav.append("  - Archive:")
    new_nav.append("    - archive/index.md")
    new_nav.append('    - "Personal Spaces":')

    personal_space_keys = [
        "~andersand", "~andersb", "~anton@antonbabenko.com", "~awiik",
        "User: baard.lind", "User: dagb", "~gatepoet", "~halrik",
        "~hansogj", "~helge", "~hkokko", "~ho.leon@gmail.com",
        "~jek@webstep.no", "~jhannes", "~lacostej", "~lazee",
        "~leif@auke.no", "~leifh@conduct.no", "~maurtvedt",
        "~niklas@leanway.no", "~ovejord@hotmail.com", "~oyvindaa",
        "~paal.levang@synaptic.no", "~per.spilling", "~perchrh",
        "~sharebear", "~sherriff", "~steinim",
        "~terje.orvedal@webstep.no", "~tobiast",
        "~tor.martin.saur@gmail.com", "User: totto",
    ]

    for skey in personal_space_keys:
        if skey not in sections_dict:
            print(f"  WARNING: personal space '{skey}' not found!")
            continue
        slines = sections_dict[skey]
        # Write the header (re-indented)
        header = slines[0].strip()
        # Re-indent the header to 8 spaces
        new_nav.append("        " + header)
        # Write sub-entries at 12 spaces base
        entries = get_entries(skey)
        write_entries(new_nav, entries, 12)

    new_nav.append('    - Miscellaneous:')

    misc_spaces = [("noops", ["noops"]), ("PVC", ["PVC"])]
    for display_name, space_keys in misc_spaces:
        for skey in space_keys:
            entries = get_entries(skey)
            write_entries(new_nav, entries, 8)

    new_nav.append("")

    # Write the new file
    # The before_nav part includes everything before "nav:"
    # We need to also update the theme and plugins sections
    output_lines = []

    # Write the updated header (theme, plugins, extensions)
    output_lines.append("site_name: Cantara Wiki")
    output_lines.append("site_description: Archive of the Cantara open source wiki (wiki.cantara.no)")
    output_lines.append("site_url: https://cantara.github.io/wiki/")
    output_lines.append("repo_url: https://github.com/Cantara/wiki")
    output_lines.append("repo_name: Cantara/wiki")
    output_lines.append("")
    output_lines.append("theme:")
    output_lines.append("  name: material")
    output_lines.append("  palette:")
    output_lines.append("    primary: deep purple")
    output_lines.append("    accent: purple")
    output_lines.append("  features:")
    output_lines.append("    - navigation.sections")
    output_lines.append("    - navigation.indexes")
    output_lines.append("    - navigation.top")
    output_lines.append("    - navigation.tabs")
    output_lines.append("    - navigation.tabs.sticky")
    output_lines.append("    - search.highlight")
    output_lines.append("    - search.suggest")
    output_lines.append("    - content.code.copy")
    output_lines.append("")
    output_lines.append("plugins:")
    output_lines.append("  - search")
    output_lines.append("  - tags")
    output_lines.append("")
    output_lines.append("markdown_extensions:")
    output_lines.append("  - admonition")
    output_lines.append("  - attr_list")
    output_lines.append("  - md_in_html")
    output_lines.append("  - pymdownx.superfences")
    output_lines.append("")

    # Add the nav
    output_lines.extend(new_nav)

    write_file(MKDOCS_YML, "\n".join(output_lines) + "\n")
    print(f"\nWrote restructured {MKDOCS_YML}")

    # Verify: count .md references in original vs new
    orig_md = set()
    for line in nav_lines:
        for m in re.finditer(r'[^\s"]+\.md', line):
            orig_md.add(m.group())

    new_md = set()
    for line in new_nav:
        for m in re.finditer(r'[^\s"]+\.md', line):
            new_md.add(m.group())

    new_pages = {"projects/index.md", "knowledge/index.md", "community/index.md",
                 "operations/index.md", "archive/index.md"}
    new_md -= new_pages

    missing = orig_md - new_md
    extra = new_md - orig_md

    if missing:
        print(f"\nWARNING: {len(missing)} pages from original nav are MISSING:")
        for p in sorted(missing)[:20]:
            print(f"  {p}")
        if len(missing) > 20:
            print(f"  ... and {len(missing) - 20} more")
    else:
        print(f"\nAll {len(orig_md)} original pages preserved.")


if __name__ == "__main__":
    main()
