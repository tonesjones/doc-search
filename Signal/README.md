# Black Duck Signal documentation corpus

Offline Markdown copy of official **Black Duck Signal** docs from [docs.blackduck.com](https://docs.blackduck.com/r/signal/black-duck-signal.html). People and coding agents can search this repo instead of the live help center.

The public site is a JavaScript SPA. Opening a topic in a browser works; fetching that same URL with `curl` usually returns only `Loading application...`. This repo uses the Fluid Topics **TOC and content APIs**, not HTML shells.

**Pinned snapshot**

| Field | Current pin |
|-------|-------------|
| Product | Black Duck Signal (English) |
| Version | **latest** (last official publication 2026-07-23) |
| Product key | `signal-latest` |
| Topics | **17 / 17** |
| Official help center | https://docs.blackduck.com/r/signal/black-duck-signal.html |
| Map ID | `xmDr3Yryk7OYDGb__OGKlg` |
| Catalog | [index.md](index.md) |
| Progress hub | [corpus-status.md](corpus-status.md) |

This is a convenience mirror for local lookup and RAG. Official docs remain the source of truth if this snapshot and the live site disagree.

---

## Using a shared copy (no scrape)

If someone handed you this folder already populated, you do **not** need Python, network access, or a scrape to read it.

### 1. Open the folder

```
docs/                  Topic bodies (one official topic → one .md file)
  overview/            What Signal is (Developer vs Enterprise, MCP, OS)
  scan-changes/        Claude Code, Copilot, Code Sight, CLI diff / file scans
  scan-project/        Full-project CLI, SARIF-only, send results to Polaris
  reference/           Bridge / Signal flags and environment variables
  ai-security/         LLM gateway, data handling, trust
  release-notes/       Signal release notes
index.md               Full catalog with links (generated — do not hand-edit rows)
corpus-status.md       Progress summary (generated)
AGENTS.md              Standing rules for coding agents
CHECKPOINT.md          Last scrape status and next action
```

Each topic file starts with YAML front matter (`title`, `source_url`, `content_id`, `version`, `section`, `scraped_at`).

### 2. Find a topic

1. Start at [index.md](index.md) or [corpus-status.md](corpus-status.md).
2. Follow the links into `docs/…`, or search the tree (IDE search, `rg`, GitHub search).
3. Route by question:
   - What is Signal / Developer vs Enterprise → [docs/overview/](docs/overview/)
   - Coding assistants, IDE, incremental CLI scans → [docs/scan-changes/](docs/scan-changes/)
   - Full-project scan, SARIF, Polaris upload → [docs/scan-project/](docs/scan-project/)
   - Flags and env vars → [docs/reference/](docs/reference/)
   - AI / data protection → [docs/ai-security/](docs/ai-security/)
   - What changed in a release → [docs/release-notes/](docs/release-notes/)

Treat the local Markdown as the source of truth for this snapshot. Cite the path (for example `docs/scan-changes/from-the-command-line/perform-a-diff-scan.md`) so answers are checkable.

### 3. Use it with a coding agent

Point the agent at this checkout and tell it to follow [AGENTS.md](AGENTS.md):

1. Search this repo first (`docs/**` and `index.md`).
2. Cite the Markdown path in answers.
3. Do not invent UI paths, CLI flags, MCP setup steps, or Polaris upload options.
4. If the corpus is silent, say so. Offer to refresh from the official APIs rather than guessing.

A typical prompt:

> Use the Black Duck Signal docs in this repo (`docs/`, `index.md`). Search those files before answering. Cite the Markdown path.

### What is not in this snapshot

Sibling products live in neighboring folders. Do **not** scrape them into this tree:

| Product | Typical path |
|---------|--------------|
| Black Duck SCA / Detect / Alert / Bridge | `C:\TestCode\Product Docs\BlackDuck SCA` |
| Coverity | `C:\TestCode\Product Docs\Coverity` |
| Polaris | `C:\TestCode\Product Docs\Polaris` |

Non-English Signal locales are out of scope unless someone registers those maps.

---

## Prerequisites (only if you will refresh or scrape)

- Python 3.10+
- Network access to `https://docs.blackduck.com`
- From the repo root:

```powershell
cd path\to\Signal
python -m pip install -r requirements.txt
python scripts/build-index.py --list-products
```

`requirements.txt` is only needed to run the scrape scripts. Reading the existing Markdown needs nothing extra.

**Never scrape the SPA HTML page.** Always go through the scripts (Fluid Topics APIs).

---

## When official docs change

There are two different situations. Use the matching workflow.

Signal today is a mutable **`latest`** book (no year in the help-center URL). Most updates are case 1. Case 2 is for a future versioned publication (for example if Black Duck ships a `2027.1` Signal book with a new map ID).

### 1. Same book, updated in place (usual path)

The map ID is still `xmDr3Yryk7OYDGb__OGKlg`. Pages were edited, added, or removed on the live site.

```powershell
python scripts/build-index.py --product signal-latest --refresh-toc --hub
python scripts/scrape-pending.py --product signal-latest --all-pending
python scripts/scrape-pending.py --product signal-latest --refresh-changed
python scripts/scrape-pending.py --product signal-latest --retry-errors
python scripts/build-index.py --product signal-latest --hub
python scripts/validate-corpus.py --product signal-latest
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

`--init` is **not** a refresh. It rebuilds a fresh manifest with every topic `pending` and does not keep previous statuses. Do not use it unless you intend a full reset.

After the commands succeed:

1. Confirm [corpus-status.md](corpus-status.md) counts look right.
2. Spot-check a few changed files under `docs/`.
3. Update the pin table at the top of this README (topic count, publication date if you know it).
4. Note what changed in [CHECKPOINT.md](CHECKPOINT.md).
5. Commit `docs/`, `sources/`, generated indexes, this README, and the checkpoint together.

Do **not** hand-edit topic rows in `index.md` or `corpus-status.md`. Change `sources/signal-latest/manifest.json` (or re-scrape) and run `build-index.py`.

### 2. A new product version / new Fluid Topics map

A new Signal release with its own help-center map is **not** a TOC refresh of `signal-latest`. Do not point the existing key at a new map and run `--init` unless you intend to throw away the current pin.

#### Find the new map ID

The current help-center URL has no version segment:

`https://docs.blackduck.com/r/signal/black-duck-signal/`

A future versioned book might look like:

`https://docs.blackduck.com/r/signal/<VERSION>/black-duck-signal/`

List Signal maps from the Fluid Topics API and filter locally:

```powershell
python -c "import json,urllib.request; req=urllib.request.Request('https://docs.blackduck.com/api/khub/maps', headers={'Accept':'application/json'}); maps=json.loads(urllib.request.urlopen(req, timeout=60).read().decode());
def meta(m,k):
    return next((i.get('values') or [] for i in (m.get('metadata') or []) if i.get('key')==k), [])
for m in maps:
    products=[x.lower() for x in meta(m,'Product')]
    if (m.get('title') or '')=='Black Duck Signal' or 'signal' in products:
        print(m['id'], meta(m,'Version'), meta(m,'ft:originId'), meta(m,'ft:locale') or meta(m,'lang'))"
```

Pick the English map (`en-US`) whose **Version** is the new release. Confirm the TOC exists:

`GET https://docs.blackduck.com/api/khub/maps/<MAP_ID>/toc`

Skip non-English titles unless you are deliberately expanding scope. Do not invent map IDs.

#### Register the product (keep the old snapshot)

Add an entry in [`scripts/products.py`](scripts/products.py). Keep `signal-latest` if you still want that corpus on disk. Give the new version its own `docs_root` and index so paths do not collide with the current `docs/overview/`, `docs/scan-changes/`, … tree.

```python
"signal-2027.1": {
    "key": "signal-2027.1",
    "map_id": "<MAP_ID>",
    "version": "2027.1",
    "product": "signal",
    "title": "Black Duck Signal",
    "source_dir": "sources/signal-2027.1",
    "docs_root": "signal-2027.1",   # writes docs/signal-2027.1/...
    "root_slugs": SIGNAL_ROOT_SLUGS,
    "reader_product": "signal",
    "reader_book": "black-duck-signal",
    "reader_path": "r/signal/2027.1/black-duck-signal/",  # adjust if the live URL differs
    "index_file": "index-2027.1.md",
    "default": False,
    "phase": 1,
},
```

If the new book still has no version in the reader URL, set `reader_path` to whatever `prettyUrl` the TOC actually uses.

If official section titles change, update `SIGNAL_ROOT_SLUGS` in the same file before `--init`.

#### Init, scrape, validate

```powershell
python scripts/build-index.py --product signal-2027.1 --init --hub
python scripts/scrape-pending.py --product signal-2027.1 --all-pending
python scripts/scrape-pending.py --product signal-2027.1 --retry-errors
python scripts/build-index.py --product signal-2027.1 --hub
python scripts/validate-corpus.py --product signal-2027.1
```

A full English Signal map is currently on the order of **~17** topics and finishes in under a minute. Preview first with `--dry-run` or a one-section smoke:

```powershell
python scripts/scrape-pending.py --product signal-2027.1 --section "Overview of Black Duck Signal" --limit 5 --dry-run
```

#### Replace-in-place (drop the old pin)

Only do this if you no longer need the current files as the default corpus. Change `map_id`, `version`, `source_dir`, and `DEFAULT_PRODUCT_KEY` on the existing `signal-latest` entry, then use `--refresh-toc` (not `--init`) so topics that kept the same content id stay `done`. New topics scrape as `pending`; `--refresh-changed` updates bodies that moved. Leftover Markdown for removed TOC nodes is **not** deleted automatically.

#### Retarget the pin

If the new version becomes the default corpus:

1. Set `DEFAULT_PRODUCT_KEY` in `scripts/products.py`.
2. Update the pin table in [AGENTS.md](AGENTS.md) and this README (version, map ID, help-center URL, topic count).
3. Update [CHECKPOINT.md](CHECKPOINT.md) with the new key, counts, and next action.
4. Point agents at the new index (`index-2027.1.md` or whatever you registered).
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
python scripts/validate-corpus.py --product signal-latest
python scripts/smoke-retrieval.py

# Everyday refresh (same book, docs edited or TOC grew)
python scripts/build-index.py --product signal-latest --refresh-toc --hub
python scripts/scrape-pending.py --product signal-latest --all-pending
python scripts/scrape-pending.py --product signal-latest --refresh-changed
python scripts/build-index.py --product signal-latest --hub

# One section only
python scripts/scrape-pending.py --product signal-latest --section "Scan your code changes"

# Retry failures
python scripts/scrape-pending.py --product signal-latest --retry-errors

# Preview without writing
python scripts/scrape-pending.py --product signal-latest --all-pending --dry-run
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
