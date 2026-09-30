# Live evidence

Owner-reviewed observations from an isolated Black Duck SCA sandbox. Each record states what the live product showed and how it compares with the local documentation.

Live evidence is a separate evidence type. It is not documentation evidence, and answers must not cite it as a documentation source. This folder is deliberately outside the evaluation profile's `evidence_roots` and `instruction_files`, so adding records does not change evaluated behavior.

## Record rules

- One JSON file per reviewed observation session: `YYYY-MM-DD-<topic>.json`.
- Sanitized: no hostnames, URLs with hosts, user names, tokens, registration keys, or license-specific limits. Use the generic `environment` fields below.
- Raw, unreviewed observations stay in the ignored `.local/live-observations/`. A record enters this folder only after owner review.
- A sandbox replacement produces new records. It does not rewrite old ones.

## Shape

```json
{
  "id": "live-YYYY-MM-DD-<topic>",
  "evidence_type": "LIVE_UI_OBSERVATION | LIVE_UI_AND_API_OBSERVATION",
  "environment": { "product": "black-duck-sca", "server_version": "2026.7.0", "kind": "isolated sandbox" },
  "principal_role": "role the session held, never a user name",
  "observed_at": "ISO date",
  "method": "what was read; confirmation that nothing was changed",
  "findings": [
    {
      "case_id": "optional regression case this finding checks",
      "verdict": "CONFIRMED | PARTIAL | CONTRADICTED",
      "observed": "what the live product showed",
      "not_checked": "optional: what remains unverified"
    }
  ],
  "documentation_comparison": [
    { "file": "repo-relative doc path", "verdict": "CONSISTENT | ROUTE_CORRECT_LABELS_DIFFER | MISLEADING | WRONG", "note": "..." }
  ],
  "review": { "status": "APPROVED", "reviewed_by": "owner", "reviewed_at": "ISO date", "notes": "owner decisions" }
}
```
