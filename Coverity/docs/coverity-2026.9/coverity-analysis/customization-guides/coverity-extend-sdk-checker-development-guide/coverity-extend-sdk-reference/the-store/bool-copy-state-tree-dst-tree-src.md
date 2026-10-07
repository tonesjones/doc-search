---
title: "bool COPY_STATE(tree dst, tree src)"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/bool-copy_state-tree-dst-tree-src-.html"
content_id: "adJxET8aVZN74sLtIgwZvw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:58.169925+00:00"
---

# bool COPY_STATE(tree dst, tree src)

First, calls `CLEAR_STATE(dst)`.

Next, if there is no mapping for `src`, returns `false`.

Otherwise, creates a mapping for `dst`, sets its integer value and event
sequence to equal those of `src`, and returns `true`.
