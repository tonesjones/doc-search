---
name: codesight
description: Answer Black Duck Code Sight questions from the local 2026.9.0 documentation corpus and verify its offline integrity.
---

# Black Duck Code Sight

Use this skill for questions about Code Sight, including supported IDEs, installation, authentication, viewing issues, product integrations, preferences, troubleshooting, and release notes.

## Retrieve evidence

- Read [README.md](README.md), [AGENTS.md](AGENTS.md), and [CHECKPOINT.md](CHECKPOINT.md) for scope and source rules.
- Use [index.md](index.md) and [corpus-status.md](corpus-status.md) to locate topics, then open the matching files under `docs/` before answering.
- The pinned corpus is English Code Sight **2026.9.0**. State that version when it matters.
- Code Sight covers workflows involving SCA, Coverity, Polaris, and SRM. Load a sibling product corpus only when the question asks about that product's own behavior or a cross-product workflow.
- Cite local Markdown paths. Distinguish documented behavior from inference or live observations. If the corpus is silent, say so; do not guess UI paths or product behavior.
- Use official Fluid Topics APIs only when the corpus is missing, stale, or the user asks for a refresh. Follow `AGENTS.md` and the user's requested scope.

## Verify offline

From the repository root, run:

```powershell
python -B "CodeSight/verification/verify.py"
```

The JSON report covers corpus integrity and selected index-to-topic retrieval checks. A `PASS` applies only to those offline checks; it does not establish live product behavior or answer accuracy.
