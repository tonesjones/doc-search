---
title: "View-level charts"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/view-level-charts.html"
content_id: "acHILusbFYg_k2UQb5U_pw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:10.586061+00:00"
---

# View-level charts

Views belonging to the Component, Checkers, Owners, and Snapshots view types can display
charts that graph view data. For a list of View types, see Views.

Figure 1 shows a chart for the All In
Project view of the Checkers View type.

Figure 1. Example: View-level column chart
  
 [image: image]

These fields allow you to filter view data:

- Show: For selecting the number of items to display in the chart. Because there
  are a total of `16` matching checkers listed in the View pane,
  Figure 1 selects
  15 to display (instead of using other options in the
  menu, such as `10` or `20`.).
- Values From menu: For filtering by the type of view data
  that you want to display in the chart. For example, Figure 1 displays only the 
  New
   issues in the chart (instead of filtering by other options in this menu:
  Outstanding
   issues, 
  Resolved
   issues, the Total number of issues for a each
  function, or the Line Count of each function).

  Values From menus include countable values that pertain to
  the view filters. For example, the chart for the High Issue Density
  (> 1) view of the Components View type
  includes an Issue Density value in its Values
  From menu because the view uses the Issue
  Density filter to set a density > 1,
  which is a countable value.

  Note that some items, such as a given function name, can occur in numerous source
  code locations, and more than one instance of the function can manifest a
  separate issue (CID). For this reason, it is possible to discover, for example,
  when there is more than one new (untriaged) issue for a given function.
- Chart Type menu: For displaying chart data in vertical
  columns (see Figure 1) or horizontal
  bars.
