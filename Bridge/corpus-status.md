# Bridge CLI Documentation Corpus

> Multi-product local knowledge base for RAG. Per-product catalogs hold the full TOC; this hub tracks scrape progress.

## Products

| Product | Version | Progress | Index | Notes |
|---------|---------|----------|-------|-------|
| Bridge CLI | latest | **178/178** (100.0%) | [index.md](index.md) | phase 1 |

## How to scrape

```powershell
python scripts/build-index.py --product bridge-latest --refresh-toc
python scripts/scrape-pending.py --product bridge-latest --all-pending
python scripts/build-index.py --product bridge-latest --hub
```

Registered product keys: `bridge-latest`.

---

*Full topic catalog: [index.md](index.md).*

