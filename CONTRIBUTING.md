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

- Please do not add paid courses/resources (there are so many we should not include them all here)
- Posts should be in series and well structured. Please do not add single post.

# Maintaining Existing Entries

This list decays over time — libraries get abandoned, URLs change, and
projects get superseded.  When you notice a stale entry, please help:

1. **Broken link** — check whether the project moved (e.g. a GitHub
   repo transferred to a new owner).  If so, update the URL.
   If the project is truly gone and has no successor, remove the entry.
2. **Superseded project** — if a library has an official successor
   (e.g. `Flask-RestPlus` → `flask-restx`), keep the old entry but add
   a note pointing to the successor:
   `(**no longer maintained** — see [successor](url))`.
3. **Unmaintained project** — if a repo has had no commits for 2+ years
   and open issues are unanswered, append `(appears unmaintained)` to
   the description so readers know what to expect.
4. **Duplicate entries** — each project should appear in at most one
   section.  If a library fits multiple categories, pick the most
   specific one.

CI runs a link checker ([lychee](https://lychee.cli.rs/)) on every PR
that touches `README.md` and weekly on `master`.  The configuration
lives in `.lychee.toml` — every excluded URL pattern **must** have an
inline comment explaining why it is excluded.  Do not add blanket
exclusions just to make CI pass; fix the underlying entry instead.
