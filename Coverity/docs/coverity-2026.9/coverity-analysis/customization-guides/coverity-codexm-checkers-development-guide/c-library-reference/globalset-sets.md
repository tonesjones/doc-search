---
title: "'globalset' sets"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/globalset-sets.html"
content_id: "TsH8hUV7K6apYRP00oy29A"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:24.448493+00:00"
---

# 'globalset' sets

The sets described in this section can help narrow the search of your checker.

Typically a `globalset` is used in `for` loop constructions such as the following:

[image: CXM code follows]

```
    for code in globalset allFunctionCode where code matches // ... further criteria
```
