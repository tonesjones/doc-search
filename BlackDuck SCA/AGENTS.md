# Black Duck SCA Documentation Corpus

This repository is a **local knowledge base** of Black Duck product documentation (SCA server/UI plus companion clients). Content is scraped from official docs, then organized into Markdown so agents can answer product and usage questions from **files in this repo** instead of re-scraping the web each session.

## Purpose

- Capture Black Duck documentation offline as Markdown.
- Maintain **product indexes** (`index.md`, `index-detect.md`, …) and a multi-product hub (`corpus-status.md`).
- Split topics into **many smaller `.md` files** under `docs/` for retrieval-friendly chunks.
- Prefer **RAG over this corpus** when answering questions about Black Duck SCA, Detect, Alert, Bridge, features, setup, workflows, policy, integrations, APIs, and operations.

## Source of truth

| Priority | Source | When to use |
|----------|--------|-------------|
| 1 | Markdown files in this repo (`docs/**`, product indexes) | Default for all product/how-to questions |
| 2 | Official Black Duck docs via Fluid Topics **content API** (not SPA HTML) | Corpus missing, outdated, or user asks to refresh |
| 3 | General knowledge | Last resort; label uncertainty clearly |

Do **not** treat random blog posts or third-party summaries as authoritative when corpus or official docs cover the topic.

## Pinned documentation sources

### Phase 1 — SCA server/UI (done)

| Field | Value |
|-------|-------|
| Product map | Black Duck Documentation (SCA server/UI) |
| Product key | `blackduck-2026.7` |
| Version | **2026.7** |
| Map ID | `1WqD3iF0wWDzpOGfy2mr8Q` |
| Help Center (browser SPA) | https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/black-duck-sca-help-center.html |
| TOC API | `GET https://docs.blackduck.com/api/khub/maps/1WqD3iF0wWDzpOGfy2mr8Q/toc` |
| Content API | `GET https://docs.blackduck.com/api/khub/maps/1WqD3iF0wWDzpOGfy2mr8Q/topics/{contentId}/content` |
| Topics | **941** under `docs/help-center/`, `docs/api/`, install, architecture, release-notes, etc. |
| Index | `index.md` |

### Phase 2 — companions (core done)

| Product | Key | Version | Map ID | Topics | Docs | Index |
|---------|-----|---------|--------|-------:|------|-------|
| Black Duck Detect | `detect-11.5.1` | **11.5.1** | `bMVbOgKqSRm_N11~2Mv5gg` | **206** | `docs/detect/` | `index-detect.md` |
| Black Duck Alert | `alert-8.4.0` | **8.4.0** | `QEB0e_qPG~BdIwQfv5eDZQ` | **45** | `docs/alert/` | `index-alert.md` |
| Bridge CLI | `bridge-latest` | **latest** | `ilBVZr_kR5v3KVjK1p~wbw` | **174** | `docs/bridge/` | `index-bridge.md` |
| Black Duck C/CPP Tool | `c-cpp-tool-latest` | **latest** | `2GUQEgoyKxsQAcOtWsqdDA` | **14** (6 Tools siblings skipped) | `docs/c-cpp-tool/` | `index-c-cpp-tool.md` |
| Air-gapped KnowledgeBase | `airgap-kb-latest` | latest | `YsDtm_HKwGM6efkx~2HVvQ` | ~15 **deferred** (not scraped; not needed for current use) | — | — |

**Sibling corpora** (do not scrape into this SCA tree):

| Product | Path |
|---------|------|
| Coverity | `C:\TestCode\Product Docs\Coverity` |
| Polaris | `C:\TestCode\Product Docs\Polaris` |

**Intentionally not scraped yet** (user: not needed right now): Air-gapped KB; remainder of Black Duck Tools (KB Vulnerability Feed Server); BDBA; Artifactory; Code Sight; Defensics; Seeker; Sigma; Signal; SRM; Portal; older SCA versions; non-English locales. See **`CHECKPOINT.md`**. Do not scrape these unless the user reopens scope.

