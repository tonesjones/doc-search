# Black Duck Documentation Corpus

> Multi-product local knowledge base for RAG. Per-product catalogs hold the full TOC; this hub tracks scrape progress.

## Products

| Product | Version | Progress | Index | Notes |
|---------|---------|----------|-------|-------|
| Black Duck Documentation | 2026.7 | **941/941** (100.0%) | [index.md](index.md) | phase 1 |
| Black Duck Detect | 11.5.1 | **206/206** (100.0%) | [index-detect.md](index-detect.md) | phase 2 |
| Black Duck Alert | 8.4.0 | **45/45** (100.0%) | [index-alert.md](index-alert.md) | phase 2 |
| Bridge CLI | latest | **174/174** (100.0%) | [index-bridge.md](index-bridge.md) | phase 2 |
| Black Duck C/CPP Tool | latest | **14/20** (70.0%) | [index-c-cpp-tool.md](index-c-cpp-tool.md) | phase 2 |
| Black Duck Air-gapped KnowledgeBase | latest | not initialized | — | optional |

## How to scrape

```powershell
python scripts/build-index.py --product detect-11.5.1 --init
python scripts/scrape-pending.py --product detect-11.5.1 --all-pending
python scripts/build-index.py --product detect-11.5.1
```

Registered product keys: `blackduck-2026.7`, `detect-11.5.1`, `alert-8.4.0`, `bridge-latest`, `c-cpp-tool-latest`, `airgap-kb-latest`.

---

*Hub generated 2026-08-13T16:17:07.371611+00:00. Primary SCA detail index: [index.md → see also monoproduct builds](index.md).*

