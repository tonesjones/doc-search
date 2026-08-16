# Coverity Documentation Corpus

This repository is a **local knowledge base** of Coverity product documentation. Content is scraped from official Black Duck / Coverity docs (Fluid Topics), then organized into Markdown so agents can answer product and usage questions from **files in this repo** instead of re-scraping the web each session.

## Purpose

- Capture Coverity documentation offline as Markdown.
- Maintain a product index (`index.md`) and progress hub (`corpus-status.md`).
- Split topics into **many smaller `.md` files** under `docs/` for retrieval-friendly chunks.
- Prefer **RAG over this corpus** when answering questions about Coverity Connect, Analysis, CLI/Desktop, APIs, cloud deployment, checkers, and operations.

## Source of truth

| Priority | Source | When to use |
|----------|--------|-------------|
| 1 | Markdown files in this repo (`docs/**`, `index.md`) | Default for all product/how-to questions |
| 2 | Official Coverity docs via Fluid Topics **content API** (not SPA HTML) | Corpus missing, outdated, or user asks to refresh |
| 3 | General knowledge | Last resort; label uncertainty clearly |

Do **not** treat random blog posts or third-party summaries as authoritative when corpus or official docs cover the topic.

## Pinned documentation source

| Field | Value |
|-------|-------|
| Product | Coverity Documentation |
| Product key | `coverity-2026.6` |
| Version | **2026.6** |
| Map ID | `Ul9eg_yUOJh8gKU4cs1xrg` |
| Help Center (browser SPA) | https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/ |
| TOC API | `GET https://docs.blackduck.com/api/khub/maps/Ul9eg_yUOJh8gKU4cs1xrg/toc` |
| Content API | `GET https://docs.blackduck.com/api/khub/maps/Ul9eg_yUOJh8gKU4cs1xrg/topics/{contentId}/content` |
| Topics | **~4,443** under `docs/` (overview, connect, analysis, …) |
| Index | `index.md` |
| Phased scrape plan | `PHASE-PLAN.md` |
| Session handoff | `CHECKPOINT.md` |

**Out of scope unless user reopens:** Coverity on Polaris; non-English locales; older Coverity year versions.

The public site is a **JavaScript SPA** (Fluid Topics). A plain page fetch only returns "Loading application...". **Always use the TOC/content APIs** for structure and bodies.

## Corpus layout

```
/
  README.md                 # How to use a shared copy; how to refresh or scrape a new version
  AGENTS.md                 # This file — agent instructions
  CHECKPOINT.md             # Session handoff: where we left off, next steps
  PHASE-PLAN.md             # Phased scrape plan (1–8)
  corpus-status.md          # Progress hub (generated)
  index.md                  # Full TOC catalog (generated; do not hand-edit topic rows)
  requirements.txt
  docs/
    overview/ connect/ analysis/ clients-plugins/ connect-apis/
    cloud-native/ checkers/ release-notes/ glossary/ legal/ misc/
  sources/
    coverity-2026.6/
      toc.json
      manifest.json
  scripts/
    products.py             # Product/map registry
    build-index.py          # Init TOC + regenerate indexes
    scrape-pending.py       # Scrape pending topics
    build-index.ps1
```

### Progress tracking

- Manifest topic `status`: `pending` | `done` | `skipped` | `error`.
- Product index is generated from the manifest. Do not hand-edit topic rows.
- **`CHECKPOINT.md`** records the last completed phase and next steps.
- Scrape only `pending` (retry `error`). Never re-fetch `done` unless the user asks to refresh.
- After scraping: `python scripts/build-index.py --product coverity-2026.6 --hub`
- Re-pull TOC and merge statuses: `python scripts/build-index.py --product coverity-2026.6 --refresh-toc`
- On session start: read **`CHECKPOINT.md`**, then `PHASE-PLAN.md` / `corpus-status.md`, then filter the manifest for pending work.

### Topic file conventions

- One official TOC topic → one Markdown file at the manifest `localPath`.
- YAML front matter:

```yaml
---
title: "..."
source_url: "https://docs.blackduck.com/..."
content_id: "..."
version: "2026.6"
section: "..."
scraped_at: "ISO-8601"
---
```

## How to answer questions (RAG-first)

1. **Search this repo first** — `index.md` / `corpus-status.md`, then open relevant `docs/**/*.md` (grep / read).
2. **Cite paths** when answering (e.g. `docs/connect/...`) so answers are verifiable.
3. **Quote or paraphrase carefully** — distinguish product facts from interpretation.
4. **If the corpus is silent or conflicting**, say so; offer to scrape the relevant phase or fetch official content.
5. **Do not invent** Coverity UI paths, checker names, CLI flags, or API endpoints.

## Scraping commands

```powershell
cd C:\TestCode\Coverity
python scripts/build-index.py --list-products
python scripts/build-index.py --product coverity-2026.6 --init --hub
python scripts/scrape-pending.py --product coverity-2026.6 --section "Coverity overview"
python scripts/scrape-pending.py --product coverity-2026.6 --section "Coverity Analysis" --exclude-path "Customization guides"
python scripts/scrape-pending.py --product coverity-2026.6 --all-pending
python scripts/scrape-pending.py --product coverity-2026.6 --retry-errors
python scripts/build-index.py --product coverity-2026.6 --hub
```

See **`PHASE-PLAN.md`** for the recommended phase order.

## Agent behavior

- Optimize for **documentation quality and retrieval**, not application code unless scripts are requested.
- When the user asks how something works, answer from local Markdown first.
- When expanding coverage, scrape into `docs/`, flip manifest statuses, rebuild index, update checkpoint.
- On a new session without a clear user goal, open **`CHECKPOINT.md`** first.

## Related project

Black Duck SCA / Detect / Alert / Bridge corpus lives separately at `C:\TestCode\BlackDuck SCA`. Do not mix Coverity docs into that tree.
