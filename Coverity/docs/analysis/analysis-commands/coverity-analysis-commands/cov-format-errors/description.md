---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "UX5_lw0EMbFo3nkq7ZUKPA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:52.990574+00:00"
---

# Description

The `cov-format-errors` command reads defects from an intermediate
directory and creates static HTML pages in the specified directory.

**Deprecated behavior**: By default, this command writes HTML
output into the <intermediate_directory>/output/errors
directory, but this usage is deprecated. Instead, you should use the
`--html-output` option to specify the HTML output directory.

To commit defects to Coverity Connect, use cov-commit-defects instead
of `cov-format-errors`.

The output of `cov-format-errors` is only accessible to users who have
access to the local file system; it is not made available through a network service.
