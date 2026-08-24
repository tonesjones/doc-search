# Session checkpoint

**Last updated:** 2026-08-24 (human-calibration milestone implemented and production-tested)
**Status:** **CALIBRATION MILESTONE COMPLETE on `codex/sca-verified-learning`** — resolve the product-expert/benchmark queue and define merge thresholds; do not merge yet.
**Primary corpus:** Black Duck Documentation **2026.7** — **941/941 done**  
**Companions:** Detect **206/206** · Alert **45/45** · Bridge **174/174** · C/CPP Tool **14/14** (6 Tools siblings skipped)  
**Grand total in corpus:** **1,380** topics

Read this file at the start of every new session.

---

## Current SCA self-improvement checkpoint

The corpus scrape remains complete. Current work is the SCA-only evaluation, feedback, regression, and runtime-validation workflow on branch `codex/sca-verified-learning`.

### Completed in the 2026-08-23 session

- Preserved and measured a 30-case SCA production-path baseline: 12 pass and 18 machine fail.
- Added answer traces, deterministic scoring, failure taxonomy, feedback intake, and a permanent regression suite outside the baseline.
- Proved the human-feedback loop with the C/C++ standard-scan correction: optional snippet matching is no longer silently added, and the production regression passes.
- Added a read-only-first SCA runtime validator and ownership-isolated `Tony RAG` project on `sca.field-test.blackduck.com`.
- Confirmed the runtime is SCA 2026.4.0 while the corpus is 2026.7; runtime results remain `INCONCLUSIVE / VERSION_MISMATCH`.
- Recorded that the five empty `RAG-VAL-*` versions were unnecessary infrastructure placeholders, not scan tests.
- Enforced the shared-instance operational limit of 10 Active versions in `Tony RAG`. Provisioning stops before exceeding the limit; deletion and one-way LTS conversion always require an explicit human decision.
- Automated test status: 23 passing.
- Shared-version safety guard commit: `6ae66bc` (`Guard shared SCA active version capacity`).

### Completed on 2026-08-24

- Generated `evaluation/reviews/sca-baseline-human-review.md` from all 30 preserved cases, machine results, and production traces.
- Added a customer-view-first review flow, collapsed evidence/machine details, a navigable queue, and explicit human verdict categories.
- Added `evaluation/reviews/sca-baseline-adjudications.jsonl` as the machine-readable source of human decisions; all 30 records start `UNREVIEWED`.
- Added an adjudication schema and a reusable generator that preserves existing human decisions when refreshed.
- Verified 30/30 cases, traces, queue entries, packet anchors, and adjudication records are present; no runtime credential was included.
- Completed human adjudication of all 30 cases. Verdicts: 15 `TRUE_PASS`, 6 `SCORING_FALSE_NEGATIVE`, 3 `TRUE_FAILURE`, 3 `NEEDS_PRODUCT_EXPERT`, 2 `BENCHMARK_NEEDS_REVISION`, and 1 `FALSE_PASS`.
- Captured customer-guidance corrections for lifecycle phase and distribution selection, the current Access Tokens UI path, project terminology, version-specific Archived behavior, and the default 10-version Product Registration safeguard.
- Preserved documentation/product conflicts and uncertain observations as unpromoted candidates rather than silently changing the corpus.
- Added approval-gated runtime candidates for user-inactivation token invalidation and cloned-version BOM-edit retention. No shared-instance mutation was executed.
- Recorded the 2026.4 runtime versus 2026.7 corpus mismatch and the need to rerun version-sensitive cases as the test environment is upgraded.
- Added a separate human-verified scoring-equivalence layer without modifying the preserved baseline. All six adjudicated `SCORING_FALSE_NEGATIVE` cases now score correctly on their captured production answers.
- Added inline-Markdown normalization and a constrained required-source citation fallback; Recall@K remains based only on observed retrieval.
- Added a deterministic production version guard. An explicit request for an SCA server version other than the pinned 2026.7 corpus now abstains before generation; the 2026.4 caveat case passes with 100% abstention accuracy.
- Promoted four generalized customer-answer regressions for project definitions, lifecycle phase selection, distribution selection, and the current API-token UI path. Together with the existing C/C++ scope regression, the production-trace regression suite is 5/5 passing.
- Human-calibrated saved baseline: 20/30 pass, up from 12/30. The ten remaining failures remain visible and are not overridden by the human review.
- Automated test status: 33 passing.

