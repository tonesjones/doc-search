---
title: "Desktop analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/desktop-analysis.html"
content_id: "twUwmND8c5J2T8I_K_gdvQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:15.619230+00:00"
---

# Desktop analysis

Desktop analysis is a mode of operation that relies on the results of a previous full
analysis. You run desktop analysis using the `cov-run-desktop` command
or your IDE rather than using `cov-analyze`; desktop analysis runs very
quickly because it only re-analyzes the set of files that have changed since the last
central analysis rather than your entire code base.

Unlike incremental analysis, desktop analysis is not guaranteed to produce exactly the
same results as a full analysis from scratch. Many checkers report close to the same
results. But some checkers are disabled because they only work well with full analysis.
Therefore do not assume that a defect that does not show up in desktop analysis was
actually fixed.

Fast desktop mode is especially useful for CI/CD deployments, as described in Running analysis as part of a CI/CD pipeline.