Hub progress table: **`corpus-status.md`**. Session handoff: **`CHECKPOINT.md`**.  
**Scrape status:** core scope complete (**1,380** topics). Prefer answering from local Markdown; no pending required scrape work.

The public site is a **JavaScript SPA** (Fluid Topics). A plain page fetch only returns "Loading application...". **Always use the TOC/content APIs** for structure and bodies.

**Content API pattern (all maps):**

```
GET https://docs.blackduck.com/api/khub/maps/{mapId}/toc
GET https://docs.blackduck.com/api/khub/maps/{mapId}/topics/{contentId}/content
```

## Corpus layout

```
/
  AGENTS.md                      # This file - agent instructions
  CHECKPOINT.md                  # Session handoff: where we left off, next steps
  corpus-status.md               # Multi-product progress hub (generated)
  index.md                       # SCA 2026.7 catalog (do not hand-edit topic rows)
  index-detect.md                # Detect catalog
  index-alert.md                 # Alert catalog
  index-bridge.md                # Bridge catalog
  index-c-cpp-tool.md            # C/CPP Tool catalog
  docs/
    help-center/ … release-notes/   # Phase 1 SCA section roots
    detect/                         # Phase 2
    alert/
    bridge/
    c-cpp-tool/
  sources/
    blackduck-2026.7/            # toc.json + manifest.json
    detect-11.5.1/
    alert-8.4.0/
    bridge-latest/
    c-cpp-tool-latest/
  scripts/
    products.py                  # Product/map registry
    build-index.py               # Init TOC + regenerate indexes (--product)
    scrape-pending.py            # Scrape pending topics (--product)
    build-index.ps1              # PowerShell wrapper
```

### Progress tracking (multi-session)

- Each map has **`sources/<product-key>/manifest.json`**. Topic `status`: `pending` | `done` | `skipped` | `error`.
- Product indexes are generated from manifests. Do not hand-edit topic rows.
- **`CHECKPOINT.md`** records the last completed work and next steps.
- Scrape only `pending` (retry `error`). Never re-fetch `done` unless the user asks to refresh a page or version.
- After scraping: `python scripts/build-index.py --product <key> --hub`
- Re-pull TOC and merge statuses: `python scripts/build-index.py --product <key> --refresh-toc`
- List products: `python scripts/build-index.py --list-products`
- On session start: read **`CHECKPOINT.md`**, then `corpus-status.md` / product indexes, then filter manifests for pending work.

### Index conventions

- Generated catalog of every TOC node with planned `docs/` path and status mark:
  - `[ ]` pending · `[x]` done · `[-]` skipped · `[!]` error
- Prefer relative links to topic files.
- Keep indexes as a **map**, not a dump of full article bodies.
- Refresh via `python scripts/build-index.py --product <key>`.

### Topic file conventions

- One official TOC topic → one Markdown file at the manifest `localPath`.
- Start each file with YAML front matter when possible:

```yaml
---
title: "..."
source_url: "https://docs.blackduck.com/..."
content_id: "..."
version: "2026.7"   # or product pin e.g. 11.5.1
section: "..."
scraped_at: "ISO-8601"
---
```

- Use clear `##` / `###` headings; keep tables, lists, CLI flags, and code accurate.
- Cross-link related chunks with relative Markdown links when useful.
- If content is version-specific, keep the pinned version visible in front matter.

### Chunk size guidance

