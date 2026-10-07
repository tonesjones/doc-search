# Black Duck Signal Documentation Corpus

> Local knowledge base for RAG (Black Duck Signal). The product catalog holds the full TOC; this hub tracks scrape progress. See [PHASE-PLAN.md](PHASE-PLAN.md) and [CHECKPOINT.md](CHECKPOINT.md).

## Products

| Product | Version | Progress | Index | Notes |
|---------|---------|----------|-------|-------|
| Black Duck Signal | latest | **32/32** (100.0%) | [index.md](index.md) | primary |

## How to scrape

```powershell
python scripts/build-index.py --product signal-latest --init
python scripts/scrape-pending.py --product signal-latest --all-pending
python scripts/build-index.py --product signal-latest --hub
```

Phased scrape: see [PHASE-PLAN.md](PHASE-PLAN.md).

Registered product keys: `signal-latest`.

---

*Hub generated 2026-10-04T23:34:30.506188+00:00. Full TOC catalog: [index.md](index.md).*

