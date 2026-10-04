# Black Duck Sigma Documentation Corpus

> Local knowledge base for RAG (Black Duck Sigma / Rapid Scan Static). The product catalog holds the full TOC; this hub tracks scrape progress. See [PHASE-PLAN.md](PHASE-PLAN.md) and [CHECKPOINT.md](CHECKPOINT.md).

## Products

| Product | Version | Progress | Index | Notes |
|---------|---------|----------|-------|-------|
| Sigma Documentation | 2026.8.0 | **59/59** (100.0%) | [index-sigma-2026.8.0.md](index-sigma-2026.8.0.md) | historical |
| Sigma Documentation | 2026.9.1 | **59/59** (100.0%) | [index.md](index.md) | primary |

## How to scrape

```powershell
python scripts/build-index.py --product sigma-2026.9.1 --init
python scripts/scrape-pending.py --product sigma-2026.9.1 --all-pending
python scripts/build-index.py --product sigma-2026.9.1 --hub
```

Phased scrape: see [PHASE-PLAN.md](PHASE-PLAN.md).

Registered product keys: `sigma-2026.8.0`, `sigma-2026.9.1`.

---

*Hub generated 2026-10-04T23:34:30.281439+00:00. Full TOC catalog: [index.md](index.md).*

