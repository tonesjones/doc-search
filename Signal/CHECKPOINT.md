# Session checkpoint — Signal corpus

**Last updated:** 2026-08-12  
**Status:** **Full corpus complete** — Phases 0–4 done. **17/17** topics scraped, 0 pending, 0 skipped, 0 error.  
**Primary corpus:** Black Duck Signal **latest** (see `PHASE-PLAN.md`).  
**Map ID:** `xmDr3Yryk7OYDGb__OGKlg`  
**Product key:** `signal-latest`

Read this file at the start of every new session on this project.

---

## How a new Grok session should resume

1. Workspace must be **`C:\TestCode\Product Docs\Signal`** (not SCA / Coverity / Polaris).
2. Read this file → `PHASE-PLAN.md` → `corpus-status.md` / `index.md`.
3. Scrape work is finished. Only refresh if the user asks, or if official docs change.
4. After any scrape work: rebuild index + hub; update **this** checkpoint.

Chat history from sibling product-doc sessions does **not** transfer. **These files are the memory.**

---

## Phase status

| Phase | Description | Status |
|-------|-------------|--------|
| 0 | Scaffold + TOC/manifest init | **DONE** (17 topics) |
| 1 | Overview + reference + AI/trust | **DONE** |
| 2 | Incremental scans (assistants, IDE, CLI) | **DONE** |
| 3 | Full-project CLI (SARIF / Polaris) | **DONE** |
| 4 | Release notes + cleanup | **DONE** |

**2026-08-12 one-pass scrape:** `--all-pending` wrote all **17** topics. Result: 17 updated, 0 unchanged, 0 error. Hub rebuilt. `validate-corpus.py` passed (17 done topics; 0 hashes backfilled).

---

## Tooling in place

- `scripts/products.py` — `signal-latest` registry (map `xmDr3Yryk7OYDGb__OGKlg`)
- `scripts/build-index.py` — `--init`, `--refresh-toc`, `--hub`
- `scripts/scrape-pending.py` — `--section`, `--path-contains`, `--exclude-path`, `--all-pending`, `--retry-errors`
- Windows long-path safe writes; path length clamp for deep trees
- `scripts/validate-corpus.py` validates done-topic files, front matter, and content hashes
- `scripts/smoke-retrieval.py` checks overview, Claude MCP, CLI, Polaris upload, and reference pages
- Atomic writes protect manifests, indexes, TOCs, and topic files

### Init / scrape commands

```powershell
cd "C:\TestCode\Product Docs\Signal"
python scripts/build-index.py --list-products
python scripts/scrape-pending.py --product signal-latest --section "Overview of Black Duck Signal" --dry-run
python scripts/scrape-pending.py --product signal-latest --all-pending
python scripts/build-index.py --product signal-latest --hub
python scripts/validate-corpus.py --product signal-latest
python scripts/smoke-retrieval.py
```

---

## Intentionally not in scope

| Item | Notes |
|------|-------|
| Non-English Signal docs | No other locale maps registered |
| Black Duck SCA / Detect / Alert / Bridge | Separate project: `C:\TestCode\Product Docs\BlackDuck SCA` |
| Coverity | Separate project: `C:\TestCode\Product Docs\Coverity` |
| Polaris | Separate project: `C:\TestCode\Product Docs\Polaris` |

---

## Key files

| Path | Role |
|------|------|
| `README.md` | Shared-repo usage and how to refresh |
| `CHECKPOINT.md` | This handoff |
| `AGENTS.md` | Standing rules |
| `PHASE-PLAN.md` | Full phase commands |
| `corpus-status.md` | Progress hub |
| `index.md` | Full TOC catalog |
| `sources/signal-latest/manifest.json` | Work queue |
| `docs/**` | Markdown corpus |

---

## Next action

**Corpus is complete.** No pending scrape work.

If official Signal docs change, refresh instead of re-scraping everything:

```powershell
cd "C:\TestCode\Product Docs\Signal"
python scripts/build-index.py --product signal-latest --refresh-toc
python scripts/scrape-pending.py --product signal-latest --refresh-changed
python scripts/scrape-pending.py --product signal-latest --all-pending
python scripts/scrape-pending.py --product signal-latest --retry-errors
python scripts/build-index.py --product signal-latest --hub
python scripts/validate-corpus.py --product signal-latest
python scripts/smoke-retrieval.py
```
