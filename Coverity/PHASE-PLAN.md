# Coverity corpus — phased scrape plan

**Pinned product:** `coverity-2026.6`  
**Map ID:** `Ul9eg_yUOJh8gKU4cs1xrg`  
**Version:** 2026.6 (English)  
**Total topics:** ~4,443  
**Scope:** Full corpus eventually; execute in phases.  
**Out of scope:** Coverity on Polaris; non-English locales.

This file is the durable plan for any new session opened on this project.

---

## Phase 0 — Scaffold (tooling + TOC init)

- [x] Create project layout, scripts, AGENTS/CHECKPOINT/PHASE-PLAN
- [x] Register `coverity-2026.6` and init TOC/manifest (4,443 topics)
- [x] Smoke scrape: 3 overview topics → pipeline verified

**Status:** **DONE** (see CHECKPOINT).

---

## Phase 1 — Foundations (~75 topics)

**Goal:** Concepts + small top-level pages.

| Section / path | ~Topics |
|----------------|--------:|
| Coverity overview | 70 |
| Acknowledgements | 1 |
| Coverity glossary | 1 |
| Legal notice | 1 |
| Black Duck statement on inclusivity and diversity | 1 |
| All checkers | 1 |
| SpotBugs™ Checker Reference | 4 |

```powershell
python scripts/scrape-pending.py --product coverity-2026.6 --section "Coverity overview"
python scripts/scrape-pending.py --product coverity-2026.6 --section "Acknowledgements"
python scripts/scrape-pending.py --product coverity-2026.6 --section "Coverity glossary"
python scripts/scrape-pending.py --product coverity-2026.6 --section "Legal notice"
python scripts/scrape-pending.py --product coverity-2026.6 --section "Black Duck statement on inclusivity and diversity"
python scripts/scrape-pending.py --product coverity-2026.6 --section "All checkers"
python scripts/scrape-pending.py --product coverity-2026.6 --section "SpotBugs™ Checker Reference"
python scripts/build-index.py --product coverity-2026.6 --hub
```

---

## Phase 2 — Coverity Connect (~526)

```powershell
python scripts/scrape-pending.py --product coverity-2026.6 --section "Coverity Connect"
python scripts/build-index.py --product coverity-2026.6 --hub
```

Includes user guide, administration, installation and upgrade.

---

## Phase 3 — Analysis core without customization (~1,019)

**Section:** Coverity Analysis **excluding** Customization guides (~1,294 deferred to Phase 7).

```powershell
python scripts/scrape-pending.py --product coverity-2026.6 --section "Coverity Analysis" --exclude-path "Customization guides"
python scripts/build-index.py --product coverity-2026.6 --hub
```

Includes: Analysis overview, install/upgrade, analysis commands, reports, compliance, safety, Fortran, security directives.

---

## Phase 4 — Clients, plugins, CLI, Desktop (~366)

```powershell
python scripts/scrape-pending.py --product coverity-2026.6 --section "Clients, plug-ins, integrations, and APIs"
python scripts/build-index.py --product coverity-2026.6 --hub
```

---

## Phase 5 — Coverity Connect APIs (~486)

```powershell
python scripts/scrape-pending.py --product coverity-2026.6 --section "Coverity Connect APIs"
python scripts/build-index.py --product coverity-2026.6 --hub
```

SOAP + REST API reference material; large; fine overnight.

---

## Phase 6 — Cloud Native deployment (~520)

**Status:** **DONE** (520 topics, 2026-08-12 remainder pass).

```powershell
python scripts/scrape-pending.py --product coverity-2026.6 --section "Cloud Native Coverity deployment"
python scripts/build-index.py --product coverity-2026.6 --hub
```

---

## Phase 7 — Customization / checker authoring (~1,294)

```powershell
python scripts/scrape-pending.py --product coverity-2026.6 --path-contains "Customization guides"
python scripts/build-index.py --product coverity-2026.6 --hub
```

| Subtree | ~Topics |
|---------|--------:|
| Customizing Coverity | 125 |
| CodeXM Checkers Development Guide | 1,003 |
| Coverity Extend SDK Checker Development Guide | 165 |

**Status:** **DONE** (1,294 topics, 2026-08-12 remainder pass).

---

## Phase 8 — Release notes & cleanup (~153+)

```powershell
python scripts/scrape-pending.py --product coverity-2026.6 --section "Coverity release notes and upgrade considerations"
python scripts/scrape-pending.py --product coverity-2026.6 --all-pending
python scripts/scrape-pending.py --product coverity-2026.6 --retry-errors
python scripts/build-index.py --product coverity-2026.6 --hub
```

**Status:** **DONE** — release notes (153) scraped earlier; `--all-pending` remainder pass finished 2026-08-12 with **4443/4443 done**, 0 pending, 0 error. CHECKPOINT marked full-corpus complete.

---

## Timing (approx.)

| Chunk | Wall time (0.35s delay) |
|-------|-------------------------|
| ~500 topics | 15–25 min |
| Full ~4,443 | 2–3 hours total |

---

## Resume checklist (new Grok session)

1. Open workspace `C:\TestCode\Product Docs\Coverity`
2. Read `CHECKPOINT.md`
3. Check `corpus-status.md` / manifest stats
4. Corpus scrape is complete (4443/4443). Only refresh if official docs change or the user asks.
5. Update `CHECKPOINT.md` after any refresh or scrape.
