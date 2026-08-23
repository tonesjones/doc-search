# Black Duck Documentation Skill Handoff

This folder is a local, retrieval-friendly mirror of Black Duck product documentation. It is intended to be portable to another machine and usable by a coding assistant— including Claude Code—without requiring a live documentation scrape for ordinary questions.

## Improvements already made

The previous optimization work changed this from a loose collection of downloaded pages into a maintainable offline knowledge base:

- **RAG-first answering:** assistants search the local Markdown corpus before using web search or general knowledge.
- **Product separation:** Black Duck SCA, Coverity, Polaris, Sigma, and Signal have separate roots, indexes, manifests, and agent guidance. This prevents similarly named products and workflows from being mixed together.
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

## How Claude Code should use this folder

1. Read the relevant product's `AGENTS.md` and `CHECKPOINT.md` before making changes or answering product questions.
2. Search that product's `docs/`, generated indexes, and `corpus-status.md` first.
3. Cite local Markdown paths in answers so claims are verifiable.
4. Do not invent UI paths, API endpoints, CLI flags, checker names, license names, or product properties.
5. If the local corpus is silent, say so clearly. Only then consult official Black Duck documentation or propose a refresh.
6. Treat generated indexes and status hubs as outputs. Update the manifest or source scripts, then regenerate them.
7. Preserve the pinned product versions and the documented out-of-scope decisions unless the user explicitly requests a new scrape or version.

## Product entry points

| Product | Folder | Start with |
|---|---|---|
| Black Duck SCA and companion tools | `BlackDuck SCA/` | `README.md`, `AGENTS.md`, `index.md` |
| Coverity | `Coverity/` | `README.md`, `AGENTS.md`, `index.md` |
| Polaris Platform | `Polaris/` | `README.md`, `AGENTS.md`, `index.md` |
| Sigma | `Sigma/` | `README.md`, `AGENTS.md`, `index.md` |
| Signal | `Signal/` | `README.md`, `AGENTS.md`, `index.md` |

For a Claude Code skill, use this root README as the high-level instruction and each product's `AGENTS.md` as the product-specific operating rules. Do not flatten the product folders into one undifferentiated index.

## Refresh principle

Use the scripts and commands documented in the relevant product README. Prefer a targeted refresh or retry over a full re-scrape. After a refresh, validate the corpus, rebuild generated indexes/status files, update the checkpoint, and review the resulting changes before sharing the folder.

## SCA evaluation and runtime POC

The current SCA baseline uses the installed production `bd` path; expected benchmark facts are never sent to it. Raw traces, results, runtime artifacts, and `.env.runtime` are gitignored.

```powershell
python -m unittest discover -s tests -v
python scripts/evaluate.py --cases evaluation/cases/sca-baseline.jsonl --adapter python scripts/codex_production_adapter.py --label "BLACK DUCK SCA PHASE 1 BASELINE" --output evaluation/results/sca-baseline.json --trace-output evaluation/traces/sca-baseline
python scripts/phase1-gate.py --report evaluation/results/sca-baseline.json
python scripts/validate-runtime.py --product blackduck-sca --all --output runtime/results/sca-runtime.json
python scripts/combined-evaluate.py
```

Provisioning is separately double-gated and restricted to the exact ownership-marked `Tony RAG` project:

```powershell
python scripts/sca-provision-test-project.py --allow-mutations --confirm-project "Tony RAG"
```

## Verified self-learning workflow (currently SCA-only)

This workflow is currently implemented for Black Duck SCA. It improves answers through evidence and human review rather than treating feedback as automatic truth:

1. Ask a product question through `/bd`.
2. Keep the production answer and trace. If it is correct, no change is required.
3. If a human identifies a wrong, hallucinated, outdated, or unnecessarily broad answer, capture the answer ID, question, critique, and trace as feedback.
4. Turn the feedback into a candidate correction and check it against authoritative local documentation and the applicable product version.
5. Have a human confirm the valid path and its intended scope.
6. Promote the confirmed, generalized behavior to a versioned regression outside the preserved baseline.
7. Apply the approved general guidance or retrieval adjustment, without creating a question-specific answer hack.
8. Rerun the exact question through the production path. The loop is complete only when the regression passes and the forbidden extra scope is absent.

Feedback does not automatically edit documentation, prompts, retrieval rules, or product guidance. Version conflicts, missing evidence, and uncertain answers remain reviewable. This is continuous verified learning with a human in the loop, not autonomous self-modification.

## Changes made in this session

- Added the SCA Phase 1 baseline, deterministic gate, production adapter, trace capture, and evaluation reports.
- Added the SCA runtime validation boundary with safe, read-only defaults and explicit mutation gates.
- Created the ownership-isolated `Tony RAG` project and test versions for shared-instance validation.
- Captured the C/C++ scan-scope correction: optional snippet matching is not part of the standard command unless requested or required by evidence.
- Added the verified feedback candidate, generalized regression, post-feedback production trace, and regression test.
- Updated SCA guidance to preserve requested scope and distinguish required steps from optional modes.

## Product-line roadmap

SCA is the first product line being brought to a working state. Once this workflow is stable, replicate the same evidence, human-review, and regression process product-by-product for Detect, Alert, Bridge, C/C++ Tool, Coverity, Polaris, Sigma, and Signal. Do not assume SCA behavior or flags transfer to another product without product- and version-specific evidence.
