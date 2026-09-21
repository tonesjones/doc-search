# Bridge CLI Documentation Corpus

Standalone local Markdown corpus for Bridge CLI. It is intentionally separate from
the Black Duck SCA, Coverity, and Polaris corpus roots.

## Snapshot

| Field | Value |
|---|---|
| Documentation version | latest |
| Official map ID | `ilBVZr_kR5v3KVjK1p~wbw` |
| Topics | 174/174 |
| Catalog | [index.md](index.md) |

The corpus uses the official Fluid Topics TOC/content APIs rather than the public
JavaScript application. Topic bodies live in `docs/`; source metadata and scrape state
are in `sources/bridge-latest/`.

## Refresh and validation

```powershell
python scripts/scrape-pending.py --product bridge-latest --refresh-changed
python scripts/build-index.py --product bridge-latest --hub
python scripts/validate-corpus.py --product bridge-latest
python -m unittest discover -s tests -p 'test_corpus_tools.py' -v
```

See [AGENTS.md](AGENTS.md) for retrieval and maintenance rules, and
[CHECKPOINT.md](CHECKPOINT.md) for current corpus history.
