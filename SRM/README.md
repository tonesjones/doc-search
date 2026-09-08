# Software Risk Manager Documentation Corpus

Standalone local Markdown corpus for Software Risk Manager (SRM). It is intentionally
separate from the Black Duck SCA, Coverity, and Polaris corpus roots.

## Snapshot

| Field | Value |
|---|---|
| Documentation version | latest (docs v2026.9.0) |
| Map edition | 2026-09-08 |
| Official map ID | `6dyNreOMuOAenymg0Owm8A` |
| Topics | 286/286 |
| Catalog | [index.md](index.md) |

The corpus uses the official Fluid Topics TOC/content APIs rather than the public
JavaScript application. Topic bodies live in `docs/`; source metadata and scrape state
are in `sources/srm-latest/`.

## Refresh and validation

```powershell
python scripts/scrape-pending.py --product srm-latest --refresh-changed
python scripts/build-index.py --product srm-latest --hub
python scripts/validate-corpus.py --product srm-latest
python -m unittest discover -s tests -p 'test_corpus_tools.py' -v
```

See [AGENTS.md](AGENTS.md) for retrieval and maintenance rules, and
[CHECKPOINT.md](CHECKPOINT.md) for current corpus history.
