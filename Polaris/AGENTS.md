# Polaris Documentation Corpus

This repository is an offline, retrieval-friendly knowledge base for official Black Duck Polaris documentation. It converts official Fluid Topics documentation into small Markdown files so product questions can be answered locally.

## Source priority

1. `docs/**`, `index.md`, and `corpus-status.md` in this repository.
2. Official Black Duck documentation APIs, when content is missing or a refresh is requested.
3. General knowledge only when neither source covers the question; state the uncertainty.

Do not use third-party summaries as a product authority. Keep the current Black Duck Polaris Platform and its CI documentation separate from the legacy **Coverity on Polaris** product (`cov_polaris`); that legacy corpus is out of scope unless explicitly added later.

## Layout

```text
docs/platform/     Polaris Platform topics
sources/<product>/ toc.json, manifest.json
scripts/           registry, indexer, scraper, validator
```

Each topic has YAML front matter with title, source URL, content ID, product key, section, scrape time, and source-content hash. `manifest.json` is the work queue: `pending`, `done`, `skipped`, or `error`.

## Working rules

- Read `CHECKPOINT.md` first when resuming.
- Search local Markdown before fetching documentation.
- Do not hand-edit generated topic rows in `index.md`.
- Never re-fetch `done` topics except through `--refresh-changed` or an explicit refresh request.
- After scraping, run `python scripts/build-index.py --product all --hub` and update `CHECKPOINT.md` when a phase completes.
- Keep content granular: one official TOC topic per Markdown file.

## Commands

```powershell
python scripts/build-index.py --list-products
python scripts/build-index.py --product polaris-platform-latest --init
python scripts/scrape-pending.py --product polaris-platform-latest --section "Understand Polaris"
python scripts/scrape-pending.py --product polaris-platform-latest --all-pending
python scripts/scrape-pending.py --product all --refresh-changed
python scripts/scrape-pending.py --product all --refresh-all
python scripts/build-index.py --product all --hub
python scripts/validate-corpus.py
python scripts/smoke-retrieval.py
```

Polaris CI guidance is deliberately not duplicated here. Use the proven Bridge corpus in `C:\TestCode\BlackDuck SCA\docs\bridge\` and its `index-bridge.md` for Bridge CLI, CI platform, SARIF, and pull-request workflows. The registry requires a verified Fluid Topics map ID before `--init`; record it only after validating the official TOC endpoint.
