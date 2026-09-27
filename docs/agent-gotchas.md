# Agent gotchas

Known tooling problems and their workarounds. Record only environment, tool, and command friction here. Answer-content corrections go through feedback candidates and `docs/ds-08-promotion.md`, not this file.

Agents do not load this file as evaluated instructions. It is outside the evaluation profile's `instruction_files` and `evidence_roots`.

Each entry states what happened, the workaround, and where it was observed.

## Git from a Linux shell reports thousands of modified files

Observed 2026-09-27 from a Linux shell over the Windows checkout: 2,773 tracked files reported as modified. Committed blobs use LF line endings. The repository has no `.gitattributes`, and the Linux shell does not see the Windows `core.autocrlf` setting. Line-ending differences are the likely cause; the diff was not confirmed because it exceeded the shell timeout.

Workaround: check dirty state with Windows Git before a replay or promotion. Do not treat a Linux-shell dirty flag as proof of real changes. Full `git status` or `git diff --stat` over the mount can take more than two minutes; prefer plumbing commands such as `git cat-file` and `git rev-parse`.

## The Codex CLI on PATH can reject current models

Recorded in `docs/ds-08-checkpoint.md`: the older CLI on PATH rejected GPT-6, while the app-managed CLI accepted it.

Workaround: set `DOC_SEARCH_CODEX_BIN` to the current Codex executable before running the adapter.

## Evaluation results and feedback are local only

`evaluation/results/`, `evaluation/traces/`, `feedback/`, and `.local/` are gitignored. They do not exist on another machine or in a fresh clone.

Workaround: rerun a replay instead of claiming a saved pass. Back up `feedback/candidates/` separately if it matters.

## A root AGENTS.md would bypass evaluation provenance

The DS-07 adapter runs `codex exec --cd <checkout>`, and Codex loads a root `AGENTS.md` automatically. The evaluation profile hashes only its listed `instruction_files`.

Workaround: keep agent-maintenance rules in `CLAUDE.md` and this file. Add any new evaluated instruction file to the profile's `instruction_files`.
