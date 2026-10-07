# Black Duck Code Sight Documentation Corpus

This repository is a **local knowledge base** of Black Duck Code Sight product documentation. Content is scraped from official Black Duck docs (Fluid Topics), then organized into Markdown so agents can answer product and usage questions from **files in this repo** instead of re-scraping the web each session.

## Purpose

- Capture Black Duck Code Sight documentation offline as Markdown.
- Maintain a product index (`index.md`) and progress hub (`corpus-status.md`).
- Split topics into **many smaller `.md` files** under `docs/` for retrieval-friendly chunks.
- Prefer **RAG over this corpus** when answering questions about Code Sight installation in Eclipse/IntelliJ/VS/VS Code, server authentication, viewing Coverity/SCA/Polaris/SRM issues in the IDE, rapid scans, preferences, and release notes.

## Source of truth

| Priority | Source | When to use |
|----------|--------|-------------|
| 1 | Markdown files in this repo (`docs/**`, `index.md`) | Default for all product/how-to questions |
| 2 | Official Code Sight docs via Fluid Topics **content API** (not SPA HTML) | Corpus missing, outdated, or user asks to refresh |
| 3 | General knowledge | Last resort; label uncertainty clearly |

Do **not** treat random blog posts or third-party summaries as authoritative when corpus or official docs cover the topic.

## Pinned documentation source

| Field | Value |
|-------|-------|
| Product | Black Duck Code Sight |
| Product key | `codesight-2026.9.0` |
| Version | **2026.9.0** |
| Map ID | `MbKAMeBG9Dkor~tl3lqBXg` |
| Help Center (browser SPA) | https://docs.blackduck.com/r/codesight/code-sight-documentation.html |
| TOC API | `GET https://docs.blackduck.com/api/khub/maps/MbKAMeBG9Dkor~tl3lqBXg/toc` |
| Content API | `GET https://docs.blackduck.com/api/khub/maps/MbKAMeBG9Dkor~tl3lqBXg/topics/{contentId}/content` |
| Topics | **233 official topics** under `docs/` (welcome, support-matrix, installing, authenticating, viewing-issues, signal-vscode-extension, coverity, black-duck-sca, polaris, software-risk-manager, standard-edition, preferences-troubleshooting, release-notes, general-information) |
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
    welcome/ support-matrix/ installing/ authenticating/ viewing-issues/
    signal-vscode-extension/ coverity/ black-duck-sca/ polaris/
    software-risk-manager/ standard-edition/ preferences-troubleshooting/
    release-notes/ general-information/
  sources/
    codesight-2026.9.0/
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
- After scraping: `python scripts/build-index.py --product codesight-2026.9.0 --hub`
- Re-pull TOC and merge statuses: `python scripts/build-index.py --product codesight-2026.9.0 --refresh-toc`
- On session start: read **`CHECKPOINT.md`**, then `PHASE-PLAN.md` / `corpus-status.md`, then filter the manifest for pending work.

### Topic file conventions

- One official TOC topic → one Markdown file at the manifest `localPath`.
- YAML front matter:

```yaml
---
title: "..."
source_url: "https://docs.blackduck.com/..."
content_id: "..."
version: "2026.9.0"
section: "..."
scraped_at: "ISO-8601"
---
```

## How to answer questions (RAG-first)

1. **Search this repo first** — `index.md` / `corpus-status.md`, then open relevant `docs/**/*.md` (grep / read).
2. **Route by topic:**
   - What Code Sight is / product overview → `docs/welcome/`
   - Supported languages, frameworks, IDEs, platforms, servers → `docs/support-matrix/`
   - Installing in Eclipse / IntelliJ / Visual Studio / VS Code → `docs/installing/`
   - Authenticating to SCA / Coverity / Polaris servers → `docs/authenticating/`
   - Local View / Team View, viewing issues → `docs/viewing-issues/`
   - Signal + Code Sight VS Code extension → `docs/signal-vscode-extension/`
   - Coverity SAST workflows → `docs/coverity/`
   - Black Duck SCA workflows → `docs/black-duck-sca/`
   - Polaris workflows → `docs/polaris/`
   - Software Risk Manager workflows → `docs/software-risk-manager/`
   - Standard Edition, rapid scan engines → `docs/standard-edition/`
   - Preference panels, troubleshooting → `docs/preferences-troubleshooting/`
   - Release notes, known issues → `docs/release-notes/`
   - Inclusivity, telemetry, proprietary statement → `docs/general-information/`
3. **Cite paths** when answering (e.g. `docs/installing/installing-code-sight-in-visual-studio-code.md`) so answers are verifiable.
4. **Quote or paraphrase carefully** — distinguish product facts from interpretation.
5. **If the corpus is silent or conflicting**, say so; offer to scrape pending topics or fetch official content.
6. **Do not invent** Code Sight install steps, IDE menu paths, authentication flows, or preference options.

## Scraping commands

```powershell
cd "C:\TestCode\Product Docs\CodeSight"
python scripts/build-index.py --list-products
python scripts/build-index.py --product codesight-2026.9.0 --init --hub
python scripts/scrape-pending.py --product codesight-2026.9.0 --section "Installing Code Sight"
python scripts/scrape-pending.py --product codesight-2026.9.0 --all-pending
python scripts/scrape-pending.py --product codesight-2026.9.0 --retry-errors
python scripts/build-index.py --product codesight-2026.9.0 --hub
python scripts/validate-corpus.py --product codesight-2026.9.0
python scripts/smoke-retrieval.py
```

See **`PHASE-PLAN.md`** for the recommended phase order.

## Agent behavior

- Optimize for **documentation quality and retrieval**, not application code unless scripts are requested.
- When the user asks how something works, answer from local Markdown first.
- When expanding coverage, scrape into `docs/`, flip manifest statuses, rebuild index, update checkpoint.
- On a new session without a clear user goal, open **`CHECKPOINT.md`** first.

## Related projects

Do not mix Code Sight docs into sibling trees, and do not scrape those maps here:

| Product | Path |
|---------|------|
| Black Duck SCA / Detect / Alert | `BlackDuck SCA` |
| Bridge CLI | `Bridge` |
| Coverity | `Coverity` |
| Polaris | `Polaris` |
| Black Duck Signal | `Signal` |

## Current navigation

The 2026.9.0 edition uses the 14 `docs/` sections listed above. Use `index.md` to resolve current topics. Old pages removed from the official TOC remain as historical files and must not be used as current guidance.
