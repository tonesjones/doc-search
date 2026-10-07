---
title: "force_backtrack"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/force_backtrack.html"
content_id: "2mJFQqd3u0w2AVpFpDANow"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:54.902660+00:00"
---

# force_backtrack

Often, an analysis is able to determine that a path is *infeasible*, meaning that it
cannot be executed at run time. This discovery happens when the engine attempts to
traverse through a conditional that is inconsistent with the known facts in the store.
In such cases, the checker can call force_backtrack(), which stops
further exploration of this path.
