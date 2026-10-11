# Keep the work fork in sync with this repository

This repository, `tonesjones/doc-search` on branch `master`, is public. A private work fork fetches from it and adds work-only features: self-validation and live-instance testing that use proprietary data. Changes flow one way, from this repository into the fork. Nothing flows back.

The fork stays mergeable because each path has one owner. Upstream owns every path it already has. The fork adds its own work under `work/` and does not edit upstream paths.

Agents do not load this file as evaluated instructions. It is outside the evaluation profile's `instruction_files` and `evidence_roots`.

## Find out which checkout you are in

Run `git remote -v` before you change anything.

- If `origin` is `github.com/tonesjones/doc-search`, you are in the upstream repository. Follow [Rules in the upstream repository](#rules-in-the-upstream-repository).
- If a remote named `upstream` is `github.com/tonesjones/doc-search` and `origin` is a different repository, you are in the work fork. Follow [Rules in the work fork](#rules-in-the-work-fork).
- If neither matches, ask the user before you edit.

## Path ownership

| Path | Owner | Can the fork change it? |
| --- | --- | --- |
| Corpus folders: `BlackDuck SCA/`, `Bridge/`, `CodeSight/`, `Coverity/`, `Polaris/`, `SRM/`, `Sigma/`, `Signal/` | Upstream | No |
| `SKILL.md`, `products.json`, `README.md`, `CLAUDE.md`, `verification-report.schema.json` | Upstream | No |
| `scripts/`, `evaluation/`, `tests/`, `docs/`, `.github/`, `.gitignore` | Upstream | No |
| `work/` | Fork | Yes. Upstream never creates this folder. |
| `.local/`, `feedback/`, `runtime/`, `.env.runtime`, `evaluation/results/`, `evaluation/traces/` | Nobody. Git ignores them. | Local only. Never commit them in either repository. |

These shared files collect appended records. They cause a conflict on every sync if both repositories add to them:

- `evaluation/cases/sca-regressions.jsonl`. `scripts/promote-candidate.py` appends here unless you pass `--output`.
- `evaluation/cases/sca-baseline.jsonl`
- `evaluation/scoring/sca-human-equivalents.jsonl`
- `BlackDuck SCA/verification/live-observations/`

## Rules in the upstream repository

- Do not build self-validation, self-learning verification, or live-instance testing features here. That work happens in the fork, under `work/`.
- A generic extension point can land here first so the fork can use it, for example a configurable path or a plugin hook. It must contain no proprietary data and no work-only logic.
- Never commit proprietary data: customer names, internal server names or URLs, tokens, credentials, or work-only eval cases. Anyone can read this repository.
- Do not name the work fork, its owner, or its URL in any file here.
- Run corpus refreshes here and commit them to `master` as usual. The fork receives them on its next sync.
- Avoid renaming or moving files the fork may import. A rename turns the next sync into a conflict. If a rename is necessary, say so in the commit message.

## Rules in the work fork

- Put new code, cases, profiles, and records under `work/`. Do not edit upstream-owned paths.
- If a work feature needs core behavior to change, decide where the change goes:
  - If the change contains no proprietary data or work-only logic, ask the user to make it in the upstream repository. The fork gets it on the next sync.
  - Otherwise, wrap the core from `work/`: import it, call it with different arguments, or subclass it. Do not patch the upstream file.
- Pass explicit paths so the core scripts write into `work/`:
  - `python -B scripts/promote-candidate.py ... --output work/evaluation/cases/regressions.jsonl`
  - `python -B scripts/evaluate.py --cases work/evaluation/cases/<file>.jsonl --profile work/evaluation/profiles/<file>.json`
- Store reviewed proprietary live observations in `work/live-observations/`, not in `BlackDuck SCA/verification/live-observations/`.
- Do not run or commit corpus refreshes in the fork. If a scrape runs here by mistake, discard its changes. Refreshes arrive from upstream.
- Never push to `upstream`, and never open a pull request or issue against `tonesjones/doc-search` from the fork. `git remote get-url --push upstream` must print `DISABLED`. If it does not, run the one-time setup below.

## Set up the fork once

Run these commands in the fork checkout:

```sh
git remote add upstream https://github.com/tonesjones/doc-search.git   # skip if it exists
git remote set-url --push upstream DISABLED
git config rerere.enabled true
```

`rerere` records how you resolved a conflict and reapplies that resolution if the same conflict appears again.

## Sync the fork from upstream

1. Fetch upstream:

   ```sh
   git fetch upstream
   ```

2. Create a sync branch from the fork's default branch:

   ```sh
   git switch -c sync/upstream-YYYY-MM-DD <default-branch>
   ```

3. Merge upstream:

   ```sh
   git merge upstream/master
   ```

4. If a path conflicts, resolve it by owner:
   - For an upstream-owned path, keep the upstream version with `git checkout --theirs -- <path>`. Then move the fork's change into `work/`, or ask the user to make it upstream.
   - A path under `work/` cannot conflict, because upstream never writes there. If one does, stop and ask the user.
5. Run the offline checks and the fork's own tests:

   ```sh
   python -B scripts/check-offline.py
   ```

6. Open a pull request from the sync branch into the default branch. Merge it with a merge commit. Do not squash or rebase it. A squash or rebase drops the link to `upstream/master`, so the next sync replays the same changes and conflicts again.

Do not rebase the fork's default branch onto `upstream/master`. The fork is many commits ahead, and a rebase rewrites all of them.

## Find drift that will cause conflicts

In the fork, list the upstream-owned files that the fork has changed:

```sh
git fetch upstream
git diff --stat upstream/master...HEAD -- . ':(exclude)work'
```

Each file in the output is a future conflict. Move the fork's change into `work/`, or ask the user to make the generic part upstream. When the command prints nothing, the fork is clean.

The fork can run the same command in CI and fail the build when it prints any file.

## Known gaps in upstream extension points

These upstream files hard-code shared paths. Fix them upstream with configurable paths before the fork depends on them. Until then, the fork wraps them from `work/` and does not patch them.

- `BlackDuck SCA/verification/live_observation.py` sets `CASE_FILES` to the two upstream case files. A fork record whose `related_cases` names a case in `work/` fails validation.
- `BlackDuck SCA/verification/verify.py` reads live observations only from `BlackDuck SCA/verification/live-observations/`. It does not see records in `work/live-observations/`.
- `scripts/promote-candidate.py` defaults `--output` to `evaluation/cases/sca-regressions.jsonl`. Without the flag, a promotion in the fork appends to a shared file.
