# Coverity Documentation Corpus

Offline Markdown copy of official **Coverity Documentation** (Black Duck Fluid Topics), arranged so people and agents can answer product questions from this repo instead of the public help center.

The public site is a JavaScript SPA. A normal page fetch only returns “Loading application…”. This corpus was built from the Fluid Topics **TOC and content APIs**, not from scraped HTML.

| Field | Current pin |
|-------|-------------|
| Product | Coverity Documentation (English) |
| Version | **2026.6** |
| Product key | `coverity-2026.6` |
| Topics | **4443 / 4443** (complete) |
| Official help center | https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/ |
| Map ID | `Ul9eg_yUOJh8gKU4cs1xrg` |

**Out of scope unless someone reopens them:** Coverity on Polaris, non-English locales, older Coverity year versions, and Black Duck SCA / Detect / Alert / Bridge (separate repo).

---

## Using a shared copy (no scrape)

If you received this repository already populated, you do **not** need Python, network access, or a scrape to use it.

1. Open the repo root. Topic bodies live under `docs/`.
2. Start from the generated catalog: [`index.md`](index.md) (full TOC) or [`corpus-status.md`](corpus-status.md) (progress hub).
3. Search `docs/**/*.md` for the feature, command, API, or checker you need.
4. Treat those Markdown files as the source of truth. Cite the local path (for example `docs/connect/...`) so answers are checkable.
5. Each topic file has YAML front matter (`title`, `source_url`, `content_id`, `version`, `section`, `scraped_at`) plus the converted body.

### Where topics landed

| Official section | Local folder |
|------------------|--------------|
| Coverity overview | `docs/overview/` |
| Coverity Connect | `docs/connect/` |
| Coverity Analysis (including customization / CodeXM / Extend) | `docs/analysis/` |
| Clients, plug-ins, integrations, and APIs | `docs/clients-plugins/` |
| Coverity Connect APIs | `docs/connect-apis/` |
| Cloud Native Coverity deployment | `docs/cloud-native/` |
| Checkers / SpotBugs | `docs/checkers/` |
| Release notes and upgrade considerations | `docs/release-notes/` |
| Glossary / legal / misc | `docs/glossary/`, `docs/legal/`, `docs/misc/` |

Do **not** hand-edit topic rows in `index.md`. That file is generated from `sources/coverity-2026.6/manifest.json`.

Agents that work in this tree should follow [`AGENTS.md`](AGENTS.md): search local Markdown first, cite paths, and do not invent UI paths, checker names, CLI flags, or API endpoints.

---

## Setup (only when you need to scrape or refresh)

Requires Python 3 and network access to `https://docs.blackduck.com`.

```powershell
cd path\to\Coverity
python -m pip install -r requirements.txt
python scripts/build-index.py --list-products
```

Registered keys, map IDs, and scrape flags live in [`scripts/products.py`](scripts/products.py). Session handoff is [`CHECKPOINT.md`](CHECKPOINT.md). The original phased plan is [`PHASE-PLAN.md`](PHASE-PLAN.md).

---

## Refresh the current version (docs changed, version did not)

Use this when **2026.6** (or whatever is pinned) is updated in place on the official site.

```powershell
python scripts/build-index.py --product coverity-2026.6 --refresh-toc --hub
python scripts/scrape-pending.py --product coverity-2026.6 --all-pending
python scripts/scrape-pending.py --product coverity-2026.6 --refresh-changed
python scripts/scrape-pending.py --product coverity-2026.6 --retry-errors
python scripts/build-index.py --product coverity-2026.6 --hub
python scripts/validate-corpus.py --product coverity-2026.6
```

What those flags do:

| Command | Effect |
|---------|--------|
| `--refresh-toc` | Re-fetch the official TOC and **merge** existing `done` / `error` statuses by content id. New topics become `pending`. |
| `--all-pending` | Download every topic still marked `pending`. |
| `--refresh-changed` | Re-fetch already-`done` topics and rewrite a file only if the normalized Markdown hash changed. |
| `--retry-errors` | Retry topics whose last fetch failed. |
| `--limit 100` | Cap a run (safe on long jobs; repeat the same command to resume). |
| `--delay 0.35` | Seconds between HTTP requests (default). |
| `--dry-run` | Print the selected topic list without writing files. |

`--init` is **not** a refresh. It rebuilds a fresh manifest with every topic `pending` and does not keep previous statuses.

After any scrape, rebuild the hub and update `CHECKPOINT.md`.

---

## Scrape a future Coverity version

A new Coverity year/release (for example 2026.9) is a **new Fluid Topics map**, not a TOC refresh of 2026.6. Do not point the existing `coverity-2026.6` key at the new map and run `--init` unless you intend to throw away the current pin.

### 1. Find the new map ID

The help-center URL for a version looks like:

`https://docs.blackduck.com/r/coverity/<VERSION>/coverity-documentation/`

List maps from the Fluid Topics API (the site does not filter this list well; filter locally):

```powershell
python -c "import json,urllib.request; req=urllib.request.Request('https://docs.blackduck.com/api/khub/maps', headers={'Accept':'application/json'}); maps=json.loads(urllib.request.urlopen(req, timeout=60).read().decode());
def meta(m,k):
    return next((i.get('values') or [] for i in (m.get('metadata') or []) if i.get('key')==k), [])
for m in maps:
    if (m.get('title') or '')=='Coverity Documentation' and 'coverity' in [x.lower() for x in meta(m,'Product')]:
        print(m['id'], meta(m,'Version'), meta(m,'ft:originId'), meta(m,'ft:locale') or meta(m,'lang'))"
```

