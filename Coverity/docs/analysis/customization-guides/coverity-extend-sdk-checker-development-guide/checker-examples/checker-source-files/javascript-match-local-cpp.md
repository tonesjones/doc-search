---
title: "javascript_match_local.cpp"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/javascript_match_local.cpp.html"
content_id: "X_OFQnAwoJ7KKk9UtFvBVQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:40:10.533936+00:00"
---

# javascript_match_local.cpp

```
#include "extend-lang.hpp"     // Extend API
START_EXTEND_CHECKER( javascript_match_local, simple );
PREFER_TO_ANALYZE_JAVASCRIPT();
ANALYZE_TREE()
{
    LocalVar local1;
    LocalVar local2;
    if (MATCH(local1 = local2))
    {
        OUTPUT_ERROR("Found JavaScript local from " << local2 << " to " << local1);
    }
}
END_EXTEND_CHECKER();
MAKE_MAIN( javascript_match_local )
```
