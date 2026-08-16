---
title: "False Path Pruning (FPP)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/false-path-pruning-fpp-.html"
content_id: "o5FiO6fsLwtv92a1Shyv2A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:48.643511+00:00"
---

# False Path Pruning (FPP)

Among the reasons for what at first might seem to be unpredictable switching among paths
is false path pruning (FPP). Your Coverity Extend SDK checker is actually
running in conjunction with a number of FPP modules, each of which is looking for
sequences of operations that are inconsistent. For example, in this code:

```
int x = 2;
if (x != 2) {
  // unreachable
}
```

there is an FPP module that detects that the *then* branch of this
conditional cannot be taken. That FPP module calls force_backtrack,
but won't otherwise inform your checker, so that the checker finds the next
ANALYZE_TREE coming from a different path.
