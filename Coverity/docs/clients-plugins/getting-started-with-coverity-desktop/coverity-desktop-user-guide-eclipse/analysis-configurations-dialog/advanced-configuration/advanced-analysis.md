---
title: "Advanced: Analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/advanced-analysis.html"
content_id: "a9QNbKUdvPDJpG_vQ8KuXg"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:48:14.420129+00:00"
---

# Advanced: Analysis

Figure 1. Advanced: Analysis tab
[image: image]

When running Analyze Entire Scope, run all enabled whole program checkers
:   If whole program checkers are defined in the Additional Checker
    Configuration dialog, the analysis will attempt to use them.
    This includes coding standard checkers and web application security
    checkers.

Cov-run-desktop options
:   Options passed to `cov-run-desktop` for local analysis.
    These are inherited from the coverity.conf file. See
    the Coverity
    Desktop Analysis
    2026.6.0 User Guide for more information on
    coverity.conf.

Additional cov-run-desktop options
:   Specifies any additional options to be passed to
    `cov-run-desktop` during local analysis.

    These options will be added to those listed under the
    Cov-run-desktop options field. If there is a
    conflict, the options specified here take precedent.

Select File Exclusions...
:   This will take you to the File Exclusions tab.

Use N processor cores
:   Specifies the number of cores to use for parallel analysis. The default is
    the smaller of the number of cores on the machine and the number allowed by
    the license file.