### Next milestone

Resolve the remaining product-expert and benchmark questions with version-matched evidence, then define quantitative merge thresholds for SCA.

### Work next, in order

1. **Complete:** Generate and human-review the 30-case SCA packet; preserve all verdicts in `evaluation/reviews/sca-baseline-adjudications.jsonl`.
2. **Complete:** Fix the six adjudicated evaluator false negatives while retaining literal checks by default.
3. **Complete:** Promote generalized customer-answer regressions for the three true failures and one false pass.
4. **Complete:** Add and production-test the version-compatibility/abstention guard.
5. **Next:** Resolve the three product-expert cases and two benchmark-revision cases with version-matched documentation or approved runtime evidence.
6. Review the remaining human-correct/machine-fail cases for additional tightly scoped scoring equivalents or fresh production traces; do not blanket-override them.
7. Productize feedback capture and approval so an `answer_id` plus critique creates an untrusted candidate, not an automatic truth or code change.
8. Automate promotion gates and rerun the exact questions, all verified regressions, the preserved baseline, and safety tests.
9. Improve evidence ranking using the human-adjudicated failure set; current saved-trace Recall@1/3/5 remains 3.3%/20.0%/43.3%.
10. Define merge thresholds, then merge only when the reviewed SCA baseline, version control, regressions, and safety gates meet them.

**Immediate next action:** work the product-expert/benchmark verification queue, starting with the 10GB Managed Code claim, Internal-distribution risk calculation, Archived-upgrade behavior, and the approval-gated clone/BOM-retention test. Keep all shared-instance mutations isolated to `Tony RAG` and require explicit approval.

Other product lines remain out of scope for this iteration. Replicate the workflow product-by-product only after it is stable for SCA.

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
| Black Duck C/CPP Tool | `c-cpp-tool-latest` | latest | **14/20** (6 skipped) | `docs/c-cpp-tool/` | `index-c-cpp-tool.md` |

**Hub:** `corpus-status.md`

### Sibling corpora (do not scrape into this SCA tree)

| Product | Path |
|---------|------|
| **Coverity** | `C:\TestCode\Product Docs\Coverity` |
| **Polaris** | `C:\TestCode\Product Docs\Polaris` |

Route Coverity / Polaris questions to those checkouts. Do not copy or scrape their maps here.

### Intentionally not scraped yet (deferred — not needed now)

| Product / map | Key / notes | ~Topics | Why deferred |
|---------------|-------------|--------:|--------------|
| **Air-gapped KnowledgeBase** | `airgap-kb-latest` · map `YsDtm_HKwGM6efkx~2HVvQ` · registered in `scripts/products.py` but never initialized | ~15 | Optional corner case (offline KB). User: not needed right now. |
| **BDBA** (Binary Analysis) | Not registered | — | Out of scope unless re-requested |
| **Black Duck Tools** (rest of map) | Same map as C/CPP (`2GUQEgoyKxsQAcOtWsqdDA`) | 6 skipped | KB Vulnerability Feed Server left unscraped; C/CPP chapter is in corpus |
| **SCASS MCP Server** | Other Tools map `3JcuocdfP6Yh0iupxpNOwQ` | — | Not the map the SCA portal link opens |
| **Artifactory** plugin docs | Not registered | — | Out of scope |
| **Code Sight** | Not registered | — | Out of scope |
| **Defensics / Seeker / Sigma / Signal / SRM** | Not registered | — | Out of scope |
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
- [x] C/CPP Tool chapter — scrape (14; 6 Tools siblings skipped)  
- [x] Rebuild indexes / hub  
- [x] Update `AGENTS.md` + this checkpoint  
- [x] **User decision:** no further scrape for now  
- [ ] Air-gapped KB — **deferred** (not needed now)  
- [ ] Other portal products — **out of scope** unless re-requested  

**Next action when you return:** answer product questions from the corpus. Do **not** start a scrape batch unless the user asks.
