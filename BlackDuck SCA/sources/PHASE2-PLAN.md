# Phase 2 plan — companion product docs

## Scope (user-confirmed)

| Include | Product | Pin | Map ID | ~Topics |
|---------|---------|-----|--------|--------:|
| Yes | Detect | 11.5.1 | bMVbOgKqSRm_N11~2Mv5gg | 206 |
| Yes | Alert | 8.4.0 | QEB0e_qPG~BdIwQfv5eDZQ | 45 |
| Yes | Bridge CLI | latest | ilBVZr_kR5v3KVjK1p~wbw | 174 |
| Optional | Air-gapped KB | latest | YsDtm_HKwGM6efkx~2HVvQ | 15 |
| No (sibling repos) | Coverity, Polaris | — | — | Live under `C:\TestCode\Product Docs\Coverity` and `...\Polaris`; do not scrape here |
| No | BDBA, Tools, Artifactory, Code Sight, other portal products | — | — | Not scraped yet |

## Prerequisites

- Phase 1 SCA 2026.7 corpus complete (941 topics).
- Current scripts hard-code map `1WqD3iF0wWDzpOGfy2mr8Q`; generalize before scraping.

## Implementation steps (next session)

1. Multi-map support in `scripts/build-index.py` and `scripts/scrape-pending.py` (mapId, version, source dir, docs root).
2. Init + scrape Detect → Alert → Bridge.
3. Optionally scrape Air-gapped KB.
4. Update `index.md` (or per-product indexes), `AGENTS.md`, `CHECKPOINT.md`.

## Estimate

~425 topics core (~15–30 min); +15 optional air-gap.
