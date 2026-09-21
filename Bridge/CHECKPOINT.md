# Bridge CLI corpus checkpoint

**Last updated:** 2026-09-19
**Status:** Complete standalone Bridge corpus; use local Markdown for product questions.

## Initial import

- Scraped **174/174** topics with **0 errors** from map `ilBVZr_kR5v3KVjK1p~wbw`.
- Content is stored under `docs/`, with TOC and manifest under `sources/bridge-latest/`.

## Standalone move (DS-02) — 2026-09-19

- Moved out of the Black Duck SCA tree (`BlackDuck SCA/docs/bridge/`,
  `BlackDuck SCA/sources/bridge-latest/`, `BlackDuck SCA/index-bridge.md`) into the
  top-level `Bridge/` corpus.
- Flattened the docs layout: `docs/bridge/<section>/…` → `docs/<section>/…`
  (manifest `localPath` values rewritten by prefix strip; topic bodies byte-identical).
- Copied the standalone corpus tooling into `Bridge/scripts/` and registered
  `bridge-latest` as the default product (`docs_root: None`, `index.md`).
- Bridge is a top-level product corpus. It must not be merged into the Black Duck SCA tree.

## Next action

Refresh Bridge only when a version/content check is requested. Preserve this `latest`
snapshot and its history rather than overwriting it with another product corpus.
