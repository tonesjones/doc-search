---
title: "Setting up Coverity Policy Manager heatmaps"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/setting-up-coverity-policy-manager-heatmaps.html"
content_id: "4F8p2FicrdsIh2lqIQx8ow"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:02.967630+00:00"
---

# Setting up Coverity Policy Manager heatmaps

You can create, edit, share, duplicate, and delete one or more heatmaps. You can also save a heatmap to a
file and print out hard copies of the file (see Performing common Coverity Policy Manager actions).

Figure 1. Example: Heatmap Edit Settings window
  
 [image: image]

The example shows a heatmap specification in an Edit Settings window. This heatmap sets
an issue density policy where a density between 40 and 43 issues per 1000 lines of code
(1 KLOC) is at risk of violating the policy (and appears in yellow on the heatmap), and
a density over 43 issues per KLOC violates the policy (and appears in red on the
heatmap). A density below 40 issues per KLOC meets the specified policy criteria (and
appears in green on the heatmap). For an example of a heatmap with this specification,
see Figure 1.

Table 1. Heatmap properties

| Property | Description |
| --- | --- |
| Name | Unique name for a Coverity Policy Manager heatmap. |
| Metric | Metric to use for data in the heatmap. For an example, see the metric in Figure 1. |
| Filter | One or more filters on the data to display in the heatmap. Figure 2. Example: Filter Edit Settings window   [image: image]  To open the Edit window for filters, you click the Edit  button in the Filters area (see Figure 1 for an example of this button).  Note: Summary Metrics do not provide filters. |
| Policy | Policy that applies to the data in your heatmap. For an example, see the policy setting in Figure 1. |
| Render As | Display option for a heatmap: Sunburst, Tree, or Trend (Banded Trend map). For the Banded Trend map, you can specify a number of days, weeks, or months over which to plot data. The map displays a data point for each day in the specified period. |

For additional information about creating, editing, sharing, duplicating, and deleting
heatmaps, see Performing common Coverity Policy Manager actions.
