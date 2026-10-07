# Black Duck Code Sight Documentation Corpus

> Local knowledge base for RAG (Black Duck Code Sight). The product catalog holds the full TOC; this hub tracks scrape progress. See [PHASE-PLAN.md](PHASE-PLAN.md) and [CHECKPOINT.md](CHECKPOINT.md).

## Products

| Product | Version | Progress | Index | Notes |
|---------|---------|----------|-------|-------|
| Black Duck Code Sight | 2026.9.0 | **233/233** (100.0%) | [index.md](index.md) | primary |

## How to scrape

```powershell
python scripts/build-index.py --product codesight-2026.9.0 --init
python scripts/scrape-pending.py --product codesight-2026.9.0 --all-pending
python scripts/build-index.py --product codesight-2026.9.0 --hub
```

Phased scrape: see [PHASE-PLAN.md](PHASE-PLAN.md).

Registered product keys: `codesight-2026.9.0`.

---

*Hub generated 2026-10-06T23:40:25.315900+00:00. Full TOC catalog: [index.md](index.md).*

