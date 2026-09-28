# Black Duck Documentation Skill Handoff

This folder is a local, retrieval-friendly mirror of Black Duck product documentation. It works with coding agents without a live documentation scrape for ordinary questions.

## Supported answer workflow

Use the [supported workflow](docs/supported-workflow.md) for customer questions
and future evaluations. The merged router and the installed personal `bd` skill
are distinct profiles. The [DS-04 inventory](docs/ds-04-reconciliation.md)
records existing experimental work to reuse and its current limits.

## Verify Black Duck SCA offline

The root [router](SKILL.md) selects the [SCA skill](BlackDuck%20SCA/SKILL.md)
through `products.json`. SCA is the first product with an implemented verifier.
Other registered skill and verifier paths remain planned entrypoints.

From the repository root, run:

```powershell
python -B "BlackDuck SCA/verification/verify.py"
```

The command prints JSON matching `verification-report.schema.json`. It exits with
code 0 when all offline checks pass, or 1 on failure. The report covers corpus
integrity and selected index-to-topic retrieval checks. `PASS` applies to those
offline checks only. Live UI and API checks explicitly remain `NOT_RUN`.
Existing corpus warnings appear in `evidence`. No network or credentials are needed.

Run the registry and SCA report tests with `python -B -m unittest discover -s tests`.

## Evaluate SCA answers

Use the [DS-07 evaluation guide](docs/ds-07-evaluator.md) to validate the reviewed
case set, run the read-only checkout adapter, and capture revision-bound traces.
The evaluator contains 30 SCA baseline cases and six feedback regressions.

## Improvements already made

The previous optimization work changed this from a loose collection of downloaded pages into a maintainable offline knowledge base:

- **RAG-first answering:** assistants search the local Markdown corpus before using web search or general knowledge.
- **Product separation:** Black Duck SCA, Coverity, Polaris, Software Risk Manager, Sigma, and Signal have separate roots, indexes, manifests, and agent guidance. This prevents similarly named products and workflows from being mixed together.
- **Generated navigation:** each corpus has generated topic indexes and progress/status hubs. Index rows are derived from manifests and must not be hand-edited.
- **One topic per Markdown file:** official TOC topics are split into small, retrieval-friendly files instead of large scraped HTML documents.
- **Traceable source metadata:** topic files carry front matter such as title, source URL, content ID, product/version, section, scrape timestamp, and—in newer corpora—content hashes.
- **Reliable scraping architecture:** refreshes use the official Fluid Topics TOC/content APIs rather than the JavaScript SPA HTML shell.
- **Resumable work queues:** manifests track `pending`, `done`, `skipped`, and `error` topics. Interrupted or partial runs can resume without re-downloading completed work.
- **Safe refresh behavior:** TOC refreshes merge known statuses by content ID; changed-topic refreshes compare normalized content hashes and rewrite only files that actually changed.
- **Repair and retry support:** failed downloads, empty files, and newly added topics can be targeted independently instead of forcing a full rebuild.
- **Validation and smoke tests:** corpus validators check manifest, front matter, file, and hash consistency; retrieval smoke tests verify basic routing and discoverability.
- **Session continuity:** `AGENTS.md`, `CHECKPOINT.md`, and `corpus-status.md` preserve source priorities, scope decisions, progress, and next actions across machines and sessions.
- **Explicit scope boundaries:** intentionally omitted products, versions, locales, and legacy documentation are recorded so an assistant does not silently expand the corpus or scrape unrelated material.
- **Portable read path:** reading the existing corpus requires only the files; Python, dependencies, and network access are needed only for refresh, scrape, or validation operations.

## Product entry points

| Product | Folder | Start with |
|---|---|---|
| Black Duck SCA, Detect, Alert, and C/C++ Tool | `BlackDuck SCA/` | `README.md`, `AGENTS.md`, `CHECKPOINT.md`, `index.md` |
| Bridge | `Bridge/` | `README.md`, `AGENTS.md`, `CHECKPOINT.md`, `index.md` |
| Coverity | `Coverity/` | `README.md`, `AGENTS.md`, `index.md` |
| Polaris Platform | `Polaris/` | `README.md`, `AGENTS.md`, `index.md` |
| Software Risk Manager | `SRM/` | `README.md`, `AGENTS.md`, `index.md` |
| Sigma | `Sigma/` | `README.md`, `AGENTS.md`, `index.md` |
| Signal | `Signal/` | `README.md`, `AGENTS.md`, `index.md` |

## Use this repository with a coding agent

All coding agents use the same source and version rules.

1. Read [SKILL.md](SKILL.md) to select a product from `products.json`.
2. Read the selected product's `README.md`, `AGENTS.md`, and `CHECKPOINT.md`.
3. Search that product's `docs/`, generated index, and `corpus-status.md` before using the web or general knowledge.
4. Cite local Markdown paths in answers.
5. Do not invent UI paths, API endpoints, CLI flags, checker names, license names, or product properties.
6. If the local corpus is silent, say so. Then use official Black Duck documentation or ask before refreshing the corpus.
7. Update manifests and source scripts before generated indexes or status files. Preserve pinned versions and documented scope unless the user requests a change.

### Claude Code

Add this checkout to the Claude Code workspace. Start each product question by reading `SKILL.md` and the selected product's agent files. The root router and the Black Duck SCA product skill are the current agent instruction files.

### Codex

Open this checkout as the Codex workspace. In your first prompt, ask Codex to read `SKILL.md`, resolve the product through `products.json`, and then read the selected product's `README.md`, `AGENTS.md`, and `CHECKPOINT.md`. Codex follows `AGENTS.md` files automatically when they are in scope, but the explicit prompt ensures it loads the root router first.

### Grok

Attach or clone this checkout before asking a product question. Give Grok the same instruction as Codex because Grok does not automatically load this repository's guidance:

```text
Read SKILL.md. Resolve the product through products.json. Read the selected product's README.md, AGENTS.md, and CHECKPOINT.md. Search local Markdown and indexes before answering. Cite local file paths. Do not guess when the corpus is silent.
```

Poteto Mode is a personal agent-workflow style. It has no dedicated technical-documentation skill. Use the `technical-writing` skill for README and documentation edits.

## Refresh principle

Use the scripts and commands documented in the relevant product README. Prefer a targeted refresh or retry over a full re-scrape. After a refresh, validate the corpus, rebuild generated indexes/status files, update the checkpoint, and review the resulting changes before sharing the folder.
