---
title: "OUTPUT_ERROR"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/output_error.html"
content_id: "_v2ak4ni4xrQTnP0a1M3yg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:54.465841+00:00"
---

# OUTPUT_ERROR

The simplest reporting routine is `OUTPUT_ERROR(<message>)`, where
<message> has an ostream
operator<< to its left. For example:

```
OUTPUT_ERROR("Zounds! " << some_expr << " is " << some_value);
```

This method has properties (a) and (b) from previous, but not (c). It is suitable for
flow-insensitive checkers.
