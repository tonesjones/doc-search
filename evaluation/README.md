# Evaluation and feedback workflow

The evaluator wraps the real answer path; it does not implement retrieval or prompting. A production adapter reads this JSON on standard input:

```json
{"question":"...","product":"blackduck-sca","product_version":"2026.7"}
```

It returns one JSON object containing at least `answer`. For measurable retrieval/citation results it should also return ranked `retrieved_chunks` and `citations`:

```json
{
  "answer": "...",
  "processed_query": null,
  "retrieved_chunks": [
    {"file":"BlackDuck SCA/docs/api/authenticating-with-the-api.md","rank":1,"score":null,"content":"...","metadata":{"version":"2026.7"}}
  ],
  "citations": [{"file":"BlackDuck SCA/docs/api/authenticating-with-the-api.md"}],
  "model": "provider/model-version",
  "model_parameters": {"temperature": 0}
}
```

Expected behavior, facts, eval IDs, and evidence are never sent to the adapter. Raw traces are written under `evaluation/traces/` and are gitignored.

## Commands

```powershell
# Cheap deterministic validation (schema/evidence only)
python -m unittest discover -s tests -v
./scripts/evaluate.ps1 -DeterministicOnly -AllowUnmeasured

# Baseline from already captured production traces (<case-id>.json)
python scripts/evaluate.py --trace-dir C:\secure\baseline-traces --label BASELINE

# Baseline through the real production adapter
python scripts/evaluate.py --adapter python scripts/codex_production_adapter.py --label "BLACK DUCK SCA PHASE 1 BASELINE" --timeout 700

# Capture one real answer trace
python scripts/trace-answer.py --question "..." --product blackduck-sca --product-version 2026.7 -- python scripts/codex_production_adapter.py

# Build or refresh the 30-case human-review packet without overwriting existing decisions
python scripts/build-human-review-packet.py

# Convert a feedback JSON export into a candidate regression
./scripts/feedback-to-eval.ps1 -Feedback C:\secure\feedback-123.json -FeedbackId 123

# Runtime POC and independent combined diagnosis
python scripts/validate-runtime.py --product blackduck-sca --all --requested-version 2026.7
python scripts/combined-evaluate.py
```

The normal evaluation command returns status 2 when any case is unmeasured, so a missing live dependency cannot be mistaken for a passing baseline. `-AllowUnmeasured` is reserved for recording an explicitly incomplete report.

## Feedback promotion

1. Team member submits the issue form with `answer_id`, category, and comment.
2. Maintainer recovers the gitignored trace and reproduces the answer.
3. Maintainer checks the disputed claim against authoritative corpus evidence.
4. `feedback-to-eval` creates a `verification_status: candidate` case in the gitignored `feedback/candidates/` area.
5. A human fills in expected behavior, authoritative evidence, required/forbidden facts, and version context.
6. Deterministic evidence validation must pass; semantic facts require an explicitly configured constrained judge and human review.
7. Only then is the case moved to the trusted baseline/regression JSONL.

Report volume changes priority, not factual status. No part of this flow edits documentation, skill instructions, retrieval, prompts, or indexes.

## Human baseline adjudication

`evaluation/reviews/sca-baseline-human-review.md` presents the customer-visible answer first and keeps expected evidence and machine scoring in a collapsed second pass. Record decisions in `evaluation/reviews/sca-baseline-adjudications.jsonl`; the generator preserves existing decisions when rerun and adds only missing case records. The baseline JSONL remains unchanged.
