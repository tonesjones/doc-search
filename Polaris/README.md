# Polaris Documentation Corpus

Offline, retrieval-friendly Markdown mirror of the official **Black Duck Polaris Platform** documentation (Fluid Topics / docs.blackduck.com). Use it to answer product questions locally, feed a RAG index, or browse without the web UI.

The checked-in tree already includes a full Platform scrape. Most people only need the **Use** section. Use **Refresh** when official docs change or you want a newer snapshot.

## What’s included

| Area | Location | Notes |
|---|---|---|
| Polaris Platform topics | `docs/platform/**` | One official TOC topic per Markdown file |
| Browseable catalog | `index.md`, `index-polaris-platform-latest.md` | Generated; do not hand-edit topic rows |
| Progress hub | `corpus-status.md` | Generated product summary |
| Work queue | `sources/polaris-platform-latest/manifest.json` | Status per topic: `done` / `pending` / `error` / `skipped` |
| Tooling | `scripts/` | Init, scrape, index, validate, smoke tests |
| Agent rules | `AGENTS.md` | Source priority and corpus working rules |

**In scope:** current Black Duck Polaris Platform (`latest`).

**Out of scope (by design):**

- Legacy **Coverity on Polaris** (`cov_polaris`)
- Non-English content
- Full Polaris CI / Bridge CLI duplication — route those questions to a Bridge corpus if you have one (see [CI / Bridge](#ci--bridge-cli-and-pr-workflows))

## Use (no scrape required)

### 1. Clone and open

```bash
git clone <your-repo-url>
cd Polaris
```

Python is only required if you refresh or validate. To **read** the docs, open Markdown as-is.

### 2. Find topics

1. Start at **`index.md`** (or `index-polaris-platform-latest.md`) for the full checklist of topics with links into `docs/platform/`.
2. Search under **`docs/platform/`** by section (e.g. Get Started, How-to, Reference).
3. Prefer local Markdown over web search when answering product questions.

Each topic file has YAML front matter, including:

- `title`, `source_url`, `content_id`
- `product`, `section`
- `scraped_at`, `content_hash` (for change detection)

### 3. Answer product questions

Recommended source order:

1. This repo: `docs/**`, `index.md`, `corpus-status.md`
2. Official Black Duck docs API / site (if local content is missing or stale)
3. General knowledge only if neither covers it — call out uncertainty

Do not treat third-party blog posts as the product authority.

### 4. Optional health checks

```bash
python -m pip install -r requirements.txt
python scripts/validate-corpus.py
python scripts/smoke-retrieval.py
```

- `validate-corpus.py` — manifest, front matter, and file consistency  
- `smoke-retrieval.py` — basic retrieval / routing smoke tests  

## When official docs change

Polaris Platform docs are a mutable **`latest`** book. After Black Duck publishes updates, refresh the local mirror.

### Prerequisites

- Python 3.10+ recommended  
- Network access to `https://docs.blackduck.com`  
- Dependencies:

```bash
python -m pip install -r requirements.txt
```

### Everyday refresh (recommended)

Re-fetch only topics whose source content hash changed (or that need repair):

```bash
python scripts/scrape-pending.py --product all --refresh-changed
python scripts/build-index.py --product all --hub
python scripts/validate-corpus.py
```

Then commit the updated Markdown under `docs/`, plus generated indexes and `sources/*/manifest.json` (and `toc.json` if the TOC changed).

### Full rewrite

Use after converter/script changes, or when you want every page rewritten:

```bash
python scripts/scrape-pending.py --product all --refresh-all
python scripts/build-index.py --product all --hub
python scripts/validate-corpus.py
```

### New or missing topics only

If the TOC gained pages and some are still `pending`:

```bash
python scripts/scrape-pending.py --product polaris-platform-latest --all-pending
python scripts/build-index.py --product all --hub
```

Scrape a single section:

```bash
python scripts/scrape-pending.py --product polaris-platform-latest --section "Understand Polaris"
```

### Re-initialize from the official TOC

Only when you need a fresh TOC/manifest from the Fluid Topics map (preserves prior scrape status for known content IDs when possible):

```bash
python scripts/build-index.py --list-products
python scripts/build-index.py --product polaris-platform-latest --init
python scripts/scrape-pending.py --product polaris-platform-latest --all-pending
python scripts/build-index.py --product all --hub
```

The Platform map ID is registered in `scripts/products.py` (`5MMaMfDebQ2sCji2eI3ezg`). Do not invent map IDs; verify against the official TOC API before adding products.

### Do not

- Hand-edit generated topic rows in `index.md` / product indexes  
- Re-fetch every `done` topic casually — use `--refresh-changed` or an explicit `--refresh-all`  
- Mix this corpus with legacy Coverity-on-Polaris docs without a separate product entry  

## Layout

```text
docs/platform/              Scraped Platform Markdown
sources/polaris-platform-latest/
  toc.json                  Official TOC snapshot
  manifest.json             Work queue + per-topic status/hashes
scripts/
  products.py               Product registry (map IDs, paths)
  build-index.py            Init TOC/manifest, rebuild indexes/hub
  scrape-pending.py         Fetch/convert topics
  validate-corpus.py        Consistency checks
  smoke-retrieval.py        Retrieval smoke tests
index.md                    Hub + Platform index
corpus-status.md            Progress summary
AGENTS.md                   Standing rules for agents/contributors
CHECKPOINT.md               Session status (optional operational notes)
PHASE-PLAN.md               Original scrape plan (historical)
```

## CI / Bridge CLI and PR workflows

Polaris CI, Bridge CLI, SARIF, and pull-request integration guidance is **not** duplicated in this repo. If your team maintains a Bridge corpus (for example a sibling Black Duck SCA docs tree with `docs/bridge/` and `index-bridge.md`), point CI questions there.

`smoke-retrieval.py` can report whether a Bridge corpus is present on the machine; absence does not block using the Platform docs here.

## Command cheat sheet

```bash
# Status / products
python scripts/build-index.py --list-products
python scripts/validate-corpus.py
python scripts/smoke-retrieval.py

# Refresh after upstream doc changes
python scripts/scrape-pending.py --product all --refresh-changed
python scripts/build-index.py --product all --hub

# Full rewrite
python scripts/scrape-pending.py --product all --refresh-all
python scripts/build-index.py --product all --hub

# Finish pending topics only
python scripts/scrape-pending.py --product polaris-platform-latest --all-pending
```

On Windows PowerShell the same commands work as written.

## Contributing / sharing

When you push an updated corpus:

1. Include refreshed `docs/**`, `sources/**`, and regenerated `index*.md` / `corpus-status.md`.  
2. Note the scrape date (front matter `scraped_at` or `CHECKPOINT.md`) so others know freshness.  
3. Keep `AGENTS.md` and this README accurate if tooling or scope changes.

For agents and automated assistants, follow **`AGENTS.md`** (source priority, no hand-edited index rows, refresh policy).
