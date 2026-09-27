# Claude Code instructions

This checkout is a local Black Duck documentation corpus with a product router and an answer evaluator. For a product question, start at `SKILL.md` and follow "Use this repository with a coding agent" in `README.md`.

## Adaptive behavior

Adapted from the adaptive-agent plugin. Lessons flow back into instructions and skills, but only through the path that fits the lesson.

### Sort each lesson before acting on it

1. **Tooling friction:** a path, command, tool version, environment, or permission problem. Fix the immediate problem, then record it:
   - Repository tooling: add an entry to `docs/agent-gotchas.md`.
   - Finding or reading the checkout from the user's `bd` skill: propose a Gotchas entry for that skill for the user to review. Do not write skill files directly.
2. **Answer content:** an answer was wrong, incomplete, or cited the wrong source. Do not patch `SKILL.md`, `AGENTS.md`, `products.json`, the adapter prompt, or case assertions to fix it. After the user confirms, record a feedback candidate under `feedback/candidates/`. It then follows `docs/ds-08-promotion.md`: human review, fresh replay, dry-run preview, and a deliberate `--apply`.

If a lesson could be either kind, treat it as answer content.

### Protect evaluated instructions

The `instruction_files` in `evaluation/profiles/*.json` and the adapter's `PROMPT_TEMPLATE` shape measured answers. Change them only when the user asks, on a branch. Expect saved traces to become stale after the change.

Do not create a root `AGENTS.md` or put these rules in any `AGENTS.md`. The DS-07 adapter runs Codex in this checkout, and Codex loads a root `AGENTS.md` automatically. That file is not in `instruction_files`, so it would change evaluated behavior without changing `instruction_revision`.

### Before a task

Read `docs/agent-gotchas.md` and the relevant `CHECKPOINT.md` or handoff doc. Apply known workarounds before repeating a failed approach.

### Skill gaps

When a multi-step workflow has been done by hand three or more times (check `git log`), propose a skill. Do not create one silently. Current candidates are corpus refresh and replay-to-promotion. Write the replay skill only after the DS-08 scoring decisions are recorded.

### Skill review

`/skill-review` covers the user's `bd` skill, the root and product `SKILL.md` files, this file, and `docs/agent-gotchas.md`. Also confirm that each skill and verifier path in `products.json` exists, and report missing ones as gaps. Put changes on a branch for review. Do not auto-commit.
