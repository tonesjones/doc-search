---
title: "ANALYZE_CONDITION"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/analyze_condition.html"
content_id: "l3eie13bqPGgMMQUmRK6TA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:56.602798+00:00"
---

# ANALYZE_CONDITION

**Synopsis**

```
ANALYZE_CONDITION() { <code> }
```

**Description**

This handler is called for every conditional expression through which the current path
passes (see Paths for more information). To inspect the
condition, use `MATCH_COND(pat)`. This returns true if the current
condition matches `pat`.

Note: Do not use `MATCH` or
`MATCH_TREE` within `ANALYZE_CONDITION`. The
latter has a *polarity* notion that only `MATCH_COND` can handle
properly.
