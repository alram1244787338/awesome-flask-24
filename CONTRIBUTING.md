# Contribution Guidelines

Please ensure your pull request adheres to the following guidelines:

- Make an individual pull request for each suggestion.
- Use the following format: \[RESOURCE\]\(LINK\) - DESCRIPTION.
- Check your spelling and grammar.
- Remove any trailing whitespace.
- Send a Pull Request with the reason why the library is awesome.

# Quality Standard

To be on the list, project repositories should adhere to these quality standards:

- Python 3 supported
- Code functions as documented and expected
- Actively maintained
    - Regular, recent commits
    - Or, for finished projects, issues and pull requests are responded to
- Thoroughly documented
- Tests, where practical

For resources

- Please do not add paid cources/resources (there are so many we should not include theme all here)
- Posts should be in series and well structured. Please do not add single post.

# Handling broken or stale resources

This list is checked automatically by CI ([lychee](https://github.com/lycheeverse/lychee),
see `.github/workflows/links.yml`). A green run means every link resolves; a red
one means at least one link is genuinely unreachable.

Keeping the list healthy is not only about *adding* entries -- existing ones rot
over time (projects get archived, blogs disappear, repositories are renamed). If
you notice, or CI reports, a broken entry:

- **Moved/renamed project:** update the URL to its current canonical home (e.g. a
  repo transferred to an official org). Prefer the resolved URL over a redirecting
  one, so the link does not silently break again when the old path is removed.
- **Permanently gone:** remove the entry. If it is a valuable *free* resource that
  has a working mirror (e.g. a book's source repository), repoint it there instead.
- **Paid or low-value and stale:** remove it rather than keeping it on life support.

Do **not** silence a failure by adding the URL to the `exclude` list in
`lychee.toml` unless you have *confirmed in a browser* that the resource is alive
and the failure is a false positive (some sites deliberately block automated
checkers). Every exclude entry must be scoped as tightly as possible and carry a
comment with the reason and the date it was verified. The exclude list is for
false positives only -- never for hiding genuinely dead links.

## Checking links locally

The same check CI runs can be run locally with [lychee](https://github.com/lycheeverse/lychee):

```sh
brew install lychee        # macOS; other install options are in the lychee README
lychee --config lychee.toml README.md CONTRIBUTING.md
```
