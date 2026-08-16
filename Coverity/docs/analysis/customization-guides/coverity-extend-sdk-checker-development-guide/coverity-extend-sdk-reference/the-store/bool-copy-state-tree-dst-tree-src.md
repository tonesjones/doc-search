---
title: "bool COPY_STATE(tree dst, tree src)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/bool-copy_state-tree-dst-tree-src-.html"
content_id: "adJxET8aVZN74sLtIgwZvw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:39.069806+00:00"
---

# bool COPY_STATE(tree dst, tree src)

First, calls `CLEAR_STATE(dst)`.

Next, if there is no mapping for `src`, returns `false`.

Otherwise, creates a mapping for `dst`, sets its integer value and event
sequence to equal those of `src`, and returns `true`.
