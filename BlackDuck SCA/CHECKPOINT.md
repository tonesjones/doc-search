# Session checkpoint

**Last updated:** 2026-09-08 (Black Duck Tools / KnowledgeBase Vulnerability Feed Server branch completed)
**Status:** **DONE for now** — use local corpus for Q&A; no additional scrape is pending in the current scope.
**Primary corpus:** Black Duck Documentation **2026.7** — **941/941 done**  
**Companions:** Detect 11.5.1 **206/206** · Detect 12.0.0 **207/207** · Alert **45/45** · Bridge **174/174** · C/CPP Tool **20/20**
**Grand total in corpus:** **1,595** topics

## Black Duck SCA MCP Server source — 2026-09-08

- Added the official GitHub documentation snapshot under `docs/sca-mcp/` with its own manifest and index.
- Source is `blackducksoftware/sca-mcp` commit `6dac85b23b14899dc6c463a1021171356f381570`; it is a GitHub source, not a Fluid Topics map.
- The snapshot contains the maintained README and security policy. Refresh it from the upstream repository, not with the Fluid Topics scraper.

## Software Risk Manager corpus boundary correction — 2026-09-08

- SRM was moved to the standalone sibling corpus at `C:\TestCode\Product Docs\SRM`.
- Its 286-topic snapshot, source metadata, index, and scraper tooling are no longer part of the Black Duck SCA corpus.

Read this file at the start of every new session.

## Black Duck Tools / KnowledgeBase Vulnerability Feed Server update — 2026-09-08

- Reopened the six previously skipped topics in the `c-cpp-tool-latest` map (`2GUQEgoyKxsQAcOtWsqdDA`), including the two parent topics: Black Duck Tools; KnowledgeBase Vulnerability Feed Server; Common Security Advisory Framework (CSAF); Usage Guide; Authentication; and Rate Limiting.
- Scraped all six through the documented Fluid Topics TOC/content APIs with **0 errors**. The C/CPP Tool manifest is now **20/20 done**, with **0 pending**, **0 skipped**, and **0 errors**.
- Rebuilt `index-c-cpp-tool.md` and `corpus-status.md`. No commit or push was performed.
- KnowledgeBase Vulnerability Feed Server topics are stored separately under `docs/knowledgebase-vulnerability-feed-server/`, not under `docs/c-cpp-tool/`.

---

## Added on 2026-09-03: SCA 2026.4.0 OpenAPI snapshot

- Preserved the server-generated public specification at `sources/openapi/2026.4.0/openapi3-public.json`.
- Added `docs/api/openapi-snapshot-2026-4-0.md` with provenance, retrieval guidance, checksum, and known specification limitations.
- Updated the SCA corpus routing instructions to consult versioned OpenAPI snapshots for exact endpoint contracts while keeping narrative documentation primary for product guidance.
- The snapshot version is 2026.4.0; do not silently treat it as the pinned 2026.7 documentation contract.

---

## Scrape status — complete for current scope

User confirmed (2026-08-08): no additional scraping needed right now.  
**2026-08-13:** user reopened scope for the C/CPP Tool portal chapter only.  
Missing maps below are **intentionally deferred**, not incomplete work.

### In corpus (use these for RAG)

| Product | Key | Version | Progress | Docs | Index |
|---------|-----|---------|----------|------|-------|
| Black Duck SCA (server/UI) | `blackduck-2026.7` | 2026.7 | **941/941** | `docs/help-center/`, install, API, architecture, release-notes, … | `index.md` |
| Black Duck Detect | `detect-11.5.1` | 11.5.1 | **206/206** | `docs/detect/` | `index-detect.md` |
| Black Duck Alert | `alert-8.4.0` | 8.4.0 | **45/45** | `docs/alert/` | `index-alert.md` |
| Bridge CLI | `bridge-latest` | latest | **174/174** | `docs/bridge/` | `index-bridge.md` |
| Black Duck C/CPP Tool | `c-cpp-tool-latest` | latest | **20/20** | `docs/c-cpp-tool/` | `index-c-cpp-tool.md` |

**Hub:** `corpus-status.md`

### Sibling corpora (do not scrape into this SCA tree)

