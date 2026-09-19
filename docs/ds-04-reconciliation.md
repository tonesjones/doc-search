# Reconcile the existing implementations

Assessment date: September 19, 2026. This is a dated inventory, not a statement
that local or remote state cannot subsequently change.

## Decision

Maintain the merged `master` checkout and its root router as the supported
source workflow. Retain the existing experiment as a source of components and
historical evidence. Do not merge it wholesale or recreate its evaluation system.
The [supported workflow](supported-workflow.md) defines how to invoke and evaluate
the selected profile without changing anyone's installed configuration.

## Current state

| Implementation | Observed state | Disposition |
|---|---|---|
| Merged doc-search | `0f8c09a`, including DS-01 through DS-03 | Maintain as the shared source |
| Remote verified-learning branch | `a5d0430` | Preserve as experimental history |
| Local Product Docs checkout | Same branch tip, with 35 Git status entries for modified files and untracked paths | Preserve all changes; selectively port after review |
| Installed personal bd skill | Resolves `TONYDUCK_DOCS_ROOT`, otherwise the local Product Docs checkout; no override observed in the audit process | Current personal entrypoint, not equivalent to the merged router |
| Codex doc-skills plugin | Removal recorded in its setup task; no matching config entry or cached package found in current inspection | Removed profile, not a supported release |
| Other Docs Skills packages | No identifiable current copy found in inspected Claude and Cursor plugin locations | Unverified; cannot certify distribution contents |

The installed bd skill routes Bridge through the SCA directory and index. The
merged repository routes Bridge to its own root. The installed skill reads SCA
AGENTS.md, which in the experiment includes lab-specific capacity rules and
feedback promotion instructions. The inspected merged root and SCA instructions
do not contain those lab identifiers or experimental promotion rules.

This establishes instruction divergence. It does not establish that another
person received an affected package. No credentials or runtime environment files
were read or copied. Package absence is not a successful credential audit of an
unavailable package.

## Reuse inventory

Paths in this table refer to the experimental checkout unless marked merged.

| Component | Evidence and current limit | Action |
|---|---|---|
| `evaluation/core.py` | Case validation, exact-fact scoring, citations, trace metadata, and redaction | Reuse in DS-07 after reviewing measurement semantics |
| `evaluation/cases/baseline.jsonl` | 22 records marked verified | Preserve as a historical mixed-product baseline |
| `evaluation/cases/sca-baseline.jsonl` | 30 records marked verified | Reuse after rechecking sources and applicability; do not replace with a new duplicate set |
| `evaluation/cases/sca-regressions.jsonl` | Six records marked verified, with local modifications | Preserve and review their corrections before porting |
| `evaluation/reviews/` and `evaluation/scoring/` | Human adjudications, candidate conflicts, and approved wording equivalents; some are modified locally | Retain provenance; review equivalents for overfitting |
| `scripts/codex_production_adapter.py` | Installed-bd invocation, event parsing, prompt hash, Markdown-only evidence, version guard; locally modified | Adapt in DS-07, not usable unchanged for merged workflow |
| `scripts/trace-answer.py` and `scripts/evaluate.py` | Trace capture and evaluation wrapper | Reuse orchestration after binding it to an explicit profile |
| `scripts/feedback-to-eval.py` | Untrusted candidate conversion, with modified local implementation | Reuse in DS-08 after review |
| `scripts/promote-candidate.py` | Local untracked promotion command with dry run and explicit apply | Preserve; add replay-version and freshness checks before shared use |
| `scripts/check-merge-readiness.py` | Local untracked gate over saved evaluation results | Review thresholds and stale-result handling before porting |
| `validators/core/` | Claim/request/result contracts, including INCONCLUSIVE and reasons | Retain separately from the merged offline report until an explicit mapping exists |
| `validators/blackduck_sca/` | Read-only authentication, project, media, and current-user probes | Reuse selectively in DS-06; strengthen assertions first |
| `scripts/sca-provision-test-project.py` | Environment-specific mutation tooling | Keep lab-only; not needed for DS-04 |
| `BlackDuck SCA/approved-guidance/` | Untracked local expert guidance used by saved answers | Preserve separately from official source snapshots; review applicability before promotion |
| Old SCA-nested Bridge and SRM content | Diverges from current product separation | Do not port the old layout back into master |
| Merged SCA verifier and report schema | Implemented DS-03 offline checks | Retain as corpus checks, not answer-accuracy certification |

