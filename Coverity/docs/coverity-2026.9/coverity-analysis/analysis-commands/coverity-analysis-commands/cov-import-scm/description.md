---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/description.html"
content_id: "gBSjszOrXbkOsQ7lC2nA~A"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:51.334854+00:00"
---

# Description

The `cov-import-scm` command simplifies the process of retrieving the
SCM change data for source files and adding them to the emit directory. This command
automates the following command line flow:

1. `cov-manage-emit list-scm-unknown`
2. `cov-extract-scm`
3. `cov-manage-emit add-scm-annotations`
