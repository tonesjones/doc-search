# Black Duck documentation corpus

Offline Markdown copy of official Black Duck product docs, scraped from [docs.blackduck.com](https://docs.blackduck.com) so people and coding agents can search this repo instead of the live site.

The public help site is a JavaScript SPA. Opening a topic URL in a browser works; fetching that same URL with `curl` or a plain HTTP client usually returns only `Loading application...`. This repo uses the Fluid Topics **TOC and content APIs**, not HTML shells.

**Pinned snapshot (last full scrape: 2026-08-08):**

| Product | Version | Topics | Browse from |
|---------|---------|-------:|-------------|
| Black Duck SCA (server / UI) | 2026.7 | 941 | [index.md](index.md) |
| Black Duck Detect | 11.5.1 | 206 | [index-detect.md](index-detect.md) |
| Black Duck Alert | 8.4.0 | 45 | [index-alert.md](index-alert.md) |
| Bridge CLI | latest | 174 | [index-bridge.md](index-bridge.md) |
| Black Duck C/CPP Tool | latest | 14 | [index-c-cpp-tool.md](index-c-cpp-tool.md) |

**1,380 topics** in `docs/`. Progress hub: [corpus-status.md](corpus-status.md).

This is a convenience mirror for RAG and local lookup. Official docs remain the source of truth if this snapshot and the live site disagree.

---

## What you get after clone

No scrape is required to **read** the corpus. Clone, then open Markdown.

```
docs/                  # Topic bodies (one official topic → one .md file)
  help-center/         # SCA UI: BOM, policy, scanning, admin, …
  getting-started/ api/ architecture/ architecture-hosted/
  install-kubernetes/ install-docker-swarm/
  scanning-best-practices/ reporting-database/ release-notes/
  detect/ alert/ bridge/ c-cpp-tool/
index.md               # Full SCA catalog (generated — do not hand-edit rows)
index-detect.md        # Detect catalog
index-alert.md         # Alert catalog
index-bridge.md        # Bridge catalog
index-c-cpp-tool.md    # C/CPP Tool catalog
corpus-status.md       # Multi-product progress (generated)
sources/<product>/     # toc.json + manifest.json (work queues)
scripts/               # Init / refresh / scrape
AGENTS.md              # Standing rules for coding agents
CHECKPOINT.md          # Session handoff (what is in / out of scope)
```

Each topic file starts with YAML front matter (`title`, `source_url`, `content_id`, `version`, `section`, `scraped_at`).

---

## How to use it

### As a person

1. Start at [corpus-status.md](corpus-status.md) or the product index you need.
2. Follow links into `docs/…`, or search the tree (IDE search, `rg`, GitHub search).
3. Route by product:
   - SCA server/UI, BOM, policy, install, reporting → `docs/help-center/`, install folders, [index.md](index.md)
   - Detect client, detectors, properties → `docs/detect/`, [index-detect.md](index-detect.md)
   - Alert channels / providers → `docs/alert/`, [index-alert.md](index-alert.md)
   - Bridge CLI / CI scan plugins → `docs/bridge/`, [index-bridge.md](index-bridge.md)
   - C/C++ BOM via blackduck-c-cpp → `docs/c-cpp-tool/`, [index-c-cpp-tool.md](index-c-cpp-tool.md)

### As a coding agent (Claude, Cursor, Copilot, Grok, …)

Point the agent at this checkout and tell it to follow [AGENTS.md](AGENTS.md):

1. Search this repo first (`docs/**` and the product indexes).
2. Cite the Markdown path in answers.
3. Do not invent UI paths, license names, API endpoints, or Detect properties.
4. If the corpus is silent, say so. Offer to refresh from the official APIs rather than guessing.

A typical prompt:

> Use the Black Duck docs in this repo (`docs/`, `index.md`, `index-detect.md`). Search those files before answering. Cite the Markdown path.

### What is not in this snapshot

Intentionally omitted from this tree (see [CHECKPOINT.md](CHECKPOINT.md)): Air-gapped KnowledgeBase, rest of Black Duck Tools (KB Vulnerability Feed Server), BDBA, Artifactory, Code Sight, Defensics, Seeker, Sigma, Signal, SRM, Portal, older SCA year versions, non-English locales.

Sibling corpora (do not scrape here): Coverity at `C:\TestCode\Product Docs\Coverity`, Polaris at `C:\TestCode\Product Docs\Polaris`.

---

## Prerequisites (only if you will refresh or scrape)

- Python 3.10+
- Network access to `https://docs.blackduck.com`
- From the repo root:

```powershell
python -m pip install -r requirements.txt
```

`requirements.txt` is only needed to run `scripts/scrape-pending.py`. Reading the existing Markdown needs nothing extra.

On Windows, keep the clone path reasonably short. The scraper uses extended-length paths, but deep Bridge trees can still get close to `MAX_PATH`.

---

## When official docs change

There are three different situations. Use the matching workflow. **Never scrape the SPA HTML page**; always go through the scripts (Fluid Topics APIs).

Registered product keys:

| Key | Product | Docs live under |
|-----|---------|-----------------|
| `blackduck-2026.7` | SCA 2026.7 | section folders under `docs/` |
| `detect-11.5.1` | Detect 11.5.1 | `docs/detect/` |
| `alert-8.4.0` | Alert 8.4.0 | `docs/alert/` |
| `bridge-latest` | Bridge CLI | `docs/bridge/` |
| `c-cpp-tool-latest` | C/CPP Tool (Tools map, C/CPP chapter only) | `docs/c-cpp-tool/` |
| `airgap-kb-latest` | Air-gapped KB (optional, not initialized) | `docs/airgap-kb/` |

List keys:

```powershell
python scripts/build-index.py --list-products
```

### 1. New or removed topics on the same version (TOC changed)

`--refresh-toc` re-downloads the table of contents and **keeps existing `done` statuses by content id**. New topics become `pending`. Removed topics drop out of the manifest. Already-scraped files are **not** re-downloaded.

```powershell
python scripts/build-index.py --product detect-11.5.1 --refresh-toc --hub
python scripts/scrape-pending.py --product detect-11.5.1 --all-pending
python scripts/build-index.py --product detect-11.5.1 --hub
```

Preview first (no writes):

```powershell
python scripts/scrape-pending.py --product detect-11.5.1 --all-pending --dry-run
```

Then update [CHECKPOINT.md](CHECKPOINT.md) if the counts or scope changed.

### 2. Existing pages were edited in place (same content ids)

`--refresh-toc` will **not** re-fetch those. Status stays `done`. Reset the topics you care about, then scrape.

**One or a few pages** — in `sources/<product-key>/manifest.json`, set that topic's `"status"` to `"pending"`, then:

```powershell
python scripts/scrape-pending.py --product blackduck-2026.7 --all-pending
python scripts/build-index.py --product blackduck-2026.7 --hub
```

**Re-scrape an entire product** (wipes statuses; every topic becomes pending):

```powershell
python scripts/build-index.py --product alert-8.4.0 --init
python scripts/scrape-pending.py --product alert-8.4.0 --all-pending
python scripts/build-index.py --product alert-8.4.0 --hub
```

Do not use `--init` unless you intend a full reset of that product's manifest.

### 3. New product version (for example SCA 2026.10 or Detect 11.6)

The live map id and version change. Do **not** overwrite the old product key if you still want the previous snapshot.

1. Open `scripts/products.py` and add a new entry (copy an existing one). Set `key`, `map_id`, `version`, `source_dir`, `docs_root` / `index_file`, and reader URL fields. Map ids come from the official Fluid Topics TOC:

   `GET https://docs.blackduck.com/api/khub/maps/{mapId}/toc`

2. Init, scrape, rebuild:

```powershell
python scripts/build-index.py --product detect-11.6.0 --init
python scripts/scrape-pending.py --product detect-11.6.0 --all-pending
python scripts/build-index.py --product detect-11.6.0 --hub
```

3. Update [AGENTS.md](AGENTS.md) and [CHECKPOINT.md](CHECKPOINT.md) so agents pin to the new key.

To find a map id, open the product on docs.blackduck.com and inspect network calls to `/api/khub/maps/…/toc`, or ask someone who already registered the map.

### Retry failed downloads

```powershell
python scripts/scrape-pending.py --product bridge-latest --retry-errors
python scripts/build-index.py --product bridge-latest --hub
```

`--retry-errors --include-pending` does both `error` and `pending`.

### Optional: add Air-gapped KnowledgeBase

Registered but never initialized:

```powershell
python scripts/build-index.py --product airgap-kb-latest --init
python scripts/scrape-pending.py --product airgap-kb-latest --all-pending
python scripts/build-index.py --product airgap-kb-latest --hub
```

### After any scrape

1. Confirm [corpus-status.md](corpus-status.md) counts look right.
2. Spot-check a few new or changed files under `docs/`.
3. Note what changed in [CHECKPOINT.md](CHECKPOINT.md).
4. Commit `docs/`, `sources/`, generated indexes, and the checkpoint together.

Do **not** hand-edit topic rows in `index.md` / `index-*.md` / `corpus-status.md`. Change `sources/<key>/manifest.json` (or re-scrape) and run `build-index.py`.

---

## Script cheat sheet

```powershell
# Indexes / TOC
python scripts/build-index.py --list-products
python scripts/build-index.py --product blackduck-2026.7
python scripts/build-index.py --product detect-11.5.1 --init
python scripts/build-index.py --product detect-11.5.1 --refresh-toc --hub
python scripts/build-index.py --product all --hub

# Scrape
python scripts/scrape-pending.py --product detect-11.5.1 --all-pending
python scripts/scrape-pending.py --product blackduck-2026.7 --section "Black Duck SCA Help Center" --limit 20
python scripts/scrape-pending.py --product bridge-latest --path-contains "jenkins" --dry-run
python scripts/scrape-pending.py --product alert-8.4.0 --retry-errors
python scripts/scrape-pending.py --product detect-11.5.1 --all-pending --delay 0.5
```

PowerShell wrapper for the indexer:

```powershell
.\scripts\build-index.ps1 -ListProducts
.\scripts\build-index.ps1 -Product detect-11.5.1 -RefreshToc -Hub
```

`--delay` (default `0.35` seconds) spaces requests. If you see HTTP 429, the scraper already sleeps 10 seconds; increase `--delay` and rerun `--retry-errors`.

---

## Housekeeping rules

- One official TOC topic → one file at the path in the manifest. Do not rename those paths lightly (indexes and agents follow them).
- Scrape only `pending` (retry `error`). Do not re-fetch `done` unless you reset status or `--init`.
- Leave unscraped work as `pending` in the manifest. Do not create empty stub files.
- Do not commit secrets, tokens, or customer data. This tree is public-doc text only.

---

## License and attribution

Topic bodies are Black Duck product documentation, retrieved from the public docs site. Copyright remains with Black Duck / the original publisher. Use this mirror in line with their terms. Scripts in `scripts/` are part of this repository.
