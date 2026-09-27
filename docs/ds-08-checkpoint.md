# DS-08 project handoff

Updated 2026-09-27. Workspace: `C:\TestCode\Product Docs`. Branch: `codex/ds-08-promotion` at `e791f6c`. This is a local checkpoint, not a claim that the branch is pushed or merged.

## Goal and current state

The repository is a local, versioned Black Duck documentation corpus and product router. Its supported path starts at the root `SKILL.md`, selects a product through `products.json`, and answers from that product's documented sources. DS-07 added a checkout-bound answer evaluator. DS-08 closes the feedback loop: turn one customer question into a candidate, have a person review it, capture a fresh answer replay, and promote the case into the regression bank only after all gates pass.

The current DS-08 question asks how to run a Detect snippet scan and find the results in the Black Duck UI. Its candidate and reviewed case exist, but the case is **not promoted**. The latest GPT-6 Luna replay is measured and failed. No promotion preview or `--apply` has run for this candidate.

## Completed work

- DS-01 through DS-03 established the merged root-router workflow. DS-04 reconciled that workflow with the older personal `bd` experiment and selected the merged checkout as the maintained source. DS-05 repaired integrity checks. DS-06 preserved the SCA RBAC exercise as a sanitized, machine-checked case. The [supported workflow](supported-workflow.md) and [DS-06 case guide](ds-06-rbac-case.md) describe their boundaries.
- DS-07 established 30 baseline cases, six reviewed feedback regressions, and a four-case routine smoke set. The [evaluator guide](ds-07-evaluator.md) distinguishes deterministic corpus checks from measured answers. The older 36-case bank is a reference set, not a required routine model run.
- DS-08 added a dry-run-first promotion command with candidate, reviewed-case, fresh-replay, provenance, and duplicate-ID gates. See the [promotion guide](ds-08-promotion.md) and commit `00199a1`.
- The DS-08 adapter now accepts pinned Detect 12.0.0 evidence alongside SCA 2026.7 evidence (`49b4da8`), selects a current Codex executable through `DOC_SEARCH_CODEX_BIN` (`145dcbf`), records timeouts as `NOT_MEASURED` and saves redacted invalid answers locally (`93d0abf`), and gives general cross-platform first-scan guidance (`e791f6c`).
- All 70 local unit tests passed after those changes. The latest replay used GPT-6 Luna and recorded the model, prompt, source, and clean tracked checkout revisions. It returned valid source excerpts, but its case score is FAIL.

## Why DS-08 is stuck

The latest answer gives Windows PowerShell and Linux Bash commands, a token environment variable, server and project inputs, snippet matching, and a UI route. It is more useful than the earlier unmeasured attempts. The scorer still reports `ABSTENTION_FAILURE`, `RETRIEVAL_FAILURE`, and `SYNTHESIS_FAILURE`:

- The answer adds an unnecessary caveat that the checkout does not establish a Detect client version named 2026.7. SCA server 2026.7 and the pinned Detect 12.0.0 documentation are different version axes. The caveat triggers the abstention detector even though the answer continues with instructions.
- The case requires the exact Source-tab page. The answer cites a different 2026.7 page that describes the same UI route as "Source view" and does not say the exact words "Source tab".
- The case requires the literal `SIGNATURE_SCAN`. The answer relies on Detect's documented default tool selection and enables `SNIPPET_MATCHING`, but does not spell out `SIGNATURE_SCAN`.

These are partly scoring-policy questions, not evidence that the snippet guidance is unusable. Do not edit the model prompt again merely to make it repeat case literals. First decide which requirements protect customer value. The answer also pinned Detect 12.0.0 while the approved draft uses the generic latest-download scripts; review that difference before accepting the answer. No live Detect scan was run for this DS-08 question. Documentation evidence and live behavior remain separate.

Earlier attempts failed before scoring. The old CLI on PATH rejected GPT-6; the current app-managed CLI accepted Luna and Sol. A Luna answer had copied excerpts that did not match its files. One Sol attempt exceeded the old 120-second evaluator limit. The current adapter saves redacted invalid answers under ignored `.local/evaluation-failures/` and times out its nested model run before the evaluator's 120-second limit. Do not count those earlier attempts as measured passes.

## Review files in this order

1. [Supported workflow](supported-workflow.md) and [promotion guide](ds-08-promotion.md).
2. Candidate: `evaluation/candidates/feedback-detect-snippet-ui-001.json`.
3. Human-approved draft and run notes: `evaluation/reviews/feedback-detect-snippet-ui-001.md`.
4. Reviewed case: `evaluation/reviews/feedback-detect-snippet-ui-001.json` and its `.jsonl` copy.
5. Latest local replay: `evaluation/results/ds-08-snippet-replay.json` and `evaluation/traces/ds-08-snippet/feedback-detect-snippet-ui-001.json`. These result and trace directories are gitignored. If absent on another machine, rerun rather than claiming a pass.
6. Adapter and score implementation: `scripts/codex_checkout_adapter.py`, `evaluation/core.py`, `scripts/evaluate.py`, and `scripts/promote-candidate.py`. `scripts/audit_failed_answer.py` audits saved invalid answers without another model call.

The candidate and review files are currently untracked. Other untracked SRM and checker files also exist. Preserve all of them. The tracked checkout was clean for the latest replay, but check current status before any new run or promotion.

## Exact next action

Review the three failed expectations with the product owner. Decide whether "Source view" with equivalent 2026.7 evidence is acceptable, whether explicit `SIGNATURE_SCAN` is necessary for a first scan, and whether the Detect-version caveat is a real answer failure or a scorer false positive. Also decide whether the answer must use generic latest Detect scripts rather than pinning 12.0.0. Record the decision in the reviewed case and its notes. Do not relax a gate solely because one model answer failed it.

After that review, change only the accepted case assertions or the actual answer guidance. Run local case checks, capture one fresh replay from a clean tracked checkout, and inspect the full answer and citations. If the replay passes, run the promotion command **without** `--apply` and inspect every gate. Apply only after human approval. Do not run the 30 baseline and six regression cases as a batch to settle this one question.

## After DS-08

DS-08 is done when at least this reviewed feedback case can traverse candidate, review, measured replay, dry-run preview, and deliberate promotion without weakening source or provenance checks. The next documented step is to use that same workflow for later customer corrections while keeping candidates separate from verified regressions. The repository does not currently define a numbered DS-09 milestone in the checked guides; do not invent one.

Longer term, this makes the local documentation router more reliable through small, evidence-backed customer questions. It does not turn the corpus into a live Black Duck validator or an automatically self-improving agent. Product expansion, package distribution, and hosted search remain separate decisions that need their own scope and validation.
