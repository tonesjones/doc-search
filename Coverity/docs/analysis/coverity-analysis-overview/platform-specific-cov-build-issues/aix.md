---
title: "AIX"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/aix.html"
content_id: "N8mcXrlwkFX4~6tA7mDb3w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:11.973967+00:00"
---

# AIX

The `cov-build` and `cov-analyze` commands are not
provided on AIX. Instead, you need to manually integrate the necessary
`cov-translate` commands (see Alternative build command: 'cov-translate') into your build system. For
example:

```
> CC="cov-translate --dir int-dir --run-compile cc" make
```

After running `cov-translate`, you need to copy the resulting
intermediate directory to a different (non-AIX) machine on which a compatible version of
`cov-analyze` is installed and then run the following commands to
complete the analysis:

- `cov-manage-emit` with its non-filtered sub-command
  `reset-host-name`
- `cov-analyze`
