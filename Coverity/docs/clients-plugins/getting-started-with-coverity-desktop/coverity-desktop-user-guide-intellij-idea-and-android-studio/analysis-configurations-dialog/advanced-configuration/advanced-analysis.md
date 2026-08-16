---
title: "Advanced: Analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/advanced-analysis.html"
content_id: "sKHgL3xMn5i8NhWg1w95pw"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:48:56.440651+00:00"
---

# Advanced: Analysis

Figure 1. Advanced: Analysis tab
[image: image]

When running Analyze Entire Scope, run all enabled whole program checkers
:   If whole program checkers are defined in the Additional Checker
    Configuration dialog, the analysis will attempt to use them.
    This includes MISRA checkers, web application security checkers, and Android
    security checkers.

Additional cov-run-desktop options
:   Specifies any additional options to be passed to
    `cov-run-desktop` during local analysis.

    These options will be added to those listed under the
    Cov-run-desktop options field. If there is a
    conflict, the options specified here take precedent.

Additional Checker Configuration
:   Two options can be selected here: Enable checkers that find web
    application security vulnerabilities and Enable
    checkers that find Android security vulnerabilities.
