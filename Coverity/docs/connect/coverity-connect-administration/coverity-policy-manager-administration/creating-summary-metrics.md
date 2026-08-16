---
title: "Creating summary metrics"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/creating-summary-metrics.html"
content_id: "ysVQt8Ttqta90Oq1cVjyHA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:06.585559+00:00"
---

# Creating summary metrics

You use the Configuration - Summary Metrics screen to create and
maintain Summary metrics that
Coverity Policy Manager users can select for their heatmaps and charts.

By default, you can add up to 10 contributor metrics to a summary metric. You can change this
default through the summary.metric.contributor.limit property in
<install_dir>/config/cim.properties.

Note: **Recommended: Tuning the Technical Debt summary metric**

You
should tune the default values of the Technical Debt
metric to match the needs of your organization, preferably *before* users can
begin to incorporate the metric into their charts. You can change contributor
properties (multipliers, metrics, and/or filters), remove contributors, or add new
contributors, as needed.

Figure 1. Configuration - Summary Metrics screen
  
 [image: image]

Summary metrics consist of the following components:

- Summary Metric Name: The name that you use to identify the
  metric to users.
- Description: A description that you can add to the Summary
  metric.
- Prefix Unit: Optional label (such as the "$" in $100) that
  precedes the value of a given summary metric. This unit is visible in the
  Coverity Policy Manager UI, for example, in the axes of graphs, in table column
  or row headers, and in information boxes that identify data points that appear
  in a chart or heatmap.
- Suffix Unit: Optional label (such as the "K" in 100K,
  which is used an abbrevation used for 100,000) that follows the value of a given
  summary metric. This unit is visible in the Coverity Policy Manager UI, for
  example, in the axes of graphs, in table column or row headers, and in
  information boxes that identify data points that appear in a chart or
  heatmap.
- Contributors: List of one or more filtered metrics that
  you select for your summary metric. To establish the relative importance of a
  given contributor, you need to assign a non-negative, numeric weight as a
  multiplier. For example, the default multipliers used in the built-in summary
  metric, Technical Debt, weight the impact of issues and
  complexity of functions (where CCM refers to Cyclomatic Complexity).

**To add a contributor to a summary metric:**

1. Click the Add Contributor button to open the associated
   edit screen.

   Figure 2. Example: Edit screen for a contributor
     
    [image: image]
2. Select a metric and filter.
3. Provide a label and multiplier for the contributor.

   Using a multiplier of zero (`0`) will disable a
   contributor.

Note: **Removing Summary Metrics**

Use caution when deleting a summary metric. Deleted
Summary metrics disappear without notification from any reports that use them.
Obviously, this change can affect the meaning of a report or, in the case that the
report used only one metric, lead to a completely empty report.
