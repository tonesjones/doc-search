# Coverity Documentation Corpus

> Local knowledge base for RAG (Coverity Documentation). Per-product catalogs hold the full TOC; this hub tracks scrape progress. See [PHASE-PLAN.md](PHASE-PLAN.md) and [CHECKPOINT.md](CHECKPOINT.md).

## Products

| Product | Version | Progress | Index | Notes |
|---------|---------|----------|-------|-------|
| Coverity Documentation | 2026.6 | **4443/4443** (100.0%) | [index.md](index.md) | primary |

## How to scrape

```powershell
python scripts/build-index.py --product coverity-2026.6 --init
python scripts/scrape-pending.py --product coverity-2026.6 --all-pending
python scripts/build-index.py --product coverity-2026.6 --hub
```

Phased scrape: see [PHASE-PLAN.md](PHASE-PLAN.md).

Registered product keys: `coverity-2026.6`.

---

*Hub generated 2026-08-12T23:46:18.307415+00:00. Full TOC catalog: [index.md](index.md).*

