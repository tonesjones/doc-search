# Phase 1 — Black Duck SCA baseline

Baseline ID: `bd-docs-9485d952-20260823`  
Git revision: `9485d952e1a15f65fafecd6eb2c92b1ec435357b`  
Production path: Codex CLI 0.147.0 → installed `bd` skill  
Model: `gpt-5.6-sol`, high reasoning  
Prompt/skill revision: `bd-skill-sha256:df1549739d1bba197529036b0f76dcd202f8c1788e72eedb464f48deaebceb62`

## What was measured

All 30 verified SCA cases ran sequentially through the unchanged production answer path. Expected facts, expected behavior, eval IDs, and evidence were not supplied to that path. Raw answer traces and machine results are gitignored.

| Metric | Result |
|---|---:|
| Measured cases | 30/30 |
| Pass / fail | 12 / 18 |
| Recall@1 | 3.3% |
| Recall@3 | 20.0% |
| Recall@5 | 43.3% |
| Version accuracy | 96.3% |
| Insufficient-evidence cases | 0 |
| Unsupported claims | 1 |
| Citation failures | 5 |
| Abstention accuracy | 0.0% (one wrong-version case) |
| Mean latency | 24,763 ms |
| Min / max latency | 16,041 / 86,057 ms |

## Failure distribution

| Failure class | Count |
|---|---:|
| SYNTHESIS_FAILURE | 17 |
| CITATION_FAILURE | 5 |
| RETRIEVAL_FAILURE | 3 |
| VERSION_FAILURE | 1 |
| UNSUPPORTED_CLAIM | 1 |
| ABSTENTION_FAILURE | 1 |

The severe case is `sca-version-caveat-001`: the question requested SCA 2026.4, but the production path answered from the pinned 2026.7 corpus instead of abstaining. Many synthesis failures are literal `EXACT_FACT` mismatches that may include semantically adequate paraphrases; no semantic judge was added, so these remain strict deterministic baseline failures rather than being waived.

## Instrumentation and evaluation foundation

- `answer_id` traces include query, product/version, ranked consulted files, unavailable scores as null, citations, answer, revisions, model settings, token usage, and latency.
- Secret-shaped fields, authorization headers, bearer values, and common assignments are redacted.
- The evaluator separates retrieval, version, exact facts, citations, unsupported claims, and abstention.
- The 30 SCA cases are deterministically tied to checked-in 2026.7 Markdown evidence.
- The GitHub issue form and feedback conversion command create only `candidate` regression cases until human/source verification.
- Cheap infrastructure tests run in CI; live model evaluation remains explicit.

## Feedback and regression workflow

1. File the Documentation answer feedback issue with the `answer_id`, category, and plain-language comment.
2. Recover the gitignored trace and reproduce the answer.
3. Validate the disputed claim against authoritative, version-matched documentation.
4. Classify the root cause.
5. Convert the report with `feedback-to-eval`; it remains `origin: team-feedback`, `verification_status: candidate`.
6. A human verifies expected behavior, version, evidence, required facts, and forbidden facts.
7. Deterministic validation must pass before promotion to the permanent regression JSONL.

Nothing automatically edits documentation, the skill, prompts, retrieval, indexes, models, or branches.

## Commands

```powershell
python -m unittest discover -s tests -v
python scripts/evaluate.py --cases evaluation/cases/sca-baseline.jsonl --adapter python scripts/codex_production_adapter.py --label "BLACK DUCK SCA PHASE 1 BASELINE" --output evaluation/results/sca-baseline.json --trace-output evaluation/traces/sca-baseline
python scripts/phase1-gate.py --report evaluation/results/sca-baseline.json
./scripts/feedback-to-eval.ps1 -Feedback C:\secure\feedback-123.json -FeedbackId 123
```

## Gate

`PHASE 1 GATE: PASS`. Architecture, snapshot, tracing, verified cases, production-path measurements, factuality/abstention checks, taxonomy, feedback capture, candidate regression workflow, and reproducible report are present. The gate measures foundation completeness; it does not claim the 12/30 quality result is acceptable.
