# Bridge CLI Documentation Corpus

This directory is a standalone, retrieval-friendly mirror of official Bridge CLI
documentation. Keep it separate from Black Duck SCA, Coverity, and Polaris.

## Source priority

1. Search local Markdown in `docs/`, `index.md`, and `corpus-status.md`.
2. Use the official Fluid Topics TOC/content APIs only when a refresh is requested.
3. Use general knowledge only when the corpus is silent; label uncertainty.

The documentation site is a JavaScript SPA. Do not scrape its HTML shell; use the
TOC/content APIs recorded in `sources/bridge-latest/manifest.json`.

## Current corpus

| Field | Value |
|---|---|
| Product key | `bridge-latest` |
| Documentation version | latest |
| Map ID | `ilBVZr_kR5v3KVjK1p~wbw` |
| Topics | 174/174 |
| Index | `index.md` |

## Working rules

- Read `CHECKPOINT.md` before resuming corpus work.
- Do not hand-edit generated topic rows in `index.md`; update the manifest and rebuild.
- Preserve the `latest` snapshot as a standalone Bridge corpus. Do not place Bridge
  content under `BlackDuck SCA/`.
- After a refresh, run `python scripts/validate-corpus.py --product bridge-latest` and
  `python -m unittest discover -s tests -p 'test_corpus_tools.py' -v`.

## Commands

```powershell
python scripts/build-index.py --list-products
python scripts/build-index.py --product bridge-latest --refresh-toc
python scripts/scrape-pending.py --product bridge-latest --all-pending
python scripts/scrape-pending.py --product bridge-latest --refresh-changed
python scripts/build-index.py --product bridge-latest --hub
python scripts/validate-corpus.py --product bridge-latest
python scripts/refresh-corpus.py --product bridge-latest
```
