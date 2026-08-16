---
title: "Recommended analysis configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/recommended-analysis-configuration.html"
content_id: "3Wwx~6dIu7tRMtyi2v2acg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:34.569692+00:00"
---

# Recommended analysis configuration

For optimal report results, Coverity recommends that you use the following options to the
`cov-analyze` command when you use Coverity Analysis for C/C++ to
run an analysis on your code:

```
cov-analyze --dir <intermediate_directory> --security --concurrency 
  [--enable-constraint-fpp] [--enable-fnptr]
```

For details about these options, see the `cov-analyze` command
documentation in the Coverity 2026.6.0 Command Reference. Note that the options that are
surrounded by square brackets are optional.
