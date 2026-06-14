#!/usr/bin/env python3
"""
Validate README.md against the contribution guidelines in CONTRIBUTING.md.

Checks performed:
1. All entries in sections requiring descriptions have them (with minimum length).
2. No duplicate URLs across the entire file.
3. Markdown link syntax is correct (no stray spaces, broken brackets, etc.).
4. Table of Contents links match actual section headings.
5. Known spelling/typo checks on section headings and common mistakes.
6. Description separator ` - ` is used consistently where required.
"""

import re
import sys
import os
from collections import Counter

README_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'README.md')

# Sections where entries MUST have ` - Description` format
SECTIONS_REQUIRING_DESCRIPTION = {
    'Framework',
    'Admin interface',
    'Analytics',
    'Authentication',
    'Authorization',
    'Database',
    'Database Migrations',
    'Session',
    'Cache',
    'Data Validation',
    'Email',
    'i18n',
    'Full-text searching',
    'Rate Limiting',
    'Task Queue',
    'Exception tracking',
    'Tracing',
    'APM',
    'Other SDK',
    'Frontend',
    'Development (Debugging/Testing/Documentation)',
    'Utils',
    'Built with Flask',
    'Boilerplate',
}

# Sections that use simplified format (title-only links allowed)
SECTIONS_SIMPLIFIED_FORMAT = {
    'Tutorials',
    'Courses',
    'Books',
    'Slides',
    'Videos',
}

# Minimum description length (characters) for sections requiring descriptions
MIN_DESCRIPTION_LENGTH = 10

# Regex patterns
# Matches: - [Name](URL) - Description
ENTRY_WITH_DESC = re.compile(
    r'^- \[([^\]]+)\]\(([^)]+)\)\s+-\s+(.+)$'
)
# Matches: - [Name](URL)  (no description)
ENTRY_WITHOUT_DESC = re.compile(
    r'^- \[([^\]]+)\]\(([^)]+)\)\s*$'
)
# Matches: - [Name](URL) (by Author)  — simplified format with author
ENTRY_WITH_AUTHOR = re.compile(
    r'^- \[([^\]]+)\]\(([^)]+)\)\s+\(by\s+[^)]+\)\s*$'
)
# Matches malformed links like [Name] (URL) with space before paren
MALFORMED_LINK_SPACE = re.compile(
    r'^- \[[^\]]+\]\s+\(http'
)
# Matches )- (no space before dash separator)
MALFORMED_DASH = re.compile(
    r'^- \[[^\]]+\]\([^)]+\)-\s'
)
# Heading pattern
HEADING = re.compile(r'^(#{1,4})\s+(.+)$')
# TOC link pattern
TOC_LINK = re.compile(r'^\s+-\s+\[([^\]]+)\]\(#([^)]+)\)')


def slugify(text):
    """Convert heading text to markdown anchor slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s]+', '-', text.strip())
    return text


def parse_readme(content):
    """Parse README into sections with their entries."""
    sections = {}
    current_section = None
    current_entries = []
    toc_entries = []
    headings = []

    for line in content.split('\n'):
        # Track TOC entries
        toc_match = TOC_LINK.match(line)
        if toc_match:
            toc_entries.append((toc_match.group(1), toc_match.group(2)))
            continue

        heading_match = HEADING.match(line)
        if heading_match:
            if current_section is not None:
                sections[current_section] = current_entries
            current_section = heading_match.group(2).strip()
            headings.append(current_section)
            current_entries = []
            continue

        if current_section and line.startswith('- ['):
            current_entries.append(line)

    if current_section is not None:
        sections[current_section] = current_entries

    return sections, toc_entries, headings


def check_missing_descriptions(sections):
    """Check for entries that should have descriptions but don't."""
    errors = []
    for section, entries in sections.items():
        if section not in SECTIONS_REQUIRING_DESCRIPTION:
            continue
        for entry_line in entries:
            if MALFORMED_LINK_SPACE.match(entry_line):
                errors.append(f"[FORMAT] Malformed link (space before parenthesis): {entry_line.strip()}")
                continue
            if MALFORMED_DASH.match(entry_line):
                errors.append(f"[FORMAT] Missing space before dash separator: {entry_line.strip()}")
                continue
            if ENTRY_WITH_DESC.match(entry_line):
                continue
            if ENTRY_WITHOUT_DESC.match(entry_line):
                errors.append(f"[MISSING_DESC] Entry in '{section}' has no description: {entry_line.strip()}")
            elif not ENTRY_WITH_DESC.match(entry_line):
                errors.append(f"[FORMAT] Unrecognized entry format in '{section}': {entry_line.strip()}")
    return errors