Counts describe records, not independently verified factual correctness. Some
experimental components are committed, but the adapter, cases, and instructions
also have local changes. A branch SHA alone cannot reproduce the current profile.

## Reproduced findings

1. The adapter's `version_mismatch_trace` rejects an explicit `2026.4.0` request
   with `EXPLICIT_VERSION_NOT_PINNED`, although that OpenAPI snapshot exists.
2. `product_evidence_paths` returns an empty list for the OpenAPI JSON path.
3. `parse_event_stream` infers opened sources from paths in command text and
   rereads whole files, including search-hit files. This is an approximation of
   observed retrieval, not proof of the exact text the model saw.
4. The adapter launches Codex with `danger-full-access`. A future evidence-only
   evaluation must select an appropriate restricted execution profile explicitly.
   This command was inspected, not launched during DS-04.
5. `_validate_project_media` records the response content type but passes on HTTP
   200 alone. It does not establish the claimed response media type.
6. `_version_compatible` accepts a missing observed or requested version. Runtime
   claims requiring version matching must treat that absence explicitly.
7. Promotion verifies matching question and product, but does not compare the
   replay's requested version or require the current prompt/source revision.
8. Exact required/forbidden fact matching does not examine every material claim.
   A zero unsupported-claim count is not a general entailment guarantee.

These are implementation findings and bounded porting prerequisites, not live
server findings. They explain why passing the existing tests is insufficient for
immediately promoting the experiment.

## Trace a real historical question

Question: Does SCA enforce a strict maximum size for an individual project, and
how should a very large repository be handled?

The saved trace `evaluation/traces/feedback-sca-project-size-guidance-001.json`
records an answer generated August 25 with `gpt-5.6-terra` and a prompt revision.
The inspected adapter's path is Codex execution, installed bd, local SCA AGENTS,
selected evidence, then a customer-visible answer and citations.

The answer cites separate expert guidance on project size and official topic
files on subprojects and licensed code-size limits. All three cited paths exist.
Replaying the saved answer through the current scorer and approved equivalents
returns PASS with no reported failures. Its saved prompt revision does not match
the current computed revision.

This demonstrates an existing correction-to-answer path worth preserving. It is
a historical replay, not fresh answer generation or independent verification of
the project-size advice. The raw trace and expert guidance remain local.

## Trace the selected workflow manually

Question: In the SCA 2026.7 documentation, where is a business-unit group's BOM
Manager role assigned, and how does it reach the projects?

The reviewer followed the merged root router, selected SCA through products.json,
read its SKILL.md and AGENTS.md, and opened these topic bodies:

- [Project group roles reference](../BlackDuck%20SCA/docs/help-center/administering-black-duck/administering-user-accounts/understanding-roles/project-group-roles-reference.md).
- [Editing a project group](../BlackDuck%20SCA/docs/help-center/managing-black-duck/managing-project-groups/editing-a-project-group.md).

Resulting answer: Assign the user group the BOM Manager role on the relevant
project group. The role applies to projects within that group, and users inherit
access through their group membership. Use the project group's user-group
assignment controls. This describes the local 2026.7 documentation; it does not
establish a customer's current grants or prove an out-of-scope request is denied.

This is a manual trace by the DS-04 reviewer using the merged source at 0f8c09a.
It is not an automated adapter run or a new RBAC experiment. A later baseline
must record the configured model and full trace rather than infer them here.

## Verification and preservation

- Ran the experimental test suite with bytecode writes disabled. All 41 tests
  passed, including candidate conversion, promotion to temporary fixtures,
  scoring, redaction, and mocked runtime validators.
- Replayed one existing answer through the scorer without generating a new
  answer, promoting guidance, or contacting a server.
- Exercised the adapter's version guard and citation extraction offline.
- Inspected current Git status and refreshed remote branch references.
- Created DS-04 documentation in an isolated worktree from merged master.

No experimental source, installed skill, package, configuration, customer data,
or live RBAC state was changed. Old performance and accuracy summaries remain
historical. The remaining package-certification work is conditional on an actual
distributable artifact, not a reason to assume parity today.

## Milestone disposition

DS-04 completes reconciliation and selects the source workflow. It deliberately
does not claim that the installed personal skill has migrated or that the old
evaluator measures the new workflow. Carry the adapter repairs into DS-07, the
runtime prerequisites into DS-06, and promotion provenance into DS-08. Reuse the
existing 30-case SCA baseline and six regressions after review instead of building
another independent evaluator and baseline.
