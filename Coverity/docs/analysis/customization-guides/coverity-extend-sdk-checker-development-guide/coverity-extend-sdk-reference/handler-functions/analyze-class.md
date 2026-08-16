---
title: "ANALYZE_CLASS"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/analyze_class.html"
content_id: "YKrM29t2SY4qwY3BiEDUsQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:16.487539+00:00"
---

# ANALYZE_CLASS

**Synopsis**

```
ANALYZE_CLASS() { code }
```

**Description**

This function can only be used for `type` checkers. It is called for each class that is
defined in the source code. You can use the `CURRENT_CLASS` macro to get
the class that is undergoing analysis. It has type
`defined_class_type_t`.
