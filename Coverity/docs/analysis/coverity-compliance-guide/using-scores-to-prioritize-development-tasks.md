---
title: "Using scores to prioritize development tasks"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-scores-to-prioritize-development-tasks.html"
content_id: "kXBz8kD4_ug8QY~09Da~Ag"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:47.505795+00:00"
---

# Using scores to prioritize development tasks

Scoring policies assign priority scores to findings. When you run
`cov-commit-defects`, findings are transformed into issues (with
scores intact) and uploaded to Coverity Connect. Coverity Connect provides a
Score filter and Score column on
relevant views so that you can search, filter, and sort your issues by score.

Note: It's possible for some or all issues not to have scores. Whether your issues have
scores depends on how the compliance filtering policies are configured. Issues without
scores are findings that did not match any scoring policy.
