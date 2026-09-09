# Black Duck Documentation Corpus

> Multi-product local knowledge base for RAG. Per-product catalogs hold the full TOC; this hub tracks scrape progress.

## Products

| Product | Version | Progress | Index | Notes |
|---------|---------|----------|-------|-------|
| Black Duck Documentation | 2026.7 | **941/941** (100.0%) | [index.md](index.md) | phase 1 |
| Black Duck Detect | 11.5.1 | **206/206** (100.0%) | [index-detect-11.5.1.md](index-detect-11.5.1.md) | historical/version-specific |
| Black Duck Detect | 12.0.0 | **207/207** (100.0%) | [index-detect-12.0.0.md](index-detect-12.0.0.md) | default for unversioned questions |
| Black Duck Alert | 8.4.0 | **45/45** (100.0%) | [index-alert.md](index-alert.md) | phase 2 |
| Bridge CLI | latest | **174/174** (100.0%) | [index-bridge.md](index-bridge.md) | phase 2 |
| Black Duck C/CPP Tool | latest | **20/20** (100.0%) | [index-c-cpp-tool.md](index-c-cpp-tool.md) | phase 2 |
| Black Duck SCA MCP Server | main@6dac85b23b14899dc6c463a1021171356f381570 | **2/2** (100.0%) | [index-sca-mcp.md](index-sca-mcp.md) | phase 2 |
| Black Duck Air-gapped KnowledgeBase | latest | not initialized | — | optional |

## How to scrape

```powershell
python scripts/build-index.py --product detect-12.0.0 --init
python scripts/scrape-pending.py --product detect-12.0.0 --all-pending
python scripts/build-index.py --product detect-12.0.0
```

Registered product keys: `blackduck-2026.7`, `detect-11.5.1`, `detect-12.0.0`, `alert-8.4.0`, `bridge-latest`, `c-cpp-tool-latest`, `sca-mcp-latest`, `airgap-kb-latest`.

---

*Primary SCA detail index: [index.md → see also monoproduct builds](index.md).*

