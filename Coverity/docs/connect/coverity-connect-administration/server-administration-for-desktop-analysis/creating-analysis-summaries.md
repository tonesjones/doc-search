---
title: "Creating analysis summaries"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/creating-analysis-summaries.html"
content_id: "1~QJoGoX53gRX~_3vQaUUQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:48.732627+00:00"
---

# Creating analysis summaries

Desktop Analysis relies on analysis summary data for accurate and efficient analysis
results. In order to provide this data, it is required that each stream used by Desktop
Analysis have at least one snapshot containing analysis summaries.

Therefore, as part of the stream configuration process, you must complete a full Coverity
Analysis for each stream in your configuration, and commit the results before any
developers can start using Desktop Analysis.

Note: Analysis summaries will be captured
and committed by default, unless the `cov-analyze
--export-summaries` option is explicitly set to
`false`.
