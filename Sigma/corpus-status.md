# Black Duck Sigma Documentation Corpus

> Local knowledge base for RAG (Black Duck Sigma / Rapid Scan Static). The product catalog holds the full TOC; this hub tracks scrape progress. See [PHASE-PLAN.md](PHASE-PLAN.md) and [CHECKPOINT.md](CHECKPOINT.md).

## Products

| Product | Version | Progress | Index | Notes |
|---------|---------|----------|-------|-------|
| Sigma Documentation | 2026.8.0 | **59/59** (100.0%) | [index.md](index.md) | primary |

## How to scrape

```powershell
python scripts/build-index.py --product sigma-2026.8.0 --init
python scripts/scrape-pending.py --product sigma-2026.8.0 --all-pending
python scripts/build-index.py --product sigma-2026.8.0 --hub
```

Phased scrape: see [PHASE-PLAN.md](PHASE-PLAN.md).

Registered product keys: `sigma-2026.8.0`.

---

*Hub generated 2026-08-13T00:25:46.980320+00:00. Full TOC catalog: [index.md](index.md).*

