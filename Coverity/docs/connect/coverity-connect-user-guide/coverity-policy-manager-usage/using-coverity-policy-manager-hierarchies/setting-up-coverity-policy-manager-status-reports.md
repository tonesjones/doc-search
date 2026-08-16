---
title: "Setting up Coverity Policy Manager status reports"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/setting-up-coverity-policy-manager-status-reports.html"
content_id: "5mAH46SlNiiyxyJBOqWOUA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:03.977778+00:00"
---

# Setting up Coverity Policy Manager status reports

You can create, edit, share, duplicate, and delete status reports. You can
also save a status report to file and print out hard copies of the file (see Performing common Coverity Policy Manager actions).

The Edit Settings window in the following figure specifies a single metric for a status
report.

Figure 1. Example: Status Report Edit Settings window (single metric)
  
 [image: image]

The chart that results from the preceding example:

Figure 2. Example: resulting Status Report (single metric)
  
 [image: image]

Notice that in the report above, the primary segmentation of the issues is classification
(Unclassified, Pending, Bug) and the secondary segmentation is based on the checkers
that found the issues. The checkers are listed at the bottom of the report.

The Edit Settings window in the following figure specifies two metrics for a status
report. Note that when two metrics are being compared, the secondary segmentation is
automatically set to Metrics.

Figure 3. Example: Status Report Edit Settings window (two metrics)
  
 [image: image]

Figure 4. Example: resulting Status Report (two metrics)
  
 [image: image]

The following table describes the properties that you can specify in the Edit Settings
window for a status report.

Table 1. Status Report properties

| Property | Description |
| --- | --- |
| Name | Unique name for the report. Available to all chart types. |
| Description | Description for the report. Available to all chart types. |
| Metrics | One or more metrics to use in the report. The metric specifies the type of data to use in the data. For example, the chart in Figure 2 reports issues by their classification, and the chart in Figure 1 reports outstanding and resolved issues. You can use the Edit button to set one or more filters on data for a selected metric. For an example, see Figure 2.  Available to all chart types. |
| Chart Type | Chart display options: Bar (data graphed in horizontal bars), Column (data graphed in vertical columns), Pie (data divided into a standard pie chart), table (data listed in a standard table format). |
| [Primary] Segmentation | Primary division of the data found through the specified metric. Available to Bar, Column, and Pie charts only. See also Secondary Segmentation. |
| Secondary Segmentation | Secondary division of the data found through the specified metric. If multiple metrics are selected, this option will be disabled, and the chart will divide data by metric. Available to Bar and Column charts only. See also [Primary] Segmentation. |
| Rows | Primary division of the data found through the specified metric, listed as rows in a table. Available to Table charts only. See also Columns. |
| Columns | Secondary division of the data found through the specified metric, represented as the columns in a table. Available to Table charts only. See also Rows. |
| Stack sections | For reports that specify a Split By property, this property stacks the resulting data segments together (see Figure 2), instead of presenting them side-by-side. Available to Bar and Column charts only. |
| Sort by Value | Option to sort data points from highest to lowest. Available to all chart types. |
| Limit chart to [specified_number_of] categories | Limits the number of Group By categories to display in the chart. Defaults to 40. For example, setting the value to `5` displays only five rows of this category in the resulting spreadsheet. Setting it to `100` displays one hundred rows, and so on.  Typically this option is used for items such as users or checkers, where it might be impractical to display all of them.  See also Show remainder as "Other".  Available to all chart types. |
| Show remainder as "Other" | When using Limit chart to [number_of] categories, you can turn on this option to generate a single Other data point that aggregates values from all categories not otherwise displayed. Available to all chart types. |
| Value axis label | Name that you can prepend to the subtitle of the report. By default, the subtitle displays the values of the Group By and Split By fields. For example, Figure 1 specifies *Issue Count* as the value of this property, so the subtitle displays the following: Issue Count by Classification and Checker. Available to Bar and Column charts only. |
| Value axis range | Numeric range of values to display in the chart. If you set the values to `0`, Coverity Policy Manager will automatically determine the range to use. If the actual values exceed the specified range, the chart will crop the data. Available to Bar and Column charts only. |
| Log Scale | Option to scale data points logarithmically. Typically used to display of large-scale differences between the data points in a practical way. Available to Bar and Column charts only. |

For additional information about creating, editing, sharing, duplicating, and deleting
status reports, see Performing common Coverity Policy Manager actions.
