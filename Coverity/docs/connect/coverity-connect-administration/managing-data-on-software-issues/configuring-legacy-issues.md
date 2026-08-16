---
title: "Configuring legacy issues"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-legacy-issues.html"
content_id: "Poe0CWaWbdfYFEZTqqwS3g"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:25.989930+00:00"
---

# Configuring legacy issues

A legacy issue is any issue that existed in a company's code base prior to adopting
Coverity Analysis, or one that was undetected prior to completing a Coverity Analysis
upgrade. Differentiating legacy issues from others returned by Coverity Analysis can be
helpful for prioritizing newly introduced issues over those which were part of the
company's backlog.

An issue's legacy status is defined by it's `legacy` attribute, which is
set to `false` by default. To set the legacy status of a set of issues
to `true`, use the `cov-manage-im` command in update
mode, with `--set legacy:True` as an argument. See
`cov-manage-im` in the
Coverity 2026.6.0 Command Reference for more details on legacy issues and the
`cov-manage-im` command.
