# Black Duck Sigma Documentation Corpus

This repository is a **local knowledge base** of Black Duck Sigma (Rapid Scan Static) product documentation. Content is scraped from official Black Duck docs (Fluid Topics), then organized into Markdown so agents can answer product and usage questions from **files in this repo** instead of re-scraping the web each session.

## Purpose

- Capture Black Duck Sigma documentation offline as Markdown.
- Maintain a product index (`index.md`) and progress hub (`corpus-status.md`).
- Split topics into **many smaller `.md` files** under `docs/` for retrieval-friendly chunks.
- Prefer **RAG over this corpus** when answering questions about Sigma overview, download (binary / Docker), configuration, AI-augmented SAST plug-in, Jenkins / CI/CD, quality-gate policies, CLI commands, support matrix, checkers, and release notes.

## Source of truth

| Priority | Source | When to use |
|----------|--------|-------------|
| 1 | Markdown files in this repo (`docs/**`, `index.md`) | Default for all product/how-to questions |
| 2 | Official Sigma docs via Fluid Topics **content API** (not SPA HTML) | Corpus missing, outdated, or user asks to refresh |
| 3 | General knowledge | Last resort; label uncertainty clearly |

Do **not** treat random blog posts or third-party summaries as authoritative when corpus or official docs cover the topic.

## Pinned documentation source

| Field | Value |
|-------|-------|
| Product | Sigma Documentation (Rapid Scan Static) |
| Product key | `sigma-2026.9.1` |
| Version | **2026.9.1** |
| Map ID | `HDJ_IfD4RK593mgPPhyrnw` |
| Help Center (browser SPA) | https://docs.blackduck.com/r/sigma/2026.9.1/sigma-documentation/ |
| TOC API | `GET https://docs.blackduck.com/api/khub/maps/HDJ_IfD4RK593mgPPhyrnw/toc` |
| Content API | `GET https://docs.blackduck.com/api/khub/maps/HDJ_IfD4RK593mgPPhyrnw/topics/{contentId}/content` |
| Topics | **59** under `docs/sigma-2026.9.1/sigma-user-guide/` |
| Index | `index.md` |
| Phased scrape plan | `PHASE-PLAN.md` |
| Session handoff | `CHECKPOINT.md` |

**Out of scope unless user reopens:** older Sigma versions (2026.7.0, 2026.6.1); the mutable `latest` map; non-English locales; other Black Duck products.

The **Sigma Checkers** and standalone **Release Notes** topics in this map are short pointer pages. They link to Fluid Topics origin IDs (`sigma_checker_latest-en`, `sigma_release_notes`) that are **not** registered book maps, so the full checker catalog and detailed RN history are not in `docs/`. Say so if a question needs those.

The public site is a **JavaScript SPA** (Fluid Topics). A plain page fetch only returns "Loading application...". **Always use the TOC/content APIs** for structure and bodies.

## Corpus layout

```
/
  README.md                 # How to use a shared copy; how to refresh
  AGENTS.md                 # This file — agent instructions
  CHECKPOINT.md             # Session handoff: where we left off, next steps
  PHASE-PLAN.md             # Phased scrape plan
  corpus-status.md          # Progress hub (generated)
  index.md                  # Full TOC catalog (generated; do not hand-edit topic rows)
  requirements.txt
  docs/
    user-guide/             # Introducing, download, config, CI/CD, CLI, support, checkers
  sources/
    sigma-2026.9.1/
      toc.json
      manifest.json
  scripts/
    products.py             # Product/map registry
    build-index.py          # Init TOC + regenerate indexes
    scrape-pending.py       # Scrape pending topics
    validate-corpus.py
    smoke-retrieval.py
    build-index.ps1
```

### Progress tracking

- Manifest topic `status`: `pending` | `done` | `skipped` | `error`.
- Product index is generated from the manifest. Do not hand-edit topic rows.
- **`CHECKPOINT.md`** records the last completed work and next steps.
- Scrape only `pending` (retry `error`). Never re-fetch `done` unless the user asks to refresh.
- After scraping: `python scripts/build-index.py --product sigma-2026.9.1 --hub`
- Re-pull TOC and merge statuses: `python scripts/build-index.py --product sigma-2026.9.1 --refresh-toc`
- On session start: read **`CHECKPOINT.md`**, then `PHASE-PLAN.md` / `corpus-status.md`, then filter the manifest for pending work.

