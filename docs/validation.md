# Documentation validation

This reorganization validates a course hub, not a Flutter application.

- `python3 tools/check_docs.py`: local links and anchors, ten ordered modules, both entry points, and fifty exercises with objectives and completion criteria.
- `git diff --check`: no whitespace errors.
- The archived README was compared with the original Git revision and preserved exactly.
- Public metadata, manifests and recent workflows were consulted for the 23 repositories in [the snapshot](repository-snapshot.json).
- Fourteen course article URLs were extracted from their current READMEs. Their publication and execution evidence belongs to those projects; this change does not edit Medium articles.
- All 34 distinct new official-documentation, author-book and learning-site URLs in the course guides returned HTTP 200 during the external-link review. The historical index was excluded from that availability claim.

The automated workflow checks course structure and internal navigation without network dependencies. External availability is a point-in-time observation. This change does not execute linked applications, book examples, external integrations or students' exercise solutions.
