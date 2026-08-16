---
title: "'globalset' sets"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/globalset-sets.html"
content_id: "7P2eunaFBStS~Mqey8durw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:54.805928+00:00"
---

# 'globalset' sets

The sets described in this section can help narrow the search of your checker.

Typically a `globalset` set is used in `for` loop constructions such as the following:

  
 [image: CXM code follows]   

```
    for code in globalset allFunctionCode where code matches // ... further criteria
```
