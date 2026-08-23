# Phase 2 — Black Duck SCA runtime POC

## Environment and isolation

- Host: `sca.field-test.blackduck.com` (exact HTTPS allowlist)
- Requested/documentation version: 2026.7
- Observed UI version: 2026.4.0
- Authentication: API token exchanged successfully for a bearer token
- Isolated project: `Tony RAG`
- Other projects touched: 0

The server's authenticated 2026.4 API reference advertised `POST` on `/api/projects` and documented the v7 project/v5 project-version request shapes. The ownership-marked `Tony RAG` project was created with five versions:

- `RAG-VAL-auth`
- `RAG-VAL-current-user`
- `RAG-VAL-isolation-name`
- `RAG-VAL-project-list`
- `RAG-VAL-project-media`

The resources are retained by explicit user request. The provisioner is idempotent, requires exact names and a marker before reuse, and cannot target any other project.

## Runtime results

All low-level API assertions passed: token exchange returned 200; current-user returned 200; projects returned a countable collection; the documented custom media type was accepted and returned; and exactly one ownership-marked `Tony RAG` project exists.

All five primary results are nevertheless `INCONCLUSIVE / VERSION_MISMATCH`, because a 2026.4.0 environment cannot establish 2026.7 documentation behavior. Cleanup is `PASS` in the sense that the explicitly requested retained state was verified; nothing was deleted.

| Validation | Assertions | Primary result | Diagnosis |
|---|---:|---|---|
| Token exchange | 1/1 pass | INCONCLUSIVE — VERSION_MISMATCH | RUNTIME_INCONCLUSIVE |
| Current user | 2/2 pass | INCONCLUSIVE — VERSION_MISMATCH | RUNTIME_INCONCLUSIVE |
| Isolation name | 3/3 pass | INCONCLUSIVE — VERSION_MISMATCH | RUNTIME_INCONCLUSIVE |
| Project list | 3/3 pass | INCONCLUSIVE — VERSION_MISMATCH | RUNTIME_INCONCLUSIVE |
| Project media type | 2/2 pass | INCONCLUSIVE — VERSION_MISMATCH | RUNTIME_INCONCLUSIVE |

## Safety and integration

The common contract supports `PASS`, `FAIL`, and `INCONCLUSIVE`, separate observations/assertions, observed/requested versions, artifacts, reason, and cleanup result. Auth, permission, environment, timeout, unsafe operation, and version mismatch are not treated as product claim failures.

`combined-evaluate.py` keeps `RETRIEVAL_RESULT`, `DOC_FAITHFULNESS_RESULT`, `CORPUS_CORRECTNESS_RESULT`, `RUNTIME_VALIDATION_RESULT`, and `OVERALL_DIAGNOSIS` separate. All five current combined diagnoses are `RUNTIME_INCONCLUSIVE`.

## Commands

```powershell
python scripts/validate-runtime.py --product blackduck-sca --all --requested-version 2026.7 --output runtime/results/sca-runtime.json
python scripts/sca-provision-test-project.py --allow-mutations --confirm-project "Tony RAG"
python scripts/combined-evaluate.py
```

## Remaining products

Per the requested SCA focus, no other product validator was implemented or runtime-assessed. Their API, UI, environment, credential, mutation, and runtime-readiness fields remain `Unknown`; the recommended next step is `Do not assess until explicitly selected`.
