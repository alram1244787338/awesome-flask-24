#!/usr/bin/env python3
"""Offline, deterministic structural checks for README.md.

Unlike a dead-link checker, this does not touch the network, so it gives CI a
stable signal: if it fails, the README really is malformed.

Checks performed:
  1. Anchors resolve  -- every in-page link `](#slug)` points at a real heading.
  2. Link syntax      -- no broken Markdown links of the form `] (` (a space
                         between the link text and the URL renders as plain text).
  3. Entry format     -- list items follow `[NAME](URL)` optionally followed by
                         ` - DESCRIPTION` (the format documented in CONTRIBUTING.md).

Exit code is non-zero with line-numbered errors when any check fails.
"""
import re
import sys
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"

# Characters stripped by GitHub's heading-slug algorithm (github-slugger).
# Note: hyphen and underscore are intentionally kept.
_SLUG_STRIP = re.compile(
    "[\u2000-\u206F\u2E00-\u2E7F"
    + re.escape("\\'!\"#$%&()*+,./:;<=>?@[]^`{|}~")
    + "]"
)
_IMAGE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
_LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")

_HEADING = re.compile(r"^(#+)\s+(.*?)\s*$")
_LIST_ITEM = re.compile(r"^\s*[-*]\s+(.*)$")
_PRIMARY_LINK = re.compile(r"^\[[^\]]+\]\(([^)]+)\)(.*)$")
_ANCHOR_LINK = re.compile(r"\]\(#([^)]+)\)")
_BROKEN_LINK = re.compile(r"\]\s+\(")


def slugify(text):
    """Reproduce a GitHub heading anchor from raw Markdown heading text."""
    text = _IMAGE.sub("", text)        # images contribute no anchor text
    text = _LINK.sub(r"\1", text)      # links collapse to their visible text
    text = text.strip().lower()
    text = _SLUG_STRIP.sub("", text)
    text = text.replace(" ", "-")
    return text


def collect_headings(lines):
    """Map every heading to its GitHub anchor, deduping like github-slugger."""
    headings = set()
    counts = {}
    for line in lines:
        m = _HEADING.match(line)
        if not m:
            continue
        slug = slugify(m.group(2))
        if slug in counts:
            counts[slug] += 1
            slug = f"{slug}-{counts[slug]}"
        else:
            counts[slug] = 0
        headings.add(slug)
    return headings


def check(lines):
    headings = collect_headings(lines)
    errors = []

    for i, line in enumerate(lines, 1):
        for target in _ANCHOR_LINK.findall(line):
            if target not in headings:
                errors.append(f"{i}: anchor '#{target}' has no matching heading")

        if _BROKEN_LINK.search(line):
            errors.append(
                f"{i}: broken link syntax (space between ']' and '('): {line.strip()}"
            )

        item = _LIST_ITEM.match(line)
        if item:
            primary = _PRIMARY_LINK.match(item.group(1))
            if primary:
                rest = primary.group(2)
                if rest.strip() and not rest.startswith(" - "):
                    errors.append(
                        f"{i}: entry description must be separated by ' - ': "
                        f"{line.strip()}"
                    )

    return headings, errors


def main():
    if not README.exists():
        print(f"README not found at {README}", file=sys.stderr)
        return 2

    lines = README.read_text(encoding="utf-8").splitlines()
    headings, errors = check(lines)

    if errors:
        print("README.md validation FAILED:\n")
        for e in errors:
            print("  " + e)
        print(f"\n{len(errors)} problem(s) found.")
        return 1

    print(
        "README.md validation passed: "
        f"{len(headings)} headings, all in-page anchors resolve, "
        "all list entries well-formed."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
