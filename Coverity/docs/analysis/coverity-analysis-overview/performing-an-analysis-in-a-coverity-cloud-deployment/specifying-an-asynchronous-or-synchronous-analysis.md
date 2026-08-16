---
title: "Specifying an asynchronous or synchronous analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/specifying-an-asynchronous-or-synchronous-analysis.html"
content_id: "FHJ9WTA_jkd5OKO9oCr2AQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:34.325733+00:00"
---

# Specifying an asynchronous or synchronous analysis

An analysis can be asynchronous or synchronous: You can specify which using the
`COVERITY_CLI_CLOUD_ANALYSIS_ASYNC` environment variable. This
variable determines if the `coverity scan` or `coverity
analyze` command waits for a scan to complete before the command
completes.

- If you specify `COVERITY_CLI_CLOUD_ANALYSIS_ASYNC=true`, the
  analysis is asynchronous. This workflow enables a CI/CD pipeline to continue to
  the next step in the pipeline before the analysis is completed.
- If you specify `COVERITY_CLI_CLOUD_ANALYSIS_ASYNC=false` or any
  other non-true value, the analysis is synchronous. In this workflow, the CI/CD
  pipeline must wait until the analysis is completed before continuing to the next
  step in the pipeline.
