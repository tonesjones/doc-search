# Software Risk Manager corpus checkpoint

**Last updated:** 2026-09-08
**Status:** Complete standalone SRM corpus; use local Markdown for product questions.

## Initial import

- Selected the newer mutable SRM map `6dyNreOMuOAenymg0Owm8A` (map edition
  2026-09-08; docs v2026.9.0), rather than the older 2026-05-29 map.
- Scraped **286/286** topics with **0 errors**.
- Content is stored under `docs/`, with TOC and manifest under `sources/srm-latest/`.
- Validated with `python scripts/validate-corpus.py --product srm-latest`; the corpus
  tooling tests passed 3/3.
- SRM is a top-level product corpus. It must not be merged into the Black Duck SCA tree.

## Next action

Refresh SRM only when a version/content check is requested. Preserve this `latest`
snapshot and its history rather than overwriting it with another product corpus.
