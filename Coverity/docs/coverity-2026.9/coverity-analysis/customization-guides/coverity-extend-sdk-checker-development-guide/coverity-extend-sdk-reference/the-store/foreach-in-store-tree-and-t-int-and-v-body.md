---
title: "FOREACH_IN_STORE(tree &t, int &v) { body }"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/foreach_in_store-tree-t-int-v-body-.html"
content_id: "lcTI64VD0Iyy8g7_Fgo~yA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:58.207524+00:00"
---

# FOREACH_IN_STORE(tree &t, int &v) { body }

For each mapping in the store, bind `t` to the tree and `v`
to the integer component, then execute `body`. The body is syntactically
in a `for` loop, so `break` and `continue`
can be used to control the iteration.

The loop iterates over the mappings in an undefined order.

It is an error to modify the store during the iteration.
