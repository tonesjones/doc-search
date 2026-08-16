---
title: "MAKE_MAIN"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/make_main.html"
content_id: "a5xr_N3Dfirrvb0ELH0gaw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:07.962790+00:00"
---

# MAKE_MAIN

**Synopsis**

```
MAKE_MAIN( checker_name );
```

**Description**

This macro call defines the `main` function of the entire checker program.
`checker_name` is the name of the checker and should be the same as
the name of the source file (without the `.c` extension).

The call to `MAKE_MAIN` should come directly after the call to 
`END_EXTEND_CHECKER`
, and should be the last statement in the checker source file.
