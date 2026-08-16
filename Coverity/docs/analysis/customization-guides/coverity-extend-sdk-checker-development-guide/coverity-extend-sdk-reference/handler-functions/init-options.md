---
title: "INIT_OPTIONS"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/init_options.html"
content_id: "sS3AJQR9bZFi5Evyqq_rhw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:08.617572+00:00"
---

# INIT_OPTIONS

**Synopsis**

```
INIT_OPTIONS() { code }
```

**Description**

The code in `INIT_OPTIONS` is executed at program startup. Use this code to
initialize member variables declared in section (2). This is the first handler function that is called when the
program starts up (even before `CHECKER_INIT`).