- Default: **one API topic = one file** (already split by Black Duck's DITA map).
- Only sub-split further if a single topic is huge and mixes unrelated workflows.
- Do not create empty stubs; leave unscraped topics as `pending` in the manifest only.

## How to answer questions (RAG-first)

1. **Search this repo first** — `corpus-status.md` / product indexes, then open relevant `docs/**/*.md` (grep / read).
2. **Route by product:**
   - SCA server/UI, BOM, policy, install, reporting → `docs/help-center/`, install, architecture, `index.md`
   - Detect client, detectors, properties, scripts → `docs/detect/`, `index-detect.md`
   - Alert channels / providers → `docs/alert/`, `index-alert.md`
   - Bridge CLI / CI security scan plugins → `docs/bridge/`, `index-bridge.md`
   - C/C++ BOM via blackduck-c-cpp / Coverity Build Capture → `docs/c-cpp-tool/`, `index-c-cpp-tool.md`
3. **Cite paths** when answering (e.g. `docs/detect/planning-and-running-detect.md`) so answers are verifiable.
4. **Quote or paraphrase carefully** — distinguish product facts from interpretation.
5. **If the corpus is silent or conflicting**, say so; offer to scrape pending topics (e.g. optional air-gap) or fetch official content.
6. **Do not invent** Black Duck UI paths, license names, API endpoints, or Detect properties.
7. **Preserve the requested scope.** Distinguish required behavior from documented recommendations and optional capabilities. For a standard or default workflow, keep the primary steps and executable command to what is necessary. Do not add optional scan types, modes, flags, reports, or hardening unless the user requests them or the stated environment/use case requires them. If an optional capability is genuinely useful, label it separately and do not silently add it to the main command.
8. **Learn through verified regressions.** When a user explicitly reports that a traced `/bd` answer is wrong, hallucinated, outdated, or unnecessarily expanded, recover the answer trace and capture the report as a candidate. Verify the correction against authoritative, version-matched documentation. After user/source verification, add a generalized regression outside the preserved baseline. Do not treat unverified feedback as truth or automatically edit product documentation. Record any approved guidance change separately from the original baseline and rerun the regression through the production path.

## Scraping and updating the corpus

When adding or refreshing documentation:

1. Use the **pinned map** for that product from `scripts/products.py` (not SPA HTML).
2. Init if needed: `python scripts/build-index.py --product <key> --init`
3. Scrape: `python scripts/scrape-pending.py --product <key> --all-pending` (or `--limit`, `--section`, `--retry-errors`)
4. Rebuild: `python scripts/build-index.py --product <key> --hub`
5. Update **`CHECKPOINT.md`** with what finished and what is next.
6. Prefer additive updates; bulk-`skipped` Release Notes is fine if the goal is product how-to RAG only.

### What belongs in a scrape pass

- Concepts and architecture
- Install / configure / upgrade
- Scanning (Detect, containers, signature, rapid, correlated, BDBA)
- BOM / components / licenses / vulnerabilities
- Policy management and risk
- Integrations and REST API
- Admin, projects, users, reports
- Troubleshooting and known limits

### What does not belong

- Secrets, tokens, customer private data
- Marketing fluff without technical value
- Duplicate copies of the same page under different names

## Naming

- Directories: `kebab-case` (from section roots / product docs roots)
- Files: `kebab-case.md` (from topic titles; paths already assigned in manifest — do not rename lightly)
- Titles inside files: product-accurate proper names (Black Duck, Detect, etc.)
- Product keys: `<slug>-<version>` (e.g. `detect-11.5.1`, `bridge-latest`)

## Agent behavior in this repo

- Optimize for **documentation quality and retrieval**, not application code unless scripts are requested.
- When the user asks how something works, answer from local Markdown first.
- When expanding coverage, scrape into `docs/`, flip manifest statuses, rebuild index, update checkpoint.
- When the corpus cannot support a question, propose the **specific pending topics** or optional products to scrape next.
- On a new session without a clear user goal, open **`CHECKPOINT.md`** first.

## Out of scope (unless asked)

- Building a full app or vector DB pipeline (describe or scaffold only on request).
- Changing Black Duck product configuration in a live customer environment.
- Legal advice on license compliance (document what Black Duck reports; do not replace counsel).
