# Code Sight corpus — phased scrape plan

**Pinned product:** `codesight-2026.9.0`
**Map ID:** `MbKAMeBG9Dkor~tl3lqBXg`
**Version:** 2026.9.0 (English)
**Total topics:** **233**
**Scope:** Full corpus.
**Out of scope:** non-English locales; sibling Black Duck products.

This file is the durable plan for any new session opened on this project.

---

## Phase 0 — Scaffold (tooling + TOC init)

- [x] Create project layout, scripts, AGENTS/CHECKPOINT/PHASE-PLAN
- [x] Register `codesight-2026.9.0` and verify map `MbKAMeBG9Dkor~tl3lqBXg`
- [x] Init TOC/manifest (233 topics)
- [x] Smoke scrape + full scrape in one pass

**Status:** **DONE** (see CHECKPOINT).

---

## Phase 1 — Overview, support matrix, install (~15 topics)

**Goal:** What Code Sight is, supported languages/IDEs/platforms, installation per IDE.

| Section | ~Topics |
|---------|--------:|
| Welcome to Code Sight | 2 |
| Code Sight Support Matrix | 5 |
| Installing Code Sight | ~8 |

```powershell
python scripts/scrape-pending.py --product codesight-2026.9.0 --section "Welcome to Code Sight"
python scripts/scrape-pending.py --product codesight-2026.9.0 --section "Code Sight Support Matrix"
python scripts/scrape-pending.py --product codesight-2026.9.0 --section "Installing Code Sight"
python scripts/build-index.py --product codesight-2026.9.0 --hub
```

---

## Phase 2 — Auth and issue viewing (~15 topics)

**Goal:** Server authentication, local vs team views.

| Section | ~Topics |
|---------|--------:|
| Authenticating to Servers in Code Sight | 6 |
| Viewing Issues in Code Sight | ~5 |
| Signal and Code Sight VS Code Extension | 1 |

---

## Phase 3 — Product integrations (~45 topics)

**Goal:** Code Sight workflows per connected product.

| Section | ~Topics |
|---------|--------:|
| Coverity with Code Sight | ~12 |
| Black Duck SCA with Code Sight | ~10 |
| Polaris with Code Sight | ~12 |
| Software Risk Manager with Code Sight | ~5 |
| Code Sight Standard Edition | ~6 |

---

## Phase 4 — Preferences, release notes, general (~150 topics)

**Goal:** Preference panels, release notes archive, general info.

| Section | ~Topics |
|---------|--------:|
| Code Sight: Preferences and Troubleshooting | ~13 |
| Code Sight Release Notes and Known Issues | ~76 (release notes archive) |
| General Information | 4 |

---

All phases ran as a single `--all-pending` pass on 2026-10-06. See CHECKPOINT for results.
