# Agent gotchas

Known tooling problems and their workarounds. Record only environment, tool, and command friction here. Answer-content corrections go through feedback candidates and `docs/ds-08-promotion.md`, not this file.

Agents do not load this file as evaluated instructions. It is outside the evaluation profile's `instruction_files` and `evidence_roots`.

Each entry states what happened, the workaround, and where it was observed.

## Git from a Linux shell reports thousands of modified files

Observed 2026-09-27 from a Linux shell over the Windows checkout: 2,773 tracked files reported as modified. Committed blobs use LF line endings. The repository has no `.gitattributes`, and the Linux shell does not see the Windows `core.autocrlf` setting. Confirmed the same day: with `core.autocrlf=true`, the count drops to 0.

Workaround: from a Linux shell, run `GIT_OPTIONAL_LOCKS=0 git -c core.autocrlf=true status --porcelain --untracked-files=no`. `GIT_OPTIONAL_LOCKS=0` keeps a read-only status from leaving lock files. `git diff --stat` over the mount can take more than two minutes; prefer plumbing commands such as `git cat-file` and `git rev-parse`.

## Git writes from the linked shell leave temporary object files

Observed 2026-09-27: writing objects from the linked Linux shell printed `unable to unlink '.git/objects/xx/tmp_obj_*': Operation not permitted`. The objects were written correctly, but the shell cannot delete files by default, so the temporary files remain.

Workaround: ignore them; `git gc` or `git prune` from Windows removes them later. Prefer Windows Git for commits when a Windows shell is available.

The same shell also leaves `.git/HEAD.lock` and `.git/objects/maintenance.lock` after a commit, and a status killed by a timeout leaves `.git/index.lock`. Those locks block the next Git command on Windows. Rename them aside (`mv` works where `rm` does not) or delete them from Windows. Avoid Git writes from the linked shell: commit from Windows, or from a separate clone that can push.

## The Codex CLI on PATH can reject current models

Recorded in `docs/ds-08-checkpoint.md`: the older CLI on PATH rejected GPT-6, while the app-managed CLI accepted it.

Workaround: set `DOC_SEARCH_CODEX_BIN` to the current Codex executable before running the adapter.

## A failed Codex replay reports an empty error

Recorded in `docs/ds-08-checkpoint.md`: the replay at `bc4f9d3` returned `NOT_MEASURED` with `Codex exited 1:` and no message. With `--json`, Codex reports errors on stdout, which the adapter discards. The likely cause was the Codex binary on PATH (`codex-cli 0.149.1`) with `DOC_SEARCH_CODEX_BIN` unset; this was not confirmed.

Workaround: set `DOC_SEARCH_CODEX_BIN` first. To diagnose, run the same `codex exec` command by hand and read its stdout events.

## Evaluation results and feedback are local only

`evaluation/results/`, `evaluation/traces/`, `feedback/`, and `.local/` are gitignored. They do not exist on another machine or in a fresh clone.

Workaround: rerun a replay instead of claiming a saved pass. Back up `feedback/candidates/` separately if it matters.

## A root AGENTS.md would bypass evaluation provenance

The DS-07 adapter runs `codex exec --cd <checkout>`, and Codex loads a root `AGENTS.md` automatically. The evaluation profile hashes only its listed `instruction_files`.

Workaround: keep agent-maintenance rules in `CLAUDE.md` and this file. Add any new evaluated instruction file to the profile's `instruction_files`.

The same risk applies to any replacement adapter. A Claude Code adapter run in this checkout would load `CLAUDE.md` automatically. Before switching adapters, list the files that model's CLI loads on its own. Then either keep them out of the evaluated run or add them to `instruction_files`.
