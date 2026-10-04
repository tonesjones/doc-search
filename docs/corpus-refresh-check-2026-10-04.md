# Corpus refresh completed, October 4, 2026

Refreshed the existing Product Docs scope from the official Black Duck Fluid Topics TOC/content APIs. The initial official catalog check returned all 124 published maps in one page. Product versions and documentation editions below were verified from map metadata.

Branch: `codex/corpus-refresh-2026-10-04`.

| Corpus | Current documentation | Completed TOC rows | Official map edition |
|---|---|---:|---|
| Black Duck SCA | 2026.7 | 939 | September 30 |
| Detect | 12.0.0 | 207 | September 17 |
| Alert | 8.4.1 | 46 | September 28 |
| Black Duck Tools / C/CPP Tool | latest | 21 official + 1 local reference note | September 29 |
| Coverity | 2026.9 | 4,526 | September 24 |
| Sigma | 2026.9.1 | 59 | September 22 |
| Bridge | latest | 178 | September 29 |
| Polaris Platform | latest | 205 | October 2 |
| Signal | latest | 31 official + 1 local reference note | September 28 |

Every listed manifest has zero pending, skipped, or error topics. Dates are documentation editions, not inferred product release dates. TOC row counts include repeated occurrences of a topic.

## Version routing and preservation

- Alert 8.4.1, Coverity 2026.9, and Sigma 2026.9.1 use separate source and document directories. Their default catalogs select the new versions.
- Original Alert 8.4.0, Coverity 2026.6, and Sigma 2026.8.0 documents and source snapshots remain unchanged. Historical catalogs are `BlackDuck SCA/index-alert-8.4.0.md`, `Coverity/index-coverity-2026.6.md`, and `Sigma/index-sigma-2026.8.0.md`.
- Detect 11.5.1 remains historical. The Detect 11-to-12 comparison was regenerated and remained unchanged.
- SRM and the GitHub SCA MCP snapshot had no detected version change and remain unchanged.
- SCA's renamed sections retain the existing folder mapping. Empty chapter bodies become navigation to their official child topics.
- Signal and C/CPP local reference notes retain their original bytes, remain indexed, and are excluded from official API scraping. A repeated-TOC-merge regression protects this behavior.
- The new Tools map includes SCASS MCP in `docs/scass-mcp/`, separate from the GitHub SCA MCP snapshot. KnowledgeBase Vulnerability Feed Server files omitted by the newer map remain as historical files.
- Removed official topics remain on disk for historical reference; use the current generated indexes to resolve current guidance.

## Validation

`python -B scripts/check-offline.py` passed all 15 check groups, including 83 root regression tests and nine product tooling tests, all seven corpus validators, Polaris/Sigma/Signal retrieval checks, and the SCA integrity/retrieval report.

Additional checks confirmed:

- All refreshed manifests are complete, with zero pending or error topics.
- No duplicate output paths occur in the imported Coverity and Sigma snapshots or refreshed SCA snapshot. Their maximum absolute path lengths are 240, 227, and 237 characters in this checkout.
- A SHA-256 preservation check found zero changes across 5,376 historical and unrelated files. The two current local reference notes also remain byte-identical to the original Git versions.
- A repeated cached Sigma scrape reported zero updated, 59 unchanged, and zero errors.
- Temporary Windows manifest sharing locks are handled by a bounded replacement retry. Tests confirm eventual publication and preservation of the original file when the lock persists.

No live product UI/API behavior or customer-answer accuracy evaluation was performed. Corpus instruction/source changes invalidate older evaluation traces; offline checks do not establish answer correctness.

## Refresh tooling

The existing product indexers, converters, and validators remain the owners of corpus files. `scripts/cached-corpus-scrape.py` downloads official topic bodies into a bounded, resumable cache and invokes those existing converters. Use a new cache directory for each refresh; reuse it only to resume the same snapshot.

After refreshing a product TOC with its existing indexer, an example from the repository root is:

```powershell
python -B scripts/cached-corpus-scrape.py Sigma sigma-2026.9.1 --cache .local/next-refresh-cache --mode both
python -B Sigma/scripts/build-index.py --product sigma-2026.9.1 --hub
python -B Sigma/scripts/validate-corpus.py
```

Install the existing scraper requirements to run a refresh. Reading the corpus and running the offline checks require no additional packages.

## Source limitations

The official content API returned no extractable body for one SCA leaf topic, `Binary scanner information`, and two Coverity leaf topics, `Coverity Platform` and `Coverity Desktop`. Those pages explicitly state that source limitation. Structural topics instead contain generated child-topic navigation.

Raw acquisition evidence, preservation hashes, caches, and validation logs are saved under `.local/` and are intentionally excluded from the PR. Existing untracked SRM duplicates, checker lists, evaluation notes, and merge-readiness work remain outside the commit.
