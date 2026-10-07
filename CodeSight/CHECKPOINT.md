# Session checkpoint — Code Sight corpus

**Last updated:** 2026-10-06
**Status:** **Full corpus complete** — Phases 0–4 done. **233/233** topics scraped, 0 pending, 0 skipped, 0 error.
**Primary corpus:** Black Duck Code Sight **2026.9.0** (see `PHASE-PLAN.md`).
**Map ID:** `MbKAMeBG9Dkor~tl3lqBXg`
**Product key:** `codesight-2026.9.0`

Read this file at the start of every new session on this project.

---

## How a new session should resume

1. Workspace must be the `CodeSight` folder (not SCA / Coverity / Polaris / Signal).
2. Read this file → `PHASE-PLAN.md` → `corpus-status.md` / `index.md`.
3. Scrape work is finished. Only refresh if the user asks, or if official docs change.
4. After any scrape work: rebuild index + hub; update **this** checkpoint.

Chat history from sibling product-doc sessions does **not** transfer. **These files are the memory.**

---

## Phase status

| Phase | Description | Status |
|-------|-------------|--------|
| 0 | Scaffold + TOC/manifest init | **DONE** (233 topics) |
| 1 | Overview, support matrix, install | **DONE** |
| 2 | Auth and issue viewing | **DONE** |
| 3 | Product integrations (Coverity, SCA, Polaris, SRM, Standard) | **DONE** |
| 4 | Preferences, release notes, general | **DONE** |

**2026-10-06 one-pass scrape:** `--all-pending` wrote all **233** topics via the cached scrape path (`scripts/cached-corpus-scrape.py`). Hub rebuilt. `validate-corpus.py` passed. `smoke-retrieval.py` passed.

---

## Tooling in place

- `scripts/products.py` — `codesight-2026.9.0` registry (map `MbKAMeBG9Dkor~tl3lqBXg`)
- `scripts/build-index.py` — TOC init + index/hub generation (`--init`, `--refresh-toc`, `--hub`)
- `scripts/scrape-pending.py` — topic body scraping (`--all-pending`, `--retry-errors`, `--refresh-changed`, `--dry-run`)
- `scripts/validate-corpus.py` — file/metadata/hash validation
- `scripts/smoke-retrieval.py` — retrieval spot checks
- `scripts/build-index.ps1` — Windows wrapper for the index script
- `../../scripts/cached-corpus-scrape.py` — cache-first bulk scrape driver

---

## Previous checkpoint history

(none — initial corpus build 2026-10-06)
