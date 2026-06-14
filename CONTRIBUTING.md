# Contribution Guidelines

Please ensure your pull request adheres to the following guidelines:

## General Rules

- Make an individual pull request for each suggestion.
- Check your spelling and grammar before submitting.
- Remove any trailing whitespace.
- Send a Pull Request with a brief explanation of why the resource is awesome and relevant to Flask.

## Entry Format

### Extensions, Libraries, and "Built with Flask" / "Boilerplate" sections

Every entry **must** follow this exact format:

```
- [Resource Name](https://link-to-resource) - A concise, specific description of what it does.
```

### Tutorials, Courses, Books, Slides, and Videos sections

These sections use a simplified format where the link text itself describes the resource:

```
- [Title of the Resource](https://link-to-resource)
- [Title of the Resource](https://link-to-resource) (by Author/Organization)
```

The title must be descriptive enough to convey what the resource covers. Optionally add the author or platform in parentheses.

### Format Details

- **Resource Name**: Use the official project name (as it appears on PyPI, GitHub, or the project's homepage).
- **Link**: Use a stable, canonical URL:
  - For Flask extensions: prefer the **GitHub repository** URL.
  - For tutorials/articles: use the **direct link** to the content.
  - For courses/books: use the **official page** (publisher or platform).
  - Do **not** use URL shorteners, affiliate links, or tracking URLs.
- **Description**: Must be present and non-empty. Requirements:
  - At least **10 characters** long (excluding the dash and leading space).
  - Must describe **what the resource does** or **what the reader will learn** — not just repeat the name.
  - Must be a complete sentence or phrase, ending with a period is preferred.
  - Avoid vague phrases like "awesome", "great", "useful", or "cool".

### Examples

Good:
```
- [Flask-Limiter](https://github.com/alisaifee/flask-limiter) - Provides rate limiting features to Flask routes.
- [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) - Comprehensive multi-part tutorial covering Flask from basics to deployment.
```

Bad:
```
- [Flask-Limiter](https://github.com/alisaifee/flask-limiter)          (no description)
- [Flask-Limiter](https://github.com/alisaifee/flask-limiter) - Cool!  (too vague)
- [flask-limiter](https://github.com/alisaifee/flask-limiter) - A library.  (too short, not specific)
```

## Category Rules

- Place your entry in the **most specific** existing category. Do not create a new category unless no existing one fits.
- Each entry should appear in **exactly one** category. Do not add the same resource to multiple sections.
- If a resource fits under "Framework" as a full API framework, it should not also be listed under "Utils" or "Development".

## Resource Type Guidelines

### Extensions / Libraries (most categories under "Awesome Flask")
- Must be a **Flask extension** or a library with **direct, documented Flask integration**.
- Generic Python libraries that happen to work with Flask but have no Flask-specific support belong elsewhere (e.g., a general Python awesome list).

### Tutorials / Courses / Books (under "Resources")
- Must be **primarily about Flask** or use Flask as the main framework.
- Single blog posts are acceptable only if they are in-depth and self-contained. Casual or very short posts should not be added.
- Paid courses and books **are allowed** in the Resources section, but must be clearly marked with their platform (e.g., Udacity, Packt, O'Reilly).
- Do **not** add paid resources to the extensions/libraries sections.

### Built with Flask
- Must be an **open-source** project that is **built primarily with Flask**.
- Each entry must have a description explaining what the project does.
- Abandoned projects with no activity for over 2 years may be removed.

### Boilerplate
- Must be a **starter template or scaffold** for Flask projects.
- Must include a description of what stack/features it provides.

## Quality Standard

To be on the list, project repositories should adhere to these quality standards:

- **Python 3 supported** (Python 2-only projects are no longer accepted).
- **Code functions as documented and expected**.
- **Actively maintained**:
  - Regular, recent commits; OR
  - For finished/stable projects, issues and pull requests are responded to in a reasonable time.
- **Thoroughly documented** (README at minimum; docs site preferred for larger projects).
- **Tests, where practical**.

For resources (tutorials, courses, books):

- Must be **up-to-date** or still relevant (Flask 1.x+ content preferred; Flask 0.x content may be rejected).
- Posts should be **in-depth or part of a series**. Please do not add single, shallow blog posts.
- Paid resources are allowed in the Resources section only (not in the extensions sections).

## What Will Get Rejected

- Entries with **no description** or descriptions shorter than 10 characters.
- **Duplicate entries** (same resource listed in multiple categories).
- Resources with **no Flask-specific relevance**.
- **Broken links** or links to non-existent projects.
- Entries with **typographical errors** in the name or description.
- Resources that have been **abandoned** with no maintained fork.
