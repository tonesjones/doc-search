# Session checkpoint — Polaris corpus

**Last updated:** 2026-08-12  
**Status:** Complete for current scope — use the local corpus for Polaris Platform questions.  
**Corpus:** Black Duck Polaris Platform `latest` — **182/182 topics complete**, zero errors.

## Next action

1. Answer Polaris Platform questions from `docs/platform/**`, `index.md`, and `index-polaris-platform-latest.md`.
2. Route Bridge CLI and CI questions to `C:\TestCode\BlackDuck SCA\docs\bridge\` and `index-bridge.md`.
3. Refresh changed topics with `python scripts/scrape-pending.py --product all --refresh-changed`.
4. After a converter change, rewrite all pages with `--refresh-all`, then `python scripts/build-index.py --product all --hub`.

## Scope

- In scope: current Polaris Platform documentation.
- Reused externally: Polaris CI material from the complete Bridge corpus at `C:\TestCode\BlackDuck SCA`.
- Out of scope: legacy **Coverity on Polaris** (`cov_polaris`), non-English content, and unrelated shared Bridge documentation.

## Durable project memory

- `AGENTS.md` — standing corpus and retrieval rules
- `PHASE-PLAN.md` — execution order
- `sources/*/manifest.json` — resumable work queues after initialization
- `corpus-status.md` — generated progress hub

## Source snapshot

- Map ID: `5MMaMfDebQ2sCji2eI3ezg`
- Official book: Black Duck Polaris Platform
- TOC snapshot: 2026-08-12
- Completion: 182/182 Markdown topics, 0 errors
