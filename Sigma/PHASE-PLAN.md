# Sigma corpus — phased scrape plan

**Pinned product:** `sigma-2026.8.0`  
**Map ID:** `S_R7XSLfKPN3q6kGpp1eHQ`  
**Version:** 2026.8.0 (English; last official publication 2026-08-11)  
**Total topics:** **59**  
**Scope:** Full English Sigma User Guide.  
**Out of scope:** `latest` map; older versions (2026.7.0, 2026.6.1); non-English locales; sibling Black Duck products.

This file is the durable plan for any new session opened on this project.

The official TOC has a single wrapper root (**Sigma User Guide**). Second-level sections live under `docs/user-guide/`. Use `--path-contains` to scrape one of those sections; `--section` matches only the wrapper title.

---

## Phase 0 — Scaffold (tooling + TOC init)

- [x] Create project layout, scripts, AGENTS/CHECKPOINT/PHASE-PLAN
- [x] Register `sigma-2026.8.0` and verify map `S_R7XSLfKPN3q6kGpp1eHQ`
- [x] Init TOC/manifest (59 topics)
- [x] Smoke scrape + full scrape in one pass

**Status:** **DONE** (see CHECKPOINT).

---

## Phase 1 — Introducing and downloading (~4 topics)

**Goal:** Product intro plus binary / Docker install.

| Path contains | ~Topics |
|---------------|--------:|
| Introducing Sigma | 1 |
| Downloading Sigma | 3 |

```powershell
python scripts/scrape-pending.py --product sigma-2026.8.0 --path-contains "Introducing Sigma"
python scripts/scrape-pending.py --product sigma-2026.8.0 --path-contains "Downloading Sigma"
python scripts/build-index.py --product sigma-2026.8.0 --hub
```

---

## Phase 2 — Configuring Sigma (~13 topics)

**Path:** Configuring Sigma (AI checker plug-in, methods/precedence, options, output, `coverity.yml`, `.sigma-config.yml`, env vars, CI config).

```powershell
python scripts/scrape-pending.py --product sigma-2026.8.0 --path-contains "Configuring Sigma"
python scripts/build-index.py --product sigma-2026.8.0 --hub
```

---

## Phase 3 — CI/CD, Jenkins, policies (~24 topics)

**Path:** Running Sigma in CI/CD (Jenkins plugin, freestyle / pipeline, quality-gate policies).

```powershell
python scripts/scrape-pending.py --product sigma-2026.8.0 --path-contains "Running Sigma in CI/CD"
python scripts/build-index.py --product sigma-2026.8.0 --hub
```

---

## Phase 4 — CLI, support matrix, checkers, release notes (~18 topics)

```powershell
python scripts/scrape-pending.py --product sigma-2026.8.0 --path-contains "Command Reference"
python scripts/scrape-pending.py --product sigma-2026.8.0 --path-contains "Sigma Support Matrix"
python scripts/scrape-pending.py --product sigma-2026.8.0 --path-contains "Release Notes"
python scripts/scrape-pending.py --product sigma-2026.8.0 --path-contains "Sigma Checkers"
python scripts/scrape-pending.py --product sigma-2026.8.0 --all-pending
python scripts/scrape-pending.py --product sigma-2026.8.0 --retry-errors
python scripts/build-index.py --product sigma-2026.8.0 --hub
python scripts/validate-corpus.py --product sigma-2026.8.0
python scripts/smoke-retrieval.py
```

**Status:** **DONE** — full `--all-pending` pass finished 2026-08-12 with **59/59 done**, 0 pending, 0 error.

---

## Timing (approx.)

| Chunk | Wall time (0.35s delay) |
|-------|-------------------------|
| Full 59 topics | ~2–4 minutes |

Because the book is this small, a new session can re-run `--all-pending` or `--refresh-changed` in one shot instead of walking the phases.

---

## Resume checklist (new Grok session)

1. Open workspace `C:\TestCode\Product Docs\Sigma`
2. Read `CHECKPOINT.md`
3. Check `corpus-status.md` / manifest stats
4. Corpus scrape is complete (59/59). Only refresh if official docs change or the user asks.
5. Update `CHECKPOINT.md` after any refresh or scrape.
