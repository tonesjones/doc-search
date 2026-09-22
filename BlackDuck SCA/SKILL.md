---
name: black-duck-sca
description: Answer Black Duck SCA, Detect, Alert, C/CPP Tool, and SCA MCP questions from the local versioned documentation and verify the offline corpus.
---

# Black Duck SCA

Read [AGENTS.md](AGENTS.md) for source priority and maintenance rules. Use
[corpus-status.md](corpus-status.md) to locate the relevant companion product.
Paths here are relative to this skill's directory.

## Retrieve evidence

- For SCA server, UI, BOM, policy, and project questions, use [index.md](index.md).
  The narrative documentation snapshot is 2026.7.
- For the current access-token menu label, read the [user-observed UI note](../evaluation/guidance/access-token-menu.md) with the SCA help-center token page. The note records where the UI differs from the page.
- For unversioned Detect questions, start at [index-detect.md](index-detect.md).
  Detect 12.0.0 is the default. Use the 11.5.1 catalog only when that version is
  named or a comparison is requested. State which version supports the answer.
- For Alert, C/CPP Tool, and SCA MCP, follow their indexes from the corpus hub.
- For exact REST contracts, combine API guidance with the versioned OpenAPI file
  under `sources/openapi/`. The 2026.4.0 specification does not establish a
  2026.7 endpoint contract. Cite the specification version and JSON path.
- For Bridge CLI and CI integrations, hand off to [Bridge](../Bridge/AGENTS.md).
  Load SCA alongside Bridge only when the question needs both products.

Open the matching topic bodies before answering. Cite their local paths and
distinguish documented behavior from an inference or an observed live result.
Do not infer UI navigation, API endpoints, or Detect properties from names alone.
If the requested version or topic is absent, report the gap. Refresh only within
the user's requested scope, following AGENTS.md.

## Verify offline

From the repository root, run:

```powershell
python -B "BlackDuck SCA/verification/verify.py"
```

The command prints one JSON report using the root verification report schema.
It validates the registered SCA corpora and follows selected index-to-topic
retrieval paths. It also validates the sanitized RBAC evidence case under
`verification/cases/`. Evidence includes corpus warnings and the versions checked.
Exit code 0 means the offline checks passed. Exit code 1 means a check failed.
Live UI and API checks remain `NOT_RUN`. A `PASS` does not establish live product
behavior or measure the quality of an agent's answers.