| Product | Path |
|---------|------|
| **Coverity** | `C:\TestCode\Product Docs\Coverity` |
| **Polaris** | `C:\TestCode\Product Docs\Polaris` |
| **Software Risk Manager** | `C:\TestCode\Product Docs\SRM` |

Route Coverity / Polaris questions to those checkouts. Do not copy or scrape their maps here.

### Intentionally not scraped yet (deferred — not needed now)

| Product / map | Key / notes | ~Topics | Why deferred |
|---------------|-------------|--------:|--------------|
| **Air-gapped KnowledgeBase** | `airgap-kb-latest` · map `YsDtm_HKwGM6efkx~2HVvQ` · registered in `scripts/products.py` but never initialized | ~15 | Optional corner case (offline KB). User: not needed right now. |
| **BDBA** (Binary Analysis) | Not registered | — | Out of scope unless re-requested |
| **SCASS MCP Server** | Other Tools map `3JcuocdfP6Yh0iupxpNOwQ` | — | Not the map the SCA portal link opens |
| **Artifactory** plugin docs | Not registered | — | Out of scope |
| **Code Sight** | Not registered | — | Out of scope |
| **Defensics / Seeker / Sigma / Signal** | Not registered | — | Out of scope |
| **Portal** / multi-product portal maps | Not registered | — | Out of scope |
| **Older SCA year versions** / non-English locales | Not registered | — | Out of scope |

If any of the above is needed later: add/init the map (or use existing `airgap-kb-latest` key), scrape, rebuild hub, update this file.

### Tooling already in place

- `scripts/products.py` — product/map registry (includes deferred `airgap-kb-latest`)
- `scripts/build-index.py` — `--product <key>|all`, `--init`, `--refresh-toc`, `--hub`
- `scripts/scrape-pending.py` — `--product <key>`; Windows long-path safe writes
- Path length clamp for deep Bridge trees (Windows MAX_PATH)

---

## How to use the corpus today

1. Prefer local `docs/**` + product indexes for **SCA, Detect, Alert, Bridge, C/CPP Tool** questions.  
2. For **Coverity** / **Polaris**: use the sibling checkouts (`C:\TestCode\Product Docs\Coverity`, `C:\TestCode\Product Docs\Polaris`). Do not scrape them here.  
3. For other deferred products: say they are **not in the local corpus**; use official Fluid Topics APIs only if the user asks, or offer to scrape.  
4. Never scrape SPA HTML shells; always Fluid Topics TOC/content APIs.

### Maintenance (only if refreshing existing maps)

```powershell
python scripts/build-index.py --list-products
python scripts/build-index.py --product detect-11.5.1
python scripts/scrape-pending.py --product bridge-latest --retry-errors
```

### If user later wants air-gap only

```powershell
python scripts/build-index.py --product airgap-kb-latest --init
python scripts/scrape-pending.py --product airgap-kb-latest --all-pending
python scripts/build-index.py --product airgap-kb-latest --hub
```

---

## Key files

| Path | Role |
|------|------|
| `CHECKPOINT.md` | This handoff |
| `AGENTS.md` | Standing rules |
| `corpus-status.md` | Multi-product progress hub |
| `index.md` | SCA 2026.7 full TOC |
| `index-detect.md` / `index-alert.md` / `index-bridge.md` / `index-c-cpp-tool.md` | Companion TOCs |
| `sources/<product-key>/manifest.json` | Per-map work queues |
| `scripts/products.py` | Map registry |
| `scripts/scrape-pending.py` | Scraper |
| `scripts/build-index.py` | Index / TOC init |
| `docs/**` | Markdown corpus |

---

## Checklist

- [x] Multi-map tooling  
- [x] Detect 11.5.1 — scrape (206)  
- [x] Alert 8.4.0 — scrape (45)  
- [x] Bridge CLI latest — scrape (174)  
- [x] C/CPP Tool and KnowledgeBase Vulnerability Feed Server — scrape (20)
- [x] Rebuild indexes / hub  
- [x] Update `AGENTS.md` + this checkpoint  
- [x] **User decision:** no further scrape for now  
- [ ] Air-gapped KB — **deferred** (not needed now)  
- [ ] Other portal products — **out of scope** unless re-requested  

**Next action when you return:** answer product questions from the corpus. Do **not** start a scrape batch unless the user asks.
