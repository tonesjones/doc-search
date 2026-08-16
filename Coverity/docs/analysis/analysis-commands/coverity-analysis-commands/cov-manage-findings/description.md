---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "3MHu_vBhY6EFTNy_yey72w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:56.011710+00:00"
---

# Description

The `cov-manage-findings` command enables you to do the following:

- Create a priority filter in a local directory.

  A priority filter is used for filtering out low-importance findings before they
  are persisted as issues.
- Generate a findings report using a locally stored priority filter.

  This report provides a statistical view of what findings would be filtered out by
  the priority filter once the filter is uploaded to the Coverity Connect
  server.
- Upload a priority filter to the Coverity Connect server.

  After being uploaded, the priority filter filters the findings data input to
  `cov-commit-defects` for the specified stream.
- Generate a findings report for a specified stream using a priority filter stored
  in the Coverity Connect server.

  This report provides a statistical view of what findings are filtered out for the
  specified stream when `cov-commit-defects` is executed.

For more details, see "Regulating issue creation" in the Coverity Compliance Guide.