def check_description_length(sections):
    """Check that descriptions meet minimum length."""
    errors = []
    for section, entries in sections.items():
        if section not in SECTIONS_REQUIRING_DESCRIPTION:
            continue
        for entry_line in entries:
            match = ENTRY_WITH_DESC.match(entry_line)
            if match:
                description = match.group(3).strip()
                if len(description) < MIN_DESCRIPTION_LENGTH:
                    errors.append(
                        f"[SHORT_DESC] Description too short ({len(description)} chars, min {MIN_DESCRIPTION_LENGTH}) "
                        f"in '{section}': {entry_line.strip()}"
                    )
    return errors


def check_duplicate_urls(sections):
    """Check for duplicate URLs across all sections."""
    errors = []
    url_pattern = re.compile(r'\((https?://[^)]+)\)')
    all_urls = []

    for section, entries in sections.items():
        for entry_line in entries:
            matches = url_pattern.findall(entry_line)
            for url in matches:
                # Normalize: strip trailing slash for comparison
                normalized = url.rstrip('/')
                all_urls.append((normalized, section, entry_line.strip()))

    url_counts = Counter(url for url, _, _ in all_urls)
    seen_dupes = set()
    for url, section, line in all_urls:
        if url_counts[url] > 1 and url not in seen_dupes:
            seen_dupes.add(url)
            locations = [s for u, s, _ in all_urls if u == url]
            errors.append(f"[DUPLICATE] URL appears in multiple sections: {url} (in: {', '.join(locations)})")

    return errors


def check_toc_vs_headings(toc_entries, headings):
    """Check that TOC links match actual headings."""
    errors = []
    heading_slugs = {slugify(h): h for h in headings}

    for toc_text, toc_slug in toc_entries:
        if toc_slug not in heading_slugs:
            errors.append(f"[TOC] TOC link '#{toc_slug}' does not match any heading (text: '{toc_text}')")

    return errors


def check_spelling(content):
    """Check for common spelling mistakes."""
    errors = []
    known_typos = {
        'cources': 'courses',
        'sytnax': 'syntax',
        'sytnactic': 'syntactic',
        'libary': 'library',
        'libaries': 'libraries',
        'extention': 'extension',
        'extentions': 'extensions',
        'seperate': 'separate',
        'recieve': 'receive',
        'acheive': 'achieve',
        'occured': 'occurred',
        'sucessful': 'successful',
    }
    for typo, correction in known_typos.items():
        if re.search(r'\b' + typo + r'\b', content, re.IGNORECASE):
            errors.append(f"[SPELLING] Found '{typo}', should be '{correction}'")
    return errors


def check_section_in_contributing(sections):
    """Check that all sections are covered by CONTRIBUTING.md rules."""
    errors = []
    all_known = SECTIONS_REQUIRING_DESCRIPTION | SECTIONS_SIMPLIFIED_FORMAT | {'Awesome Flask', 'Resources'}
    for section in sections.keys():
        # Skip top-level title (level-1 headings may contain badges/images)
        section_base = re.sub(r'\s*\[!\[.*?\]\(.*?\)\]\(.*?\)', '', section).strip()
        if section_base in all_known or section_base.startswith('Awesome'):
            continue
        if section not in all_known:
            errors.append(f"[SECTION] Section '{section}' not covered in CONTRIBUTING.md rules — consider adding it")
    return errors


def main():
    if not os.path.exists(README_PATH):
        print(f"ERROR: README.md not found at {README_PATH}")
        return 1

    with open(README_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    sections, toc_entries, headings = parse_readme(content)

    all_errors = []
    all_errors.extend(check_missing_descriptions(sections))
    all_errors.extend(check_description_length(sections))
    all_errors.extend(check_duplicate_urls(sections))
    all_errors.extend(check_toc_vs_headings(toc_entries, headings))
    all_errors.extend(check_spelling(content))
    all_errors.extend(check_section_in_contributing(sections))

    if all_errors:
        print(f"VALIDATION FAILED — {len(all_errors)} issue(s) found:\n")
        for error in all_errors:
            print(f"  {error}")
        print(f"\nTotal: {len(all_errors)} issue(s)")
        return 1
    else:
        print("VALIDATION PASSED — README.md conforms to contribution guidelines.")
        return 0


if __name__ == '__main__':
    sys.exit(main())
