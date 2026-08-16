# Black Duck Signal Documentation Corpus

This repository is a **local knowledge base** of Black Duck Signal product documentation. Content is scraped from official Black Duck docs (Fluid Topics), then organized into Markdown so agents can answer product and usage questions from **files in this repo** instead of re-scraping the web each session.

## Purpose

- Capture Black Duck Signal documentation offline as Markdown.
- Maintain a product index (`index.md`) and progress hub (`corpus-status.md`).
- Split topics into **many smaller `.md` files** under `docs/` for retrieval-friendly chunks.
- Prefer **RAG over this corpus** when answering questions about Signal overview, IDE and coding-assistant scans, CLI diff/file/full-project scans, SARIF, Polaris upload, the reference guide, AI/data-protection notes, and release notes.

## Source of truth

| Priority | Source | When to use |
|----------|--------|-------------|
| 1 | Markdown files in this repo (`docs/**`, `index.md`) | Default for all product/how-to questions |
| 2 | Official Signal docs via Fluid Topics **content API** (not SPA HTML) | Corpus missing, outdated, or user asks to refresh |
| 3 | General knowledge | Last resort; label uncertainty clearly |

Do **not** treat random blog posts or third-party summaries as authoritative when corpus or official docs cover the topic.

## Pinned documentation source

| Field | Value |
|-------|-------|
| Product | Black Duck Signal |
| Product key | `signal-latest` |
| Version | **latest** |
| Map ID | `xmDr3Yryk7OYDGb__OGKlg` |
| Help Center (browser SPA) | https://docs.blackduck.com/r/signal/black-duck-signal.html |
| TOC API | `GET https://docs.blackduck.com/api/khub/maps/xmDr3Yryk7OYDGb__OGKlg/toc` |
| Content API | `GET https://docs.blackduck.com/api/khub/maps/xmDr3Yryk7OYDGb__OGKlg/topics/{contentId}/content` |
| Topics | **17** under `docs/` (overview, scan-changes, scan-project, reference, ai-security, release-notes) |
| Index | `index.md` |
| Phased scrape plan | `PHASE-PLAN.md` |
| Session handoff | `CHECKPOINT.md` |

**Out of scope unless user reopens:** non-English locales; other Black Duck products.

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
    overview/ scan-changes/ scan-project/ reference/ ai-security/ release-notes/
  sources/
    signal-latest/
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
- After scraping: `python scripts/build-index.py --product signal-latest --hub`
- Re-pull TOC and merge statuses: `python scripts/build-index.py --product signal-latest --refresh-toc`
- On session start: read **`CHECKPOINT.md`**, then `PHASE-PLAN.md` / `corpus-status.md`, then filter the manifest for pending work.

### Topic file conventions

- One official TOC topic → one Markdown file at the manifest `localPath`.
- YAML front matter:

```yaml
---
title: "..."
source_url: "https://docs.blackduck.com/..."
content_id: "..."
version: "latest"
section: "..."
scraped_at: "ISO-8601"
---
```

## How to answer questions (RAG-first)

1. **Search this repo first** — `index.md` / `corpus-status.md`, then open relevant `docs/**/*.md` (grep / read).
2. **Route by topic:**
   - What Signal is / product overview → `docs/overview/`
   - Incremental / diff / file scans, IDE, Claude Code, Copilot, Code Sight → `docs/scan-changes/`
   - Full-project CLI, SARIF-only, send results to Polaris → `docs/scan-project/`
   - Flags, options, reference tables → `docs/reference/`
   - AI / data protection / trust → `docs/ai-security/`
   - Release notes → `docs/release-notes/`
3. **Cite paths** when answering (e.g. `docs/scan-changes/from-the-command-line.md`) so answers are verifiable.
4. **Quote or paraphrase carefully** — distinguish product facts from interpretation.
5. **If the corpus is silent or conflicting**, say so; offer to scrape pending topics or fetch official content.
6. **Do not invent** Signal UI paths, CLI flags, coding-assistant setup steps, or Polaris upload options.

## Scraping commands

```powershell
cd "C:\TestCode\Product Docs\Signal"
python scripts/build-index.py --list-products
python scripts/build-index.py --product signal-latest --init --hub
python scripts/scrape-pending.py --product signal-latest --section "Overview of Black Duck Signal"
python scripts/scrape-pending.py --product signal-latest --all-pending
python scripts/scrape-pending.py --product signal-latest --retry-errors
python scripts/build-index.py --product signal-latest --hub
python scripts/validate-corpus.py --product signal-latest
python scripts/smoke-retrieval.py
```

See **`PHASE-PLAN.md`** for the recommended phase order.

## Agent behavior

- Optimize for **documentation quality and retrieval**, not application code unless scripts are requested.
- When the user asks how something works, answer from local Markdown first.
- When expanding coverage, scrape into `docs/`, flip manifest statuses, rebuild index, update checkpoint.
- On a new session without a clear user goal, open **`CHECKPOINT.md`** first.

## Related projects

Do not mix Signal docs into sibling trees, and do not scrape those maps here:

| Product | Path |
|---------|------|
| Black Duck SCA / Detect / Alert / Bridge | `C:\TestCode\Product Docs\BlackDuck SCA` |
| Coverity | `C:\TestCode\Product Docs\Coverity` |
| Polaris | `C:\TestCode\Product Docs\Polaris` |
