# Session checkpoint — Sigma corpus

**Last updated:** 2026-08-12  
**Status:** **Full corpus complete** — Phases 0–4 done. **59/59** topics scraped, 0 pending, 0 skipped, 0 error.  
**Primary corpus:** Black Duck Sigma **2026.8.0** (see `PHASE-PLAN.md`).  
**Map ID:** `S_R7XSLfKPN3q6kGpp1eHQ`  
**Product key:** `sigma-2026.8.0`

Read this file at the start of every new session on this project.

---

## How a new Grok session should resume

1. Workspace must be **`C:\TestCode\Product Docs\Sigma`** (not SCA / Coverity / Polaris / Signal).
2. Read this file → `PHASE-PLAN.md` → `corpus-status.md` / `index.md`.
3. Scrape work is finished. Only refresh if the user asks, or if official docs change.
4. After any scrape work: rebuild index + hub; update **this** checkpoint.

Chat history from sibling product-doc sessions does **not** transfer. **These files are the memory.**

---

## Phase status

| Phase | Description | Status |
|-------|-------------|--------|
| 0 | Scaffold + TOC/manifest init | **DONE** (59 topics) |
| 1 | Introducing + Downloading | **DONE** |
| 2 | Configuring Sigma | **DONE** |
| 3 | CI/CD, Jenkins, policies | **DONE** |
| 4 | CLI, support matrix, checkers, release notes | **DONE** |

**2026-08-12 one-pass scrape:** `--all-pending` wrote all **59** topics. Result: 59 updated, 0 unchanged, 0 error. Hub rebuilt. `validate-corpus.py` and `smoke-retrieval.py` passed.

Official **Sigma Checkers** and standalone **Release Notes** pages in this map are pointer topics (they link to Fluid Topics origin IDs `sigma_checker_latest-en` and `sigma_release_notes`). Those origins are **not** separate book maps in `/api/khub/maps` and were not scraped.

---

## Tooling in place

- `scripts/products.py` — `sigma-2026.8.0` registry (map `S_R7XSLfKPN3q6kGpp1eHQ`)
- `scripts/build-index.py` — `--init`, `--refresh-toc`, `--hub`
- `scripts/scrape-pending.py` — `--section`, `--path-contains`, `--exclude-path`, `--all-pending`, `--retry-errors`
- Windows long-path safe writes; path length clamp for deep trees
- `scripts/validate-corpus.py` validates done-topic files, front matter, and content hashes
- `scripts/smoke-retrieval.py` checks intro, analyze CLI, env vars, languages, policies, AI plug-in, and the checker/release-note pointers
- Atomic writes protect manifests, indexes, TOCs, and topic files

### Init / scrape commands

```powershell
cd "C:\TestCode\Product Docs\Sigma"
python scripts/build-index.py --list-products
python scripts/scrape-pending.py --product sigma-2026.8.0 --path-contains "Introducing Sigma" --dry-run
python scripts/scrape-pending.py --product sigma-2026.8.0 --all-pending
python scripts/build-index.py --product sigma-2026.8.0 --hub
python scripts/validate-corpus.py --product sigma-2026.8.0
python scripts/smoke-retrieval.py
```

---

## Intentionally not in scope

| Item | Notes |
|------|-------|
| Sigma `latest` map | Mutable; pin 2026.8.0 instead (`vkb5zvSX~7E~X~04sUrrNQ`) |
| Older Sigma versions | 2026.7.0, 2026.6.1 not registered |
| Checker catalog / standalone RN | Origin IDs only; not book maps |
| Non-English Sigma docs | No other locale maps registered |
| Black Duck SCA / Detect / Alert / Bridge | Separate project: `C:\TestCode\Product Docs\BlackDuck SCA` |
| Coverity | Separate project: `C:\TestCode\Product Docs\Coverity` |
| Polaris | Separate project: `C:\TestCode\Product Docs\Polaris` |
| Signal | Separate project: `C:\TestCode\Product Docs\Signal` |

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
| `sources/sigma-2026.8.0/manifest.json` | Work queue |
| `docs/**` | Markdown corpus |

---

## Next action

**Corpus is complete.** No pending scrape work.

If official Sigma docs change, refresh instead of re-scraping everything:

```powershell
cd "C:\TestCode\Product Docs\Sigma"
python scripts/build-index.py --product sigma-2026.8.0 --refresh-toc
python scripts/scrape-pending.py --product sigma-2026.8.0 --refresh-changed
python scripts/scrape-pending.py --product sigma-2026.8.0 --all-pending
python scripts/scrape-pending.py --product sigma-2026.8.0 --retry-errors
python scripts/build-index.py --product sigma-2026.8.0 --hub
python scripts/validate-corpus.py --product sigma-2026.8.0
python scripts/smoke-retrieval.py
```