Pick the English map whose **Version** includes the new release and whose origin looks like `coverity-docs-<VERSION>_en-US`.

Confirm the TOC exists:

`GET https://docs.blackduck.com/api/khub/maps/<MAP_ID>/toc`

Avoid pinning the map whose only version is `latest` if you want a stable corpus. That map moves when Black Duck republishes.

Skip Coverity on Polaris maps and non-English titles unless you are deliberately expanding scope.

### 2. Register the product

Add an entry in `scripts/products.py`. Keep `2026.6` if you still want that corpus on disk.

**Recommended if you keep 2026.6:** give the new version its own `docs_root` and index so paths do not collide with the current `docs/overview/`, `docs/connect/`, … tree (`docs_root` is `None` on the current pin).

```python
"coverity-2026.9": {
    "key": "coverity-2026.9",
    "map_id": "<MAP_ID>",
    "version": "2026.9",
    "product": "coverity",
    "title": "Coverity Documentation",
    "source_dir": "sources/coverity-2026.9",
    "docs_root": "coverity-2026.9",   # writes docs/coverity-2026.9/...
    "root_slugs": COVERITY_ROOT_SLUGS,
    "reader_product": "coverity",
    "reader_book": "coverity-documentation",
    "index_file": "index-2026.9.md",
    "default": False,
    "phase": 1,
},
```

**Replace-in-place (drop 2026.6 as the pin):** only do this if you no longer need the old files as the default corpus. Change `map_id`, `version`, `source_dir`, and `DEFAULT_PRODUCT_KEY` on the existing product, then use `--refresh-toc` (not `--init`) so topics that kept the same content id stay `done`. New topics scrape as `pending`; `--refresh-changed` updates bodies that moved. Leftover Markdown for removed TOC nodes is not deleted automatically.

### 3. Init, scrape, validate

```powershell
python scripts/build-index.py --product coverity-2026.9 --init --hub
python scripts/scrape-pending.py --product coverity-2026.9 --all-pending
# Safer on long runs:
# python scripts/scrape-pending.py --product coverity-2026.9 --all-pending --limit 100
python scripts/scrape-pending.py --product coverity-2026.9 --retry-errors
python scripts/build-index.py --product coverity-2026.9 --hub
python scripts/validate-corpus.py --product coverity-2026.9
```

A full English Coverity map is on the order of **4,000+** topics. At the default 0.35s delay that is typically **1–2 hours** unattended, or faster if the API is responsive. The 2026.6 remainder pass (1,814 topics) ran in about 21 minutes.

Optional first-time smoke test:

```powershell
python scripts/scrape-pending.py --product coverity-2026.9 --section "Coverity overview" --limit 5
```

Section names must match official TOC roots (see `COVERITY_ROOT_SLUGS` in `scripts/products.py`). Phased commands from the original 2026.6 scrape are in [`PHASE-PLAN.md`](PHASE-PLAN.md).

### 4. Retarget the pin

If the new version becomes the default corpus:

1. Set `DEFAULT_PRODUCT_KEY` in `scripts/products.py`.
2. Update the pin table in `AGENTS.md` and this README (version, map ID, help-center URL, topic count).
3. Update `CHECKPOINT.md` with the new key, counts, and next action.
4. Point agents at the new index (`index-2026.9.md` or whatever you registered).

---

## Command cheat sheet

```powershell
python scripts/build-index.py --list-products
python scripts/build-index.py --product coverity-2026.6 --hub
python scripts/build-index.py --product coverity-2026.6 --refresh-toc --hub
python scripts/scrape-pending.py --product coverity-2026.6 --all-pending
python scripts/scrape-pending.py --product coverity-2026.6 --section "Coverity Connect"
python scripts/scrape-pending.py --product coverity-2026.6 --path-contains "Customization guides"
python scripts/scrape-pending.py --product coverity-2026.6 --section "Coverity Analysis" --exclude-path "Customization guides"
python scripts/scrape-pending.py --product coverity-2026.6 --refresh-changed --limit 100
python scripts/scrape-pending.py --product coverity-2026.6 --retry-errors
python scripts/scrape-pending.py --product coverity-2026.6 --repair-empty
python scripts/validate-corpus.py --product coverity-2026.6
```

PowerShell wrappers for the index script: `.\scripts\build-index.ps1 -ListProducts`, `-Init`, `-RefreshToc`, `-Hub`.

---

## Layout

```
AGENTS.md                 Agent rules (RAG-first, pin, scrape policy)
README.md                 This file
CHECKPOINT.md             Session handoff
PHASE-PLAN.md             Original 8-phase scrape plan
corpus-status.md          Generated progress hub
index.md                  Generated 2026.6 TOC catalog
requirements.txt
docs/                     Scraped Markdown (one official topic per file)
sources/<product-key>/    toc.json + manifest.json work queue
scripts/
  products.py             Product / map registry
  build-index.py          Init TOC, refresh TOC, rebuild indexes
  scrape-pending.py       Fetch pending / changed / error topics
  validate-corpus.py      Front matter + content-hash check
```

Manifest topic `status` values: `pending` | `done` | `skipped` | `error`. Scrape `pending`, retry `error`, and do not re-fetch `done` unless you pass `--refresh-changed` or the user asked to refresh.
