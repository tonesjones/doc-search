# Promote one reviewed SCA feedback case

DS-08 keeps feedback separate from verified regression cases. Promotion reads one candidate, one human-reviewed case, and one saved answer trace. It does not generate an answer or contact Black Duck SCA.

## Preview the promotion

Start from a clean checkout. Capture the replay with the current answer prompt and source revision, then run:

```powershell
python -B scripts/promote-candidate.py `
  --candidate <candidate-json-or-jsonl> `
  --candidate-id <candidate-id> `
  --approved-case <reviewed-case-json> `
  --trace <replay-trace-json>
```

The command reports every gate failure and writes nothing by default. Review the approved case and the replay answer yourself. A passing exact-fact score does not establish that every claim is correct.

## Apply a reviewed case

After the preview passes and a reviewer approves the case, repeat the command with `--apply`. The command appends that one case to `evaluation/cases/sca-regressions.jsonl`. It rejects a duplicate case ID.

Promotion requires matching candidate and approved-case identity, the SCA profile, an explicit requested product version, local source paths and sections, a passing replay with model metadata, and a matching entry point, checkout, instructions, sources, and prompt. A dirty checkout or an older replay fails the gate. The `verified_by` field records a review claim; the command cannot authenticate the reviewer.

Keep candidate conversion, fresh replay generation, and the human approval outside this command. Do not promote a saved historical answer as if it were a current replay.
