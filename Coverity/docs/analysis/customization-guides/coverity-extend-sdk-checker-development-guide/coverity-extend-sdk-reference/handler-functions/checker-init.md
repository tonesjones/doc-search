---
title: "CHECKER_INIT"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/checker_init.html"
content_id: "y5ArTCwd~OqqYA1UO_uOqw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:09.923145+00:00"
---

# CHECKER_INIT

**Synopsis**

```
CHECKER_INIT() { <code> }
```

**Description**

This function is called at program startup, after `INIT_OPTIONS` and
`HANDLE_OPTION` have been called. Initialization code, particularly
code that depends on the command-line options, can be placed in this function.
