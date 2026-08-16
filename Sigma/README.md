# Black Duck Sigma documentation corpus

Offline Markdown copy of official **Black Duck Sigma** (Rapid Scan Static) docs from [docs.blackduck.com](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/). Share this folder as a repo and people (or coding agents) can search it instead of the live help center.

The public site is a JavaScript SPA. Opening a topic in a browser works; fetching that same URL with `curl` usually returns only `Loading application...`. This repo was built from the Fluid Topics **TOC and content APIs**, not from scraped HTML.

**Pinned snapshot**

| Field | Current pin |
|-------|-------------|
| Product | Sigma Documentation (English) |
| Version | **2026.8.0** (last official publication 2026-08-11) |
| Product key | `sigma-2026.8.0` |
| Topics | **59 / 59** |
| Official help center | https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/ |
| Map ID | `S_R7XSLfKPN3q6kGpp1eHQ` |
| Catalog | [index.md](index.md) |
| Progress hub | [corpus-status.md](corpus-status.md) |

This is a convenience mirror for local lookup and RAG. Official docs remain the source of truth if this snapshot and the live site disagree.

---

## If someone shared this repo with you

You do **not** need Python, network access, or a scrape to read the docs. The Markdown is already in the tree.

### 1. Get the files

Clone or copy the repo and open the folder:

```bash
git clone <your-repo-url>
cd Sigma
```

Or unzip / copy the shared folder and open it in an editor.

### 2. Browse or search

1. Start at **[index.md](index.md)** (full catalog with links) or **[corpus-status.md](corpus-status.md)** (progress summary).
2. Follow those links into `docs/`, or search the tree (IDE search, `rg`, GitHub search).
3. Each topic file starts with YAML front matter (`title`, `source_url`, `content_id`, `version`, `section`, `scraped_at`) plus the converted body.

| Question about… | Open |
|-----------------|------|
| What Sigma / Rapid Scan Static is | [docs/user-guide/introducing-sigma.md](docs/user-guide/introducing-sigma.md) |
| Binary or Docker download | [docs/user-guide/downloading-sigma.md](docs/user-guide/downloading-sigma.md) |
| Config files, env vars, AI checker plug-in, output | [docs/user-guide/configuring-sigma.md](docs/user-guide/configuring-sigma.md) |
| Jenkins plugin, pipelines, quality-gate policies | [docs/user-guide/running-sigma-in-ci-cd.md](docs/user-guide/running-sigma-in-ci-cd.md) |
| `sigma` CLI and subcommands | [docs/user-guide/command-reference.md](docs/user-guide/command-reference.md) |
| Languages, OS, CI systems, hardware | [docs/user-guide/sigma-support-matrix.md](docs/user-guide/sigma-support-matrix.md) |
| What changed in a release | [docs/user-guide/release-notes.md](docs/user-guide/release-notes.md) |
| Checker catalog (pointer only) | [docs/user-guide/sigma-checkers.md](docs/user-guide/sigma-checkers.md) |

Treat the local Markdown as the source of truth for this snapshot. Cite the path (for example `docs/user-guide/command-reference/the-analyze-subcommand.md`) so answers are checkable.

### 3. Point a coding agent at it

Give the agent this checkout and tell it to follow **[AGENTS.md](AGENTS.md)**:

1. Search this repo first (`docs/**` and `index.md`).
2. Cite the Markdown path in answers.
3. Do not invent CLI flags, Jenkins plugin steps, policy YAML, or checker names.
4. If the corpus is silent, say so. Offer to refresh from the official APIs rather than guessing.

A typical prompt:

> Use the Black Duck Sigma docs in this repo (`docs/`, `index.md`). Search those files before answering. Cite the Markdown path.

### Layout

```
docs/user-guide/       Topic bodies (one official topic → one .md file)
index.md               Full catalog with links (generated — do not hand-edit rows)
corpus-status.md       Progress summary (generated)
AGENTS.md              Standing rules for coding agents
CHECKPOINT.md          Last scrape status and next action
scripts/               Only needed if you refresh or scrape
sources/sigma-2026.8.0/  TOC snapshot + work-queue manifest
```

### What is not in this snapshot

- Older Sigma year versions (2026.7.0, 2026.6.1)
- The mutable `latest` map (it moves when Black Duck republishes)
- Non-English locales
- The full checker catalog and standalone release-notes history — those official pages are pointer topics that link to Fluid Topics origin IDs, not extra books in this repo
- Other Black Duck products (SCA, Detect, Coverity, Polaris, Signal). Keep those in their own corpora; do not scrape them into this tree.

---

## How to update later

There are **two** situations. Pick the matching workflow. Never scrape the SPA HTML page; always use the scripts (Fluid Topics APIs).

