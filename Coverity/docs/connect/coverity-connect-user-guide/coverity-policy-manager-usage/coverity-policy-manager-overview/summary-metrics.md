---
title: "Summary metrics"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/summary-metrics.html"
content_id: "hDaDl_gACcCqQPNDy0zgDQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:58.153501+00:00"
---

# Summary metrics

Summary metrics aggregate data from built-in metrics. An example is the built-in summary metric, Technical Debt, which
by default aggregates data from metrics on outstanding issue and function counts. Like
all Summary metrics, its contributor metrics can be filtered (see Filters) and weighted. As shown in Table 1, outstanding issue
metrics are filtered according to their impact, and the function count metric is
filtered according to Cyclomatic Complexity (CCM). The value of each contributor to the
summary metric is weighted by a multiplier to produce a relative value for each
metric.

Table 1. Built-in summary metric: Technical Debt

| Metrics | Label[1] | Filter[2] | Multiplier[3] |
| --- | --- | --- | --- |
| Outstanding Issue Count | High-impact issues | Impact=High | 20 |
| Outstanding Issue Count | Medium-impact issues | Impact=Medium | 10 |
| Outstanding Issue Count | Low-impact issues | Impact=Low | 5 |
| Outstanding Issue Count | Audit-impact issues | Impact=Audit | 1 |
| Function Count | Functions with CCM > 15 | CCM > 15 | 10 |

Note: Before using the Technical Debt summary metric, you should find
out if an administrator has tuned it to meet the needs of your organization.
Alternatively, you can create a test report and select a data point to see what values
are set (see Figure 1).

Technical Debt
:   Technical debt often accrues in code where the demand for rapid
    development can take precedence over established code design and
    development standards. High levels of technical debt can make a code
    base difficult and time-consuming for development teams to successfully
    maintain, modify, and troubleshoot.

Just as the weighted values of the contributor metrics can serve as a data points in your
Coverity Policy Manager charts and heatmaps, so too can the sum of these values. In the
following Technical Debt example (Table 2), the summary
metric value of 80 is simply the sum of its contributor values. The value of each
contributor is equal to the product of its filtered metric and multiplier.

Table 2. Example: Technical Debt of 80

| Technical Debt Contributors[4] | (A) Filtered Metric Value | (B) Multiplier Value | (A x B) Contributor Value | Summary Metric Value |
| --- | --- | --- | --- | --- |
| High-impact issues | 1 | 20 | 20 | 80 (= Sum of Contributor Values) |
| Medium-impact issues | 2 | 10 | 20 |
| Low-impact issues | 4 | 5 | 20 |
| CCM > 15 | 2 | 10 | 20 |

- [1] Administrator-provided name of a filtered metric that serves as a
  contributor to a summary metric. The name appears in charts and
  heatmaps.
- [2] Default filters: Filter outstanding issues by impact, and filter
  functions by complexity.
- [3] Default weight applied to each filtered metric.
- [4]
  **Contributors:** Set of one or more
  filtered metrics and the multipliers used to weight their
  values.

In charts, Summary metrics look and behave much like other metrics. You can select them
as data sources for reports and heatmaps. As shown in the following
examples, you can click nodes and other data points in charts to see their properties,
including the values of contributors that make up Summary metrics.

Figure 1. Example: Summary metric used in a Heatmap
  
 [image: image]

As shown in the following example, it is possible to segment reports by contributors to a
summary metric. (See also, Summary metrics: technical debt.)

Figure 2. Example: Summary metric used in a Status Report
  
 [image: image]

Coverity Policy Manager administrators are responsible for creating and modifying Summary
metrics (see Creating summary metrics).
