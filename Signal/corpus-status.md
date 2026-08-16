# Black Duck Signal Documentation Corpus

> Local knowledge base for RAG (Black Duck Signal). The product catalog holds the full TOC; this hub tracks scrape progress. See [PHASE-PLAN.md](PHASE-PLAN.md) and [CHECKPOINT.md](CHECKPOINT.md).

## Products

| Product | Version | Progress | Index | Notes |
|---------|---------|----------|-------|-------|
| Black Duck Signal | latest | **17/17** (100.0%) | [index.md](index.md) | primary |

## How to scrape

```powershell
python scripts/build-index.py --product signal-latest --init
python scripts/scrape-pending.py --product signal-latest --all-pending
python scripts/build-index.py --product signal-latest --hub
```

Phased scrape: see [PHASE-PLAN.md](PHASE-PLAN.md).

Registered product keys: `signal-latest`.

---

*Hub generated 2026-08-13T00:05:06.297513+00:00. Full TOC catalog: [index.md](index.md).*

