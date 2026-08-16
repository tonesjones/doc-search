---
title: "Snapshot selection grammar usage notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/snapshot-selection-grammar-usage-notes.html"
content_id: "sO~I~PY79nMJYHLBACFH7A"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:30.674110+00:00"
---

# Snapshot selection grammar usage notes

- `firstAfter()` and `lastBefore()` must have an
  embedded expression (snapshot ID, expression, or date).
- You can use combinations of snapshot IDs, expressions, dates, ranges, and sets in
  the snapshot show/comparison statements. For example:
  - `first()..lastBefore(20023)`
  - `last()..20025`
  - `20021,30031..lastBefore(3 days ago)`
- Use the Show matches button to see to which snapshots the
  grammar maps.
- Coverity Connect will alert you if your snapshot selection grammar is
  incorrect.
- If there are multiple streams in the project, and you use relative expressions,
  Coverity Connect will gather the CIDs that exist in the specified snapshot from
  each stream. For example (using Figure 1), if you specified a show scope of `first()`, Coverity Connect
  will union the CIDs from snapshots 10011,20021, and 30031.
