# Contribution Guidelines

Please ensure your pull request adheres to the following guidelines:

- Make an individual pull request for each suggestion.
- Add your entry to the most specific section that already fits it, and only
  create a new section when none of the existing ones apply.
- Use this format for plugins and libraries: `[name](link) - Description`
- Keep the list free of duplicates: do not add a project that is already listed.
- Check your spelling and grammar.
- Remove any trailing whitespace.
- Send the pull request with a short note on why the project is awesome.

## Entry format

The list is checked automatically (see "Checking your contribution" below), so
entries must follow these rules:

- The link must be a valid Markdown link with **no space** between `]` and `(`:
  - Good: `[Flask-Login](https://github.com/maxcountryman/flask-login)`
  - Bad:  `[Flask-Login] (https://github.com/maxcountryman/flask-login)`
- In plugin/library sections, separate the link and the description with exactly
  one space, a hyphen and one space (` - `), and keep the description short,
  specific and non-empty:
  - Good: `[Flask-Login](...) - Flask user session management`
  - Bad:  `[Flask-Login](...) Flask user session management` (missing ` - `)
  - Bad:  `[Flask-Login](...)- Flask user session management` (missing space)

## Choosing a section

- Flask extensions, plugins and libraries go under the matching category in the
  first part of the README (Authentication, Database, Frontend, ...). Every entry
  there must have a description.
- Learning material and showcases go under **Resources**: Tutorials, Courses,
  Books, Slides, Videos, Built with Flask and Boilerplate. A description is
  optional in these sections.

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

- Please do not add paid courses/resources (there are so many we should not include them all here).
- Posts should be in a series and well structured. Please do not add a single post.

# Checking your contribution

Before opening a pull request, run the same check that CI runs (it only needs
Python 3, no extra packages):

```
python3 lint.py
```

It verifies the entry format, flags duplicate links and enforces the section
rules above.
