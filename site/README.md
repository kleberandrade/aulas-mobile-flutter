# Course website

Public addresses: [Português](https://kleberandrade.github.io/aulas-mobile-flutter/) and [English](https://kleberandrade.github.io/aulas-mobile-flutter/en/).

The repository remains a course hub. The website is a static presentation of its existing teaching material, with thirty-two directly addressable HTML pages and no server runtime, package installation or external JavaScript dependency.

## Build and preview

Use Python 3.9 or newer:

```sh
python3 tools/check_docs.py
python3 tools/test_site.py
python3 -m http.server 8000 --directory site/dist
```

Open `http://localhost:8000/`. The test command builds the site and verifies every local page/asset destination, exercise anchors, both languages, project links and book references. To build without running tests, use `python3 tools/build_site.py`.

## Content sources

- Portuguese modules: `lessons/*/README.md`.
- Portuguese books, guide and resources: their corresponding files in `docs/`.
- English teaching content and all fifty translated exercises: `site/content/en.json`.
- Laboratory/package catalog and bilingual module suggestions: `site/content/labs.json`.
- Shared project destinations and article links: `docs/repository-snapshot.json`.
- Navigation, localized interface labels and layout: `tools/build_site.py`.
- Styling, original book/code logo, circular flags and progressive-enhancement interactions: `site/assets/`.

Keep Portuguese and English content synchronized. Every module must have five exercises, with both an objective and completion criteria. Book titles remain in their original language. Proper names and repository names are not translation omissions.

The laboratory catalog links all seven published packages, their online labs and source repositories. Each module includes contextual activities, identified as online exploration or proposed integration. Package versions are a dated lookup, not a claim that the site automatically follows releases.

The site works as ordinary static links when JavaScript is unavailable. JavaScript adds the mobile menu, accent-insensitive module search and preservation of the section fragment during language changes. The header shows only the current circular flag; its disclosure opens the language options. The footer groups learning, exploration and course-context links. Search is browser-local. There are no accounts, trackers or stored exercise data. Explicit page URLs determine the displayed language and preserve it on reload.

## GitHub Pages

The documentation workflow builds and tests before uploading `site/dist/` as the Pages artifact. Deployment runs only for the default `master` branch, after checks pass. Pull requests run checks without deployment. GitHub Pages must use GitHub Actions as its build source.

Generated output is ignored by Git. Pages and asset links are relative, supporting the `/aulas-mobile-flutter/` project prefix and direct navigation to nested modules. Canonical and alternate-language URLs use the public address above; update `PUBLIC` in the generator if the repository or domain moves.
