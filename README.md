# Black Duck documentation search

This repository contains local, retrieval-ready copies of Black Duck product documentation. Coding agents can answer ordinary product questions from the Markdown corpus without scraping the live documentation site.

Each product has its own corpus, index, source metadata, and agent guidance. Some products also have skills, evaluation cases, or offline verification.

## Supported workflow

Use the [supported workflow](docs/supported-workflow.md) for customer questions and evaluations.

The root [router](SKILL.md) uses `products.json` to select registered products. The installed personal `bd` skill and the repository router are separate profiles.

The [DS-04 inventory](docs/ds-04-reconciliation.md) records experimental work that may be reused and its known limits.

## Product entry points

| Product | Folder | Status | Start with |
|---|---|---|---|
| Black Duck SCA, Detect, Alert, and C/C++ Tool | `BlackDuck SCA/` | Corpus, skill, and offline verifier | `README.md`, `AGENTS.md`, `CHECKPOINT.md`, `index.md` |
| Code Sight | `CodeSight/` | 2026.9.0 corpus complete, 233/233 topics | `README.md`, `AGENTS.md`, `CHECKPOINT.md`, `index.md` |
| Bridge | `Bridge/` | Documentation corpus | `README.md`, `AGENTS.md`, `CHECKPOINT.md`, `index.md` |
| Coverity | `Coverity/` | Documentation corpus | `README.md`, `AGENTS.md`, `index.md` |
| Polaris Platform | `Polaris/` | Documentation corpus | `README.md`, `AGENTS.md`, `index.md` |
| Software Risk Manager | `SRM/` | Documentation corpus | `README.md`, `AGENTS.md`, `index.md` |
| Sigma | `Sigma/` | Documentation corpus | `README.md`, `AGENTS.md`, `index.md` |
| Signal | `Signal/` | Documentation corpus | `README.md`, `AGENTS.md`, `index.md` |

## Code Sight 2026.9.0

`CodeSight/` contains the complete English Black Duck Code Sight 2026.9.0 documentation corpus.

The corpus contains 233 official topics across these sections:

- welcome and general information
- support matrices
- installation
- authentication
- issue viewing
- Signal and Visual Studio Code integration
- Coverity
- Black Duck SCA
- Polaris
- Software Risk Manager
- Standard Edition
- preferences and troubleshooting
- release notes

The Code Sight folder also contains its TOC and manifest data, generated indexes, scrape scripts, corpus validation, retrieval smoke tests, and session handoff files.

The initial corpus is complete:

```text
233/233 topics
0 pending
0 skipped
0 errors
```

Run the Code Sight checks from `CodeSight/`:

```powershell
python scripts/validate-corpus.py --product codesight-2026.9.0
python scripts/smoke-retrieval.py
```

Both checks pass for the initial 2026.9.0 corpus.

Code Sight is not yet registered with the root router. `CodeSight/SKILL.md` and a Code Sight verification entry point do not exist in this corpus update. Until those are added, enter the corpus through `CodeSight/README.md`, `CodeSight/AGENTS.md`, and `CodeSight/index.md`.

## Verify Black Duck SCA offline

Black Duck SCA is registered with the root router and has an implemented offline verifier.

From the repository root, run:

```powershell
python -B "BlackDuck SCA/verification/verify.py"
```

The command prints JSON that matches `verification-report.schema.json`.

It exits with code `0` when all offline checks pass and `1` when a check fails. The report checks corpus integrity and selected index-to-topic retrieval cases.

A `PASS` result applies only to the offline checks. Live UI and API checks remain `NOT_RUN`. The verifier does not require network access or credentials.

Run the registry and SCA report tests with:

```powershell
python -B -m unittest discover -s tests
```

## Evaluate SCA answers

Use the [DS-07 evaluation guide](docs/ds-07-evaluator.md) for the reviewed SCA case set, read-only checkout adapter, and revision-bound traces.

The evaluator contains 30 baseline cases and six feedback regressions.

## Repository structure

The documentation corpora follow the same basic rules:

- Search local Markdown before using web search or model knowledge.
- Keep products in separate folders to prevent cross-product retrieval.
- Store one official documentation topic per Markdown file.
- Generate topic indexes and status files from manifests instead of editing them by hand.
- Preserve source metadata such as the title, source URL, content ID, product version, section, and scrape timestamp.
- Use content hashes where the corpus supports them.
- Retrieve TOCs and topic content through the official Fluid Topics APIs instead of scraping the JavaScript application shell.
- Track `pending`, `done`, `skipped`, and `error` states in manifests so interrupted scrapes can resume.
- Refresh only new, changed, pending, or failed topics when possible.
- Validate the corpus after a scrape or refresh.
- Keep `AGENTS.md`, `CHECKPOINT.md`, and related status files up to date so another agent can resume the work.

Reading an existing corpus requires only the repository files. Python and network access are needed for scraping, refreshing, or validation.

## Use the repository with an agent

For a product registered in the root router:

1. Read `SKILL.md`.
2. Resolve the product through `products.json`.
3. Read the product's `README.md`, `AGENTS.md`, and `CHECKPOINT.md`.
4. Search the product's `docs/`, `index.md`, and `corpus-status.md`.
5. Cite the local Markdown files that support the answer.
6. Do not invent UI paths, API endpoints, CLI flags, checker names, license names, or product behavior.
7. If the corpus does not answer the question, say so before using another source.

For Code Sight, start directly in the product folder until root routing is added:

```text
Read CodeSight/README.md, CodeSight/AGENTS.md, and CodeSight/CHECKPOINT.md.
Search CodeSight/index.md and CodeSight/docs/ before answering.
Use the local Code Sight 2026.9.0 documentation as the primary source.
Cite the supporting Markdown files.
Do not guess when the corpus is silent.
```

### Claude Code

Add the repository to the Claude Code workspace.

For registered products, start with `SKILL.md`. For Code Sight, start with the files under `CodeSight/`.

### Codex

Open the repository as the Codex workspace.

For registered products, use:

```text
Read SKILL.md. Resolve the product through products.json. Read the selected product's README.md, AGENTS.md, and CHECKPOINT.md. Search local Markdown and indexes before answering. Cite local file paths. Do not guess when the corpus is silent.
```

Codex follows `AGENTS.md` files when they are in scope. Resolving the product first reduces cross-product retrieval.

For Code Sight, start directly in `CodeSight/`.

### Grok

Attach or clone the repository before asking product questions. Use the same source-selection instructions as Codex.

## Refresh a corpus

Prefer a targeted refresh over a full scrape.

After a refresh:

1. Update or merge the official TOC.
2. Scrape the required new, changed, pending, or failed topics.
3. Validate the corpus.
4. Rebuild generated indexes and status files.
5. Update the checkpoint.
6. Review the Git diff before committing.

Keep the documented product version and scope unless the change is an intentional version upgrade or scope expansion.
