# Use the supported documentation workflow

DS-04 selects the merged `tonesjones/doc-search` `master` branch as the maintained
source for this workflow. Use a clean checkout of the revision being evaluated.
The installed personal `bd` skill and the verified-learning branch remain a
separate experimental profile until explicitly migrated.

## Answer a customer question

Give the assistant this instruction with your question:

> Use this checkout's root SKILL.md and products.json. Load the selected product's
> skill when present, otherwise its AGENTS.md. Open the relevant source files and
> answer the question with version-qualified evidence. State any missing context
> that materially affects the answer.

The root [router](../SKILL.md) selects the product. For SCA, the
[product skill](../BlackDuck%20SCA/SKILL.md) supplies version and source rules.
Use companion or sibling products when the requested behavior depends on them.
Treat this as a documented interactive workflow, not an automated answer service.

For a question about what a customer environment actually does, identify the
needed live observation separately. Documentation alone establishes documented
behavior. Record the tested identity, environment and versions before treating a
live result as evidence. A browser or API connection alone does not validate a claim.

## Record an evaluation

Record the question, checkout revision, dirty state, model and model settings,
entrypoint, loaded instruction revisions, opened evidence, answer, and citations.
Label a manually traced answer as manual. Label a replay of a saved answer as
historical. Neither is a fresh run of the experimental adapter.

The DS-07 adapter invokes this checkout's router in a read-only Codex process. It
validates exact source excerpts from the allowed Markdown and OpenAPI roots. See
[the DS-07 evaluation guide](ds-07-evaluator.md) for the commands and evidence
boundary.

Run the SCA offline check separately:

```powershell
python -B "BlackDuck SCA/verification/verify.py"
```

The JSON report describes corpus integrity and selected retrieval checks. It does
not grade the answer. Preserve the runtime experiment's `INCONCLUSIVE` result
when translating reports later; do not silently convert it to `PASS` or confuse
it with an unattempted `NOT_RUN` check.

## Preserve the experiment

Keep the dirty Product Docs checkout, saved traces, reviewed guidance, feedback
candidates, and runtime configuration in place. Do not reset that checkout or
merge its branch wholesale. The [DS-04 inventory](ds-04-reconciliation.md) identifies
components to reuse and conditions that must be met first.

No personal skill settings, environment overrides, installed packages, or live
server configuration are changed by this milestone. Explicitly invoking this
checkout's router is the supported route while personal `bd` migration is pending.

## Distribute only a reviewed profile

No current Docs Skills package was available for certification in this audit.
Do not label another installation or cached package as equivalent to this checkout.
Before a new package is released, build from the chosen source revision, inspect
the actual output, and check its instructions and resources for lab configuration,
private evidence, credentials, and experimental promotion rules.

## Next steps

DS-05 fixes known integrity-check defects. DS-06 recovers the RBAC experiment as
a reproducible case. DS-07 adds the checkout-bound evaluator and recaptures its
baseline. DS-08 reuses the candidate-review design after strengthening its replay
provenance requirements.
