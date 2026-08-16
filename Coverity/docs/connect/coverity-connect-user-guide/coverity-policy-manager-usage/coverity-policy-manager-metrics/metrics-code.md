---
title: "Metrics: code"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/metrics-code.html"
content_id: "cptyh_Ppni4LTpT3qubSyw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:07.396161+00:00"
---

# Metrics: code

Code metrics provide information about the source code used in your analyses.

Table 1. Coverity Policy Manager code metrics

| Metric | Description | Available To | Filters | Segmentation | Primary Segmentation | Secondary Segmentation |
| --- | --- | --- | --- | --- |
| Lines of code | Number of lines of code in the source code files within the scope of a given node of a hierarchy. Does not include lines fully composed of comments or blank lines in the source code. However, any line that includes both code and a comment counts as a line of code. | Heatmaps, Status Reports, Trend Reports | Component | None, Child Nodes, Component, Detected In See Detected In. |
| Comment lines | Number of lines of comments in the source code files within the scope of a given node of a hierarchy. Does not include comments that occur on lines that also contain source code. |
| Comment density | Comment lines as a proportion of the total lines of code in the source code files. The density is equal to number of comment lines divided by the sum of comment lines and lines of source code. This metric does not include blank lines in the density calculation. |
| Policy coverage | Test Advisor metric for the percentage that is equal to the count of lines covered by tests divided by coverable lines. This metric is no longer supported since Test Advisor is end-of-life and unsupported as of the 2021.9.0 release. |
| Policy covered lines | Test Advisor measure of the number of lines covered by tests. This metric is no longer supported since Test Advisor is end-of-life and unsupported as of the 2021.9.0 release. |
| Policy uncovered lines | Test Advisor measure of the number of lines not covered by tests. This metric is no longer supported since Test Advisor is end-of-life and unsupported as of the 2021.9.0 release. |
| Raw coverage | Test Advisor metric for the percentage that is equal to the raw covered lines divided by raw coverable lines. This metric is no longer supported since Test Advisor is end-of-life and unsupported as of the 2021.9.0 release. |
| Raw covered lines | Test Advisor measure of the number of lines covered by tests, as reported by the coverage tool. This metric is no longer supported since Test Advisor is end-of-life and unsupported as of the 2021.9.0 release. |
| Raw uncovered lines | Test Advisor measure of the number of lines not covered by tests, as reported by the coverage tool. This metric is no longer supported since Test Advisor is end-of-life and unsupported as of the 2021.9.0 release. |
| File count | Number of source code files within the scope of a given node of a hierarchy. Note that files with the same name and file path count as a single file. | Code Lines (LOC), Issue Density, Outstanding, Policy Coverage, Raw Coverage |
| Function count | Number of functions in the source code files within the scope of a given node of a hierarchy. Returns a raw number of functions, with duplicate functions counted separately. | CCM | None, Child Nodes, Component, Cyclomatic Complexity |
