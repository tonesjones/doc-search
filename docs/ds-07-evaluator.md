# Evaluate SCA answers from this checkout

DS-07 measures answers produced through the merged repository router. It does not use the separately installed personal `bd` skill.

## Check the cases and evidence

Run the four-case deterministic check before a model run:

```powershell
python -B scripts/evaluate.py `
  --cases evaluation/cases/sca-regressions.jsonl `
  --case-id-file evaluation/cases/sca-smoke.txt `
  --deterministic-only --allow-unmeasured `
  --output evaluation/results/ds-07-smoke-deterministic.json
```

The full case bank contains 30 baseline cases and six feedback regressions. It is a reference bank, not the routine model-run gate. The four IDs in `evaluation/cases/sca-smoke.txt` cover a first C/C++ scan, a SaaS distribution choice, the current access-token menu, and licensed size limits. The project-definition and phase cases remain in the reference bank.

This verifies local source paths and required exact facts. It does not measure answer quality, retrieval, or generation. The 30 baseline cases remain available for targeted investigation, not automatic reruns. The baseline token-path and 10GB cases contain stale or license-dependent expectations and must not be used as promotion gates without review.

## Run one answer

Run one case only after the deterministic check passes. Use this command on a host where the nested Codex CLI can load its home directory and authentication:

```powershell
python -B scripts/evaluate.py `
  --cases evaluation/cases/sca-regressions.jsonl `
  --case-id feedback-sca-project-definition-001 `
  --adapter python scripts/codex_checkout_adapter.py `
  --trace-output evaluation/traces/ds-07-smoke `
  --output evaluation/results/ds-07-smoke.json
```

The adapter uses `gpt-5.6-terra` with medium reasoning by default. Set `DOC_SEARCH_MODEL` and `DOC_SEARCH_REASONING_EFFORT` to override those values for a named run. Review the trace before selecting another case. Stop if the result is `NOT_MEASURED`.

The nested CLI currently fails with `Could not find home directory` in the Codex desktop restricted shell, before a model receives the case. Native Codex tasks can answer a case, but their output needs validated excerpts and a trace with the actual prompt, model, and clean-checkout metadata before `--trace-dir` can certify it. Do not label a native answer as a production adapter result without that trace.

The adapter starts an ephemeral Codex process in the read-only sandbox. The process loads the root `SKILL.md`, resolves the product through `products.json`, and follows the selected product instructions. It cannot write to the checkout.

Each returned evidence item contains a repository path and an excerpt. The adapter verifies the excerpt against the named file and permits whitespace-only formatting differences. It rejects evidence outside the profile and evidence with a version that conflicts with the requested version.

## Read the result

Each trace records these revisions:

- The checkout commit and tracked-file dirty state.
- The Git tree that contains the sources.
- A hash of the router and product instructions.
- A hash of the adapter prompt.
- The model and reasoning setting.

Saved traces fail the current-profile check after the checkout, source tree, or instructions change. Re-run the cases before comparing a changed router, source tree, prompt, or model.

The deterministic scorer checks required and forbidden facts, citations, retrieval paths, and version metadata. Semantic facts remain `NOT_MEASURED` without a separate grader. A model grader can assist review, but it is not promotion authority.

## Current boundary

DS-07 does not contact a Black Duck server. It does not change the feedback candidate or promotion workflow. DS-08 owns those changes.
