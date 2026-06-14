#!/usr/bin/env python3
"""Minimal format linter for the Awesome Flask list.

It enforces the rules documented in CONTRIBUTING.md so that a passing run
proves the README and the contribution guidelines stay in sync.

Checks performed on every list entry (lines starting with ``- [``):

* the entry must begin with a valid Markdown link ``[name](link)`` with no
  space between ``]`` and ``(``;
* if anything follows the link it must be separated by a space;
* entries in plugin/library sections must use ``" - "`` before a non-empty
  description (Resources sections may omit the description);
* the same link must not appear twice anywhere in the list.

Table-of-contents entries (anchor links such as ``[Framework](#framework)``)
are ignored. Run with no arguments to lint ``README.md`` or pass a path.

Exit code is 0 when the file is clean and 1 when any problem is found.
"""

import re
import sys

# Start of a top-level list entry: "- [name](link)..."
ENTRY_RE = re.compile(r"^- \[[^\]]+\]\([^)]+\)")
# First Markdown link on the line (the primary resource link).
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
# A valid plugin description: " - " followed by at least one non-space char.
PLUGIN_DESC_RE = re.compile(r"^ - \S")


def normalize_url(url):
    """Normalize a URL for duplicate detection."""
    return url.strip().lower().rstrip("/")


def lint(path):
    with open(path, encoding="utf-8") as handle:
        lines = handle.readlines()

    problems = []
    seen_urls = {}
    # Plugins come before the "# Resources" heading; everything after it is a
    # Resources section where a description is optional.
    in_resources = False

    for number, raw in enumerate(lines, start=1):
        line = raw.rstrip("\n")

        if line.startswith("# Resources"):
            in_resources = True
            continue

        if not line.startswith("- ["):
            continue

        primary = LINK_RE.search(line)
        # Skip table-of-contents / anchor entries.
        if primary and primary.group(2).startswith("#"):
            continue

        if "] (" in line:
            problems.append(
                (number, "space between ']' and '(' breaks the Markdown link")
            )
            continue

        match = ENTRY_RE.match(line)
        if not match:
            problems.append(
                (number, "malformed entry, expected '- [name](link) ...'")
            )
            continue

        url = primary.group(2)
        remainder = line[match.end():]

        if remainder and not remainder.startswith(" "):
            problems.append(
                (number, "missing space between the link and the description")
            )
        elif not in_resources and not PLUGIN_DESC_RE.match(remainder):
            problems.append(
                (number, "plugin entries need ' - ' before a non-empty description")
            )

        key = normalize_url(url)
        if key in seen_urls:
            problems.append(
                (number, "duplicate link, already used on line %d" % seen_urls[key])
            )
        else:
            seen_urls[key] = number

    return problems


def main(argv):
    path = argv[1] if len(argv) > 1 else "README.md"
    problems = lint(path)
    if problems:
        for number, message in problems:
            print("%s:%d: %s" % (path, number, message))
        print("\n%d problem(s) found." % len(problems))
        return 1
    print("%s: OK" % path)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
