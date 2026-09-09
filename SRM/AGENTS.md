# Software Risk Manager Documentation Corpus

This directory is a standalone, retrieval-friendly mirror of official Software Risk
Manager documentation. Keep it separate from Black Duck SCA, Coverity, and Polaris.

## Source priority

1. Search local Markdown in `docs/`, `index.md`, and `corpus-status.md`.
2. Use the official Fluid Topics TOC/content APIs only when a refresh is requested.
3. Use general knowledge only when the corpus is silent; label uncertainty.

The documentation site is a JavaScript SPA. Do not scrape its HTML shell; use the
TOC/content APIs recorded in `sources/srm-latest/manifest.json`.

## Current corpus

| Field | Value |
|---|---|
| Product key | `srm-latest` |
| Documentation version | latest (map edition 2026-09-08; docs v2026.9.0) |
| Map ID | `6dyNreOMuOAenymg0Owm8A` |
| Topics | 286/286 |
| Index | `index.md` |

## Working rules

- Read `CHECKPOINT.md` before resuming corpus work.
- Do not hand-edit generated topic rows in `index.md`; update the manifest and rebuild.
- Preserve the `latest` snapshot as a standalone SRM corpus. Do not place SRM content
  under `BlackDuck SCA/`.
- After a refresh, run `python scripts/validate-corpus.py --product srm-latest` and
  `python -m unittest discover -s tests -p 'test_corpus_tools.py' -v`.

## Commands

```powershell
python scripts/build-index.py --list-products
python scripts/build-index.py --product srm-latest --refresh-toc
python scripts/scrape-pending.py --product srm-latest --all-pending
python scripts/scrape-pending.py --product srm-latest --refresh-changed
python scripts/build-index.py --product srm-latest --hub
python scripts/validate-corpus.py --product srm-latest
python scripts/refresh-corpus.py --product srm-latest
```