### Topic file conventions

- One official TOC topic → one Markdown file at the manifest `localPath`.
- YAML front matter:

```yaml
---
title: "..."
source_url: "https://docs.blackduck.com/..."
content_id: "..."
version: "2026.9.1"
section: "..."
scraped_at: "ISO-8601"
---
```

## How to answer questions (RAG-first)

1. **Search this repo first** — `index.md` / `corpus-status.md`, then open relevant `docs/**/*.md` (grep / read).
2. **Route by topic:**
   - What Sigma is / Rapid Scan Static overview → `docs/sigma-2026.9.1/sigma-user-guide/introducing-sigma.md`
   - Binary / Docker download → `docs/sigma-2026.9.1/sigma-user-guide/downloading-sigma/`
   - Config methods, options, output, `coverity.yml`, `.sigma-config.yml`, env vars, AI checker plug-in → `docs/sigma-2026.9.1/sigma-user-guide/configuring-sigma/`
   - Jenkins plugin, freestyle/pipeline, quality-gate policies → `docs/sigma-2026.9.1/sigma-user-guide/running-sigma-in-ci-cd/`
   - `sigma` CLI and subcommands (`analyze`, `checkers`, `config`, `docs`, `explain`, `metadata`) → `docs/sigma-2026.9.1/sigma-user-guide/command-reference/`
   - Languages, OS, CI systems, hardware → `docs/sigma-2026.9.1/sigma-user-guide/sigma-support-matrix/`
   - Release notes → `docs/sigma-2026.9.1/sigma-user-guide/release-notes.md`
   - Checker catalog → `docs/sigma-2026.9.1/sigma-user-guide/sigma-checkers.md`
3. **Cite paths** when answering (e.g. `docs/sigma-2026.9.1/sigma-user-guide/command-reference/the-analyze-subcommand.md`) so answers are verifiable.
4. **Quote or paraphrase carefully** — distinguish product facts from interpretation.
5. **If the corpus is silent or conflicting**, say so; offer to scrape pending topics or fetch official content.
6. **Do not invent** Sigma CLI flags, Jenkins plugin steps, policy YAML keys, environment variable names, or checker IDs.

## Scraping commands

```powershell
cd "C:\TestCode\Product Docs\Sigma"
python scripts/build-index.py --list-products
python scripts/build-index.py --product sigma-2026.9.1 --init --hub
python scripts/scrape-pending.py --product sigma-2026.9.1 --path-contains "Introducing Sigma"
python scripts/scrape-pending.py --product sigma-2026.9.1 --all-pending
python scripts/scrape-pending.py --product sigma-2026.9.1 --retry-errors
python scripts/build-index.py --product sigma-2026.9.1 --hub
python scripts/validate-corpus.py --product sigma-2026.9.1
python scripts/smoke-retrieval.py
```

See **`PHASE-PLAN.md`** for the recommended phase order.

## Agent behavior

- Optimize for **documentation quality and retrieval**, not application code unless scripts are requested.
- When the user asks how something works, answer from local Markdown first.
- When expanding coverage, scrape into `docs/`, flip manifest statuses, rebuild index, update checkpoint.
- On a new session without a clear user goal, open **`CHECKPOINT.md`** first.

## Related projects

Do not mix Sigma docs into sibling trees, and do not scrape those maps here:

| Product | Path |
|---------|------|
| Black Duck SCA / Detect / Alert | `C:\TestCode\Product Docs\BlackDuck SCA` |
| Bridge CLI | `C:\TestCode\Product Docs\Bridge` |
| Coverity | `C:\TestCode\Product Docs\Coverity` |
| Polaris | `C:\TestCode\Product Docs\Polaris` |
| Signal | `C:\TestCode\Product Docs\Signal` |

## Version history

Unversioned questions use 2026.9.1 through `index.md`. The 2026.8.0 snapshot remains unchanged at `index-sigma-2026.8.0.md`. Use the historical catalog only for that version or a comparison.
