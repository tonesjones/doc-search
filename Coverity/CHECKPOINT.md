# Session checkpoint — Coverity corpus

**Last updated:** 2026-08-12  
**Status:** **Full corpus complete** — Phases 0–8 done. **4443/4443** topics scraped, 0 pending, 0 skipped, 0 error.  
**Primary corpus:** Coverity Documentation **2026.6** (see `PHASE-PLAN.md`).  
**Map ID:** `Ul9eg_yUOJh8gKU4cs1xrg`  
**Product key:** `coverity-2026.6`

Read this file at the start of every new session on this project.

---

## How a new Grok session should resume

1. Workspace must be **`C:\TestCode\Product Docs\Coverity`** (not the Black Duck SCA folder).
2. Read this file → `PHASE-PLAN.md` → `corpus-status.md` / `index.md`.
3. Scrape work is finished. Only refresh if the user asks, or if official docs change.
4. After any scrape work: rebuild index + hub; update **this** checkpoint.

Chat history from the Black Duck SCA session does **not** transfer. **These files are the memory.**

---

## Phase status

| Phase | Description | Status |
|-------|-------------|--------|
| 0 | Scaffold + TOC/manifest init + smoke (3 topics) | **DONE** |
| 1 | Foundations (overview + small sections) | **DONE** (79 topics) |
| 2 | Coverity Connect (~526) | **DONE** (526 topics) |
| 3 | Analysis core, exclude Customization (~1,019) | **DONE** (1,019 topics) |
| 4 | Clients / CLI / Desktop (~366) | **DONE** (366 topics) |
| 5 | Connect APIs (~486) | **DONE** (486 topics) |
| 6 | Cloud Native (~520) | **DONE** (520 topics) |
| 7 | Customization / CodeXM / Extend SDK (~1,294) | **DONE** (1,294 topics) |
| 8 | Release notes + remaining cleanup | **DONE** (153 release notes earlier; remainder finished in one pass) |

**2026-08-12 one-pass remainder:** `--all-pending` scraped the last **1814** topics (Phase 7 Customization 1294 + Phase 6 Cloud Native 520) in ~21 minutes. Result: 1814 updated, 0 unchanged, 0 error. Hub rebuilt. `validate-corpus.py` passed (4443 done topics; 0 hashes backfilled).

---

## Tooling in place

- `scripts/products.py` — `coverity-2026.6` registry
- `scripts/build-index.py` — `--init`, `--refresh-toc`, `--hub`
- `scripts/scrape-pending.py` — `--section`, `--path-contains`, `--exclude-path`, `--all-pending`, `--retry-errors`
- Windows long-path safe writes; path length clamp for deep trees
- `scripts/validate-corpus.py` validates done-topic files, front matter, and content hashes.
- Atomic writes protect manifests, indexes, TOCs, and topic files; every scrape result is checkpointed.
- Empty official topic bodies become a child-topic index (or a leaf note). Re-run: `python scripts/scrape-pending.py --product coverity-2026.6 --repair-empty`

### Init / scrape commands

```powershell
cd "C:\TestCode\Product Docs\Coverity"
python scripts/build-index.py --list-products
python scripts/scrape-pending.py --product coverity-2026.6 --section "Coverity overview" --dry-run
python scripts/scrape-pending.py --product coverity-2026.6 --section "Coverity overview"
python scripts/build-index.py --product coverity-2026.6 --hub
python scripts/validate-corpus.py --product coverity-2026.6
```

For long sections, use `--limit 100` and repeat the command; each run resumes from the remaining pending topics.

To refresh a mutable documentation source, use `--refresh-changed --limit 100`; completed files are rewritten only when their normalized Markdown hash changed.

---

## Intentionally not in scope

| Item | Notes |
|------|-------|
| Coverity on Polaris | Separate maps; not registered |
| Non-English Coverity docs | ko / zh / ja maps exist; skip |
| Older versions (2026.3, etc.) | Pin is 2026.6 only |
| Black Duck SCA / Detect / Alert / Bridge | Separate project: `C:\TestCode\BlackDuck SCA` |

---

## Key files

| Path | Role |
|------|------|
| `README.md` | Shared-repo usage and how to scrape a new version |
| `CHECKPOINT.md` | This handoff |
| `AGENTS.md` | Standing rules |
| `PHASE-PLAN.md` | Full phase commands |
| `corpus-status.md` | Progress hub |
| `index.md` | Full TOC catalog |
| `sources/coverity-2026.6/manifest.json` | Work queue |
| `docs/**` | Markdown corpus |

---

## Next action

**Corpus is complete.** No pending scrape work.

If official 2026.6 docs change, refresh instead of re-scraping everything:

```powershell
cd "C:\TestCode\Product Docs\Coverity"
python scripts/build-index.py --product coverity-2026.6 --refresh-toc
python scripts/scrape-pending.py --product coverity-2026.6 --refresh-changed --limit 100
python scripts/scrape-pending.py --product coverity-2026.6 --all-pending
python scripts/scrape-pending.py --product coverity-2026.6 --retry-errors
python scripts/build-index.py --product coverity-2026.6 --hub
python scripts/validate-corpus.py --product coverity-2026.6
```
