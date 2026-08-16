---
title: "Setting up Coverity Policy Manager trend reports"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/setting-up-coverity-policy-manager-trend-reports.html"
content_id: "r57wSyuiAWsy6ZP7DqPZKA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:04.857866+00:00"
---

# Setting up Coverity Policy Manager trend reports

You can create, edit, share, duplicate, and delete Trend reports.

Figure 1. Example: Trend report Edit Settings window
  
 [image: image]

The chart that results from the preceding example:

Figure 2. Example: resulting trend report
  
 [image: image]

The following table describes the properties that you can specify in the Edit Settings
window for a trend report.

Table 1. Trend report poperties

| Property | Description |
| --- | --- |
| Name | Unique name for the report. Available to all chart types. |
| Description | Description for the report. Available to all chart types. |
| Metrics | One or more metrics to use in the report. The metric supplies the report data. For example, see the metric in Figure 1. You can use the Edit button to set one or more filters on data for a selected metric. For an example, see Figure 2.  Available to all chart types. |
| Chart Type | Trend report display options: Area (data graphed in a standard area chart), Line (data points on a standard line graph), Table (data listed in a standard table format). |
| Segmentation | Filter used to subdivide the data points or segments. For example, the trend report in Figure 2 subdivides the data points by triage Action values (Undecided, Fix Required, Fix Submitted, Modeling Required, and Ignore). Note that trend reports automatically group their data by day, so they *do not* provide a configurable Secondary Segmentation field (which is available to status reports).  Available to all chart types. |
| Limit chart to [specified_number_of] categories | Limits the number of Group By categories to display in the chart. Defaults to 40. For example, setting the value to `5` displays only five rows of this category in the resulting spreadsheet. Setting it to `100` displays one hundred rows, and so on.  Typically this option is used for items such as users or checkers, where it might be impractical to display all of them.  See also Show remainder as "Other".  Available to all chart types. |
| Show remainder as "Other" | When using Limit chart to [number_of] categories, you can turn on this option to generate a single Other data point that aggregates values from all categories not otherwise displayed. Available to all chart types. |
| Time Period | Number of days, weeks, or months over which to track changes to the data. Note that each data point in the trend report will represent a day in the specified time period. Available to all chart types. |
| Range | Numeric range of data values to display in the charts. If you set the values to `0`, Coverity Policy Manager will automatically determine the range to use. If the actual values exceed the specified range, the chart will crop the data. Available to Bar and Column charts only. |

For additional information about creating, editing, sharing, duplicating, and deleting
trend reports, see Performing common Coverity Policy Manager actions.
