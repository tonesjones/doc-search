# Signal corpus — phased scrape plan

**Pinned product:** `signal-latest`  
**Map ID:** `xmDr3Yryk7OYDGb__OGKlg`  
**Version:** latest (English; last official publication 2026-07-23)  
**Total topics:** **17**  
**Scope:** Full corpus. Signal is a small book, so phases stay short.  
**Out of scope:** non-English locales; sibling Black Duck products.

This file is the durable plan for any new session opened on this project.

---

## Phase 0 — Scaffold (tooling + TOC init)

- [x] Create project layout, scripts, AGENTS/CHECKPOINT/PHASE-PLAN
- [x] Register `signal-latest` and verify map `xmDr3Yryk7OYDGb__OGKlg`
- [x] Init TOC/manifest (17 topics)
- [x] Smoke scrape + full scrape in one pass

**Status:** **DONE** (see CHECKPOINT).

---

## Phase 1 — Overview and reference (~3 topics)

**Goal:** Product overview, reference guide, AI/trust page.

| Section / path | ~Topics |
|----------------|--------:|
| Overview of Black Duck Signal | 1 |
| Reference guide | 1 |
| AI security, data protection, and trust | 1 |

```powershell
python scripts/scrape-pending.py --product signal-latest --section "Overview of Black Duck Signal"
python scripts/scrape-pending.py --product signal-latest --section "Reference guide"
python scripts/scrape-pending.py --product signal-latest --section "AI security, data protection, and trust"
python scripts/build-index.py --product signal-latest --hub
```

---

## Phase 2 — Incremental scans (~10 topics)

**Section:** Scan your code changes (coding assistants, IDE / Code Sight, CLI diff and file scans).

```powershell
python scripts/scrape-pending.py --product signal-latest --section "Scan your code changes"
python scripts/build-index.py --product signal-latest --hub
```

---

## Phase 3 — Full-project CLI (~3 topics)

**Section:** Scan a full project from the CLI (SARIF-only and send to Polaris).

```powershell
python scripts/scrape-pending.py --product signal-latest --section "Scan a full project from the CLI"
python scripts/build-index.py --product signal-latest --hub
```

---

## Phase 4 — Release notes and cleanup (~1+)

```powershell
python scripts/scrape-pending.py --product signal-latest --section "Signal release notes"
python scripts/scrape-pending.py --product signal-latest --all-pending
python scripts/scrape-pending.py --product signal-latest --retry-errors
python scripts/build-index.py --product signal-latest --hub
python scripts/validate-corpus.py --product signal-latest
python scripts/smoke-retrieval.py
```

**Status:** **DONE** — full `--all-pending` pass finished 2026-08-12 with **17/17 done**, 0 pending, 0 error.

---

## Timing (approx.)

| Chunk | Wall time (0.35s delay) |
|-------|-------------------------|
| Full 17 topics | under 1 minute |

Because the book is this small, a new session can re-run `--all-pending` or `--refresh-changed` in one shot instead of walking the phases.

---

## Resume checklist (new Grok session)

1. Open workspace `C:\TestCode\Product Docs\Signal`
2. Read `CHECKPOINT.md`
3. Check `corpus-status.md` / manifest stats
4. Corpus scrape is complete (17/17). Only refresh if official docs change or the user asks.
5. Update `CHECKPOINT.md` after any refresh or scrape.
