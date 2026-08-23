# SCA RAG measurement and runtime-validation report

> Scope note: the verified feedback and continuous-learning workflow delivered in this session is implemented for Black Duck SCA only. Replication to the other product lines is a follow-on effort and must be validated separately for each product and version.

## Outcome

The repository now has a production-path SCA baseline, answer tracing, verified regressions, team-feedback capture, a common runtime-validator contract, one SCA validator, safe `Tony RAG` provisioning, and a combined docs/RAG/runtime diagnosis report. Retrieval and prompts were not optimized.

## Phase 1

The actual system is a local, versioned Markdown corpus searched by the installed `bd` skill using indexes, recursive text search, selected file reads, and assistant generation with local citations. The 30-case SCA 2026.7 baseline measured 12 pass and 18 fail, Recall@1/3/5 of 3.3%/20.0%/43.3%, 96.3% version accuracy, five citation failures, one unsupported claim, and 0% abstention accuracy on the single wrong-version case. Mean latency was 24.8 seconds.

The critical factuality control failure is answering a 2026.4 question from 2026.7 evidence. This is also directly relevant to Phase 2 because the available runtime is 2026.4.0.

## Phase 2

Black Duck SCA was selected because the user supplied a shared test instance and token, its API is documented, the account advertises project creation, and isolated reversible naming is possible. The exact `Tony RAG` project and five `RAG-VAL-*` versions were created; no other project was touched.

Five API-first checks executed. Every individual HTTP/shape/media/isolation assertion passed, but every primary runtime result is `INCONCLUSIVE / VERSION_MISMATCH`: the environment is 2026.4.0 while the authoritative local corpus is 2026.7. No automatic documentation or RAG change follows from this observation.

## Mismatches

- `VERSION_MISMATCH`: local SCA corpus 2026.7 vs runtime 2026.4.0.
- `RUNTIME_INCONCLUSIVE`: five runtime validations.
- `RAG_FAILURE`: baseline includes retrieval, synthesis, citation, version, unsupported-claim, and abstention failures; no combined case is labeled RAG_FAILURE while runtime remains inconclusive.
- No `DOC_RUNTIME_MISMATCH` is claimed because version compatibility is absent.

## Limitations

- Exact-fact scoring is deliberately strict and can reject adequate paraphrases; semantic evaluation was not configured.
- Tool-event order is used as retrieval rank; the production path has no numeric retrieval score.
- The SCA runtime does not match the corpus version, so runtime observations cannot validate 2026.7 behavior.
- No destructive, account-lockout, archive, LTS, scan, policy, role mutation, or customer-data test ran.
- Other products were not assessed per the SCA-only scope.

## Ranked next actions (not implemented)

1. **Observed problem:** 2026.4 questions can receive 2026.7 answers. **Evidence:** wrong-version baseline case failed abstention/version controls. **Proposed improvement:** add a general version-compatibility/abstention policy at the skill boundary, separately versioned from this baseline. **Metric:** abstention accuracy and version accuracy. **Risk:** over-abstention. **Effort:** small.
2. **Observed problem:** correct SCA sources rank behind routing/index files. **Evidence:** Recall@1 3.3%, Recall@5 43.3%. **Proposed improvement:** investigate a generalized evidence-ranking policy using this preserved baseline. **Metric:** Recall@1/3/5. **Risk:** regressions across products. **Effort:** medium.
3. **Observed problem:** runtime validation is version-inconclusive. **Evidence:** SCA 2026.4.0 vs corpus 2026.7. **Proposed improvement:** provide a 2026.7 test instance or add a separately pinned 2026.4 corpus before rerunning. **Metric:** conclusive runtime rate. **Risk:** corpus/instance maintenance. **Effort:** medium.