| Situation | What changed | Workflow |
|-----------|--------------|----------|
| Same version, pages edited or added | Still **2026.8.0**, same map ID | [Refresh the current version](#1-refresh-the-current-version-docs-changed-version-did-not) |
| New Sigma release | Help center shows **2026.9.0** (or later) with a new map | [Scrape a future Sigma version](#2-scrape-a-future-sigma-version) |

`--init` is **not** a refresh. It rebuilds a fresh manifest with every topic `pending` and does not keep previous statuses. Do not use it on the current pin unless you intend a full reset.

### Prerequisites (refresh / scrape only)

- Python 3.10+
- Network access to `https://docs.blackduck.com`
- From the repo root:

```powershell
cd path\to\Sigma
python -m pip install -r requirements.txt
python scripts/build-index.py --list-products
```

Reading the existing Markdown needs nothing extra. `requirements.txt` is only for the scrape scripts.

Registered keys, map IDs, and scrape flags live in [`scripts/products.py`](scripts/products.py). Session handoff is [`CHECKPOINT.md`](CHECKPOINT.md).

### 1. Refresh the current version (docs changed, version did not)

Use this when **2026.8.0** is updated in place on the official site. The map ID is still `S_R7XSLfKPN3q6kGpp1eHQ`.

```powershell
python scripts/build-index.py --product sigma-2026.8.0 --refresh-toc --hub
python scripts/scrape-pending.py --product sigma-2026.8.0 --all-pending
python scripts/scrape-pending.py --product sigma-2026.8.0 --refresh-changed
python scripts/scrape-pending.py --product sigma-2026.8.0 --retry-errors
python scripts/build-index.py --product sigma-2026.8.0 --hub
python scripts/validate-corpus.py --product sigma-2026.8.0
python scripts/smoke-retrieval.py
```

What those flags do:

| Command | Effect |
|---------|--------|
| `--refresh-toc` | Re-fetch the official TOC and **keep** existing `done` / `error` statuses by content id. New topics become `pending`. Removed topics drop out of the manifest. |
| `--all-pending` | Download every topic still marked `pending`. |
| `--refresh-changed` | Re-fetch already-`done` topics and rewrite a file only if the normalized Markdown hash changed. |
| `--retry-errors` | Retry topics whose last fetch failed. |
| `--dry-run` | Print the selected topic list without writing files. |

After the commands succeed:

1. Confirm [corpus-status.md](corpus-status.md) counts look right.
2. Spot-check a few changed files under `docs/`.
3. Update the pin table at the top of this README (topic count, publication date if you know it).
4. Note what changed in [CHECKPOINT.md](CHECKPOINT.md).
5. Commit `docs/`, `sources/`, generated indexes, this README, and the checkpoint together.

Do **not** hand-edit topic rows in `index.md` or `corpus-status.md`. Change `sources/sigma-2026.8.0/manifest.json` (or re-scrape) and run `build-index.py`.

### 2. Scrape a future Sigma version

A new Sigma year/release (for example 2026.9.0) is a **new Fluid Topics map**, not a TOC refresh of 2026.8.0. Do not point the existing `sigma-2026.8.0` key at the new map and run `--init` unless you intend to throw away the current pin.

Avoid pinning the map whose only version is `latest` (`vkb5zvSX~7E~X~04sUrrNQ`) if you want a stable corpus. That map moves when Black Duck republishes.

#### Find the new map ID

The help-center URL for a version looks like:

`https://docs.blackduck.com/r/sigma/<VERSION>/sigma-documentation/`

List Sigma maps from the Fluid Topics API and filter locally:

```powershell
python -c "import json,urllib.request; req=urllib.request.Request('https://docs.blackduck.com/api/khub/maps', headers={'Accept':'application/json'}); maps=json.loads(urllib.request.urlopen(req, timeout=60).read().decode());
def meta(m,k):
    return next((i.get('values') or [] for i in (m.get('metadata') or []) if i.get('key')==k), [])
for m in maps:
    products=[x.lower() for x in meta(m,'Product')]
    if (m.get('title') or '')=='Sigma Documentation' or 'sigma' in products:
        print(m['id'], meta(m,'Version'), meta(m,'ft:originId'), meta(m,'ft:locale') or meta(m,'lang'))"
```

Pick the English map (`en-US`) whose **Version** includes the new release and whose origin looks like `sigma-ug_<VERSION>`. Confirm the TOC exists:

`GET https://docs.blackduck.com/api/khub/maps/<MAP_ID>/toc`

Skip non-English titles and the unversioned `latest` map unless you are deliberately expanding scope. Do not invent map IDs.

#### Register the product (keep the old snapshot)

Add an entry in [`scripts/products.py`](scripts/products.py). Keep `sigma-2026.8.0` if you still want that corpus on disk. Give the new version its own `docs_root` and index so paths do not collide with the current `docs/user-guide/` tree.

```python
"sigma-2026.9.0": {
    "key": "sigma-2026.9.0",
    "map_id": "<MAP_ID>",
    "version": "2026.9.0",
    "product": "sigma",
    "title": "Sigma Documentation",
    "source_dir": "sources/sigma-2026.9.0",
    "docs_root": "sigma-2026.9.0",   # writes docs/sigma-2026.9.0/...
    "root_slugs": SIGMA_ROOT_SLUGS,
    "reader_product": "sigma",
    "reader_book": "sigma-documentation",
    "reader_path": "r/sigma/2026.9.0/sigma-documentation/",
    "index_file": "index-2026.9.0.md",
    "default": False,
    "phase": 1,
},
```

If official section titles change, update `SIGMA_ROOT_SLUGS` in the same file before `--init`.

#### Init, scrape, validate

```powershell
python scripts/build-index.py --product sigma-2026.9.0 --init --hub
python scripts/scrape-pending.py --product sigma-2026.9.0 --all-pending
python scripts/scrape-pending.py --product sigma-2026.9.0 --retry-errors
python scripts/build-index.py --product sigma-2026.9.0 --hub
python scripts/validate-corpus.py --product sigma-2026.9.0
```

A full English Sigma map is currently on the order of **~59** topics and finishes in a few minutes. Preview first with `--dry-run` or a path filter:

```powershell
python scripts/scrape-pending.py --product sigma-2026.9.0 --path-contains "Introducing Sigma" --limit 5 --dry-run
```

#### Replace-in-place (drop the old pin)

Only do this if you no longer need the current files as the default corpus. Change `map_id`, `version`, `source_dir`, and `DEFAULT_PRODUCT_KEY` on the existing `sigma-2026.8.0` entry, then use `--refresh-toc` (not `--init`) so topics that kept the same content id stay `done`. New topics scrape as `pending`; `--refresh-changed` updates bodies that moved. Leftover Markdown for removed TOC nodes is **not** deleted automatically.

#### Retarget the pin

If the new version becomes the default corpus:

1. Set `DEFAULT_PRODUCT_KEY` in `scripts/products.py`.
2. Update the pin table in [AGENTS.md](AGENTS.md) and this README (version, map ID, help-center URL, topic count).
3. Update [CHECKPOINT.md](CHECKPOINT.md) with the new key, counts, and next action.
4. Point agents at the new index (`index-2026.9.0.md` or whatever you registered).
5. Update `scripts/smoke-retrieval.py` paths if topic files moved under a new `docs_root`.

---

## After any scrape

1. Confirm [corpus-status.md](corpus-status.md) counts look right.
2. Spot-check a few new or changed files under `docs/`.
3. Run `python scripts/validate-corpus.py --product <key>` and `python scripts/smoke-retrieval.py`.
4. Note what changed in [CHECKPOINT.md](CHECKPOINT.md).
5. Commit `docs/`, `sources/`, generated indexes, and the checkpoint together.

---

## Command cheat sheet

```powershell
# Status / products
python scripts/build-index.py --list-products
python scripts/validate-corpus.py --product sigma-2026.8.0
python scripts/smoke-retrieval.py

# Everyday refresh (same book, docs edited or TOC grew)
python scripts/build-index.py --product sigma-2026.8.0 --refresh-toc --hub
python scripts/scrape-pending.py --product sigma-2026.8.0 --all-pending
python scripts/scrape-pending.py --product sigma-2026.8.0 --refresh-changed
python scripts/build-index.py --product sigma-2026.8.0 --hub

# One path only
python scripts/scrape-pending.py --product sigma-2026.8.0 --path-contains "Command Reference"

# Retry failures
python scripts/scrape-pending.py --product sigma-2026.8.0 --retry-errors

# Preview without writing
python scripts/scrape-pending.py --product sigma-2026.8.0 --all-pending --dry-run
```

PowerShell wrappers for the index script: `.\scripts\build-index.ps1 -ListProducts`, `-Init`, `-RefreshToc`, `-Hub`.

`--delay` (default `0.35` seconds) spaces requests. If you see HTTP 429, the scraper already sleeps 10 seconds; increase `--delay` and rerun `--retry-errors`.

---

## Housekeeping

- One official TOC topic → one file at the path in the manifest. Do not rename those paths lightly (indexes and agents follow them).
- Scrape only `pending` (retry `error`). Do not re-fetch `done` unless you pass `--refresh-changed` or reset status.
- Leave unscraped work as `pending` in the manifest. Do not create empty stub files.
- Do not commit secrets, tokens, or customer data. This tree is public-doc text only.

---

## License and attribution

Topic bodies are Black Duck product documentation, retrieved from the public docs site. Copyright remains with Black Duck / the original publisher. Use this mirror in line with their terms. Scripts in `scripts/` are part of this repository.
