# Website validation and engineering log

## Scope

The website presents this course repository on GitHub Pages. It has thirty-two static pages: home, ten modules, laboratories, books, projects, guide and resources in each language. All fifty exercises are available in Portuguese and English. It does not add an application backend or replace the case-study repositories.

## Implementation and evidence

1. Added generation checks first; the initial run failed because the website generator was absent.
2. Built Portuguese pages from the existing lesson guides and reviewed English content separately, preserving proper book and repository names.
3. Added six automated checks covering all nested page/asset links, anchors, exercise counts, corresponding module destinations across languages, all project destinations, books/Masmorra references and safe rendering of code examples.
4. Preserved the rendering behavior with tests, then simplified the Markdown renderer. The complexity-only inspection reported a maximum cyclomatic complexity of 9; coverage and CRAP scores were not measured. Duplicate analysis at threshold 0.8 found no candidates. Mutation tooling was used in scan mode only; no mutation score is claimed.
5. Checked the actual local website at the GitHub project subpath in the browser. Verified accent-insensitive search, exercise navigation and switching the persistence module to English while retaining `#exercises` and all five exercises.
6. Checked 390 × 844 and 320 × 740 layouts. Confirmed the mobile menu, keyboard Escape/return of focus, book and Masmorra links, all 23 project cards, and no horizontal overflow in the inspected pages.

## Repeatable checks

```sh
python3 tools/check_docs.py
python3 tools/test_site.py
node --check site/assets/site.js
git diff --check
```

The documentation workflow runs the Python checks before deploying the generated output from `master`. Browser inspection complements these checks; the static tests do not assert that external services or linked applications run.

Portuguese lesson updates are reflected by the generator. English translations in `site/content/en.json` should be reviewed whenever the source lessons change.

## Labs and blue/cyan navigation revision

- Verified the seven package names, published versions and owning repository links against pub.dev before adding them to `site/content/labs.json`.
- Added twenty-one English/Portuguese laboratory suggestions across all ten modules. Online exploration and proposed project integrations are labeled separately. The fifty exercises remain intact.
- Expanded automated checks to eleven, including all seven package/lab destinations, per-module suggestions, removal of arrow glyphs, grouped footer and single current-flag disclosure.
- Inspected desktop, 390px and 320px layouts in the browser. The module language switch retained `#labs`; the active in-page tab matched the section and the inspected pages had no horizontal overflow.
- Verified the language disclosure opens with Enter, hides the inactive language when closed and closes with Escape while returning focus to its trigger. Inspected the grouped footer at 320px.

## Covers, imagery and container revision

- Added nine visually verified official book covers, with intrinsic dimensions, original source URLs, author attribution and module recommendations.
- Preserved the distinction between Masmorra’s first-volume cover and the wider Masmorra learning website.
- Added three actual application screenshots with their original MIT notices and source attribution.
- Expanded automated checks to thirteen: cover presence in both languages, representative images, shared container configuration and reduced-motion styling are included.
- In the browser at 1600px, header, book heading and cover collection all measured 1280px and shared the same left edge. At 390px the nine covers and translated book page had no horizontal overflow.
- Verified the three case-study images loaded in the English home page. Animated entrance and hover effects remain optional under the reduced-motion media rule.
- Added content-versioned asset URLs for coherent stylesheet/script/image updates.
