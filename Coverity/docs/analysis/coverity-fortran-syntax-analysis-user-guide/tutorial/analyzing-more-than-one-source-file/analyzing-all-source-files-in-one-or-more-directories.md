---
title: "Analyzing all source files in one or more directories"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/analyzing-all-source-files-in-one-or-more-directories.html"
content_id: "EKrKZHmPq~ba4GzPx75FTw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:49.784160+00:00"
---

# Analyzing all source files in one or more directories

When using the command line, you can use wildcards to specify the source files to be
analyzed, for example:

```
cov-run-fortran --dir idir -- *.f
```

Note: A unix shell will expand filename wildcards before passing
the command line to `cov-run-fortran`. Therefore, local options will
only affect the first file of the expanded list. Global options, specified before
all file names, operate as expected. One can avoid this problem by listing each
source file separately rather than using wildcards. Like many Coverity tools,
`cov-run-forcheck` allows response files to be specified on the
command line. Response files can be used to provide an explicit list of input files
along with the local options affecting each.
