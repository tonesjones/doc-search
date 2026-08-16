---
title: "Metrics: analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/metrics-analysis.html"
content_id: "r56vnorxazS2e5jzBuIqwg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:06.745489+00:00"
---

# Metrics: analysis

Analysis metrics provide information about the state of software issues (CIDs).

Table 1. Coverity Policy Manager analysis metrics

| Metric | Description | Available To | Filters | Segmentation | Primary Segmentation | Secondary Segmentation |
| --- | --- | --- | --- | --- |
| All issues | Total number of issues in a given node of a hierarchy. | Heatmaps, Status Reports, Trend Reports | Action, Category, Checker, Classification, Coding standards and vulnerability reports, Component, CWE, First Detected, Fix Target, Impact, Issue Kind, Legacy, Owner, Owner Name, Severity, Status, Type Also lists any picklist-type custom attributes. [1] | None, Child Nodes, Action, CWE, Category, Checker, Classification, Coding standards and vulnerability reports,Component, Fix Target, Impact, Legacy, Owner, Owner Name, Severity, Status, Type Also lists any picklist-type custom attributes. |
| Outstanding issue count | Number of CIDs that are classified in Coverity Connect as Unclassified, Pending or Bug. The Untested count is no longer supported since Test Advisor is end-of-life and unsupported as of the 2021.9.0 release. |
| Daily issues introduced | The number of CIDs introduced to a particular stream for the first time in a day. | Trend Reports |
| Daily issues dismissed | Number of CIDs that were dismissed on a given day. |
| Daily issues fixed | Number of CIDs that were fixed on a given day. |
| Outstanding issue density | Number of outstanding issues per 1000 lines of code. | Heatmaps, Status Reports, Trend Reports | Node, Component |
| Daily commit count | Number of snapshots committed to a given node of a hierarchy on a given day. | Trend Reports | Description, Target, Version | Stream, Node |
| Daily issues committed | Number of issues committed to a given node of a hierarchy on a given day. Returns a raw number of issues, with duplicate issues counted separately. |
| Daily lines of code committed | Total number of lines of code committed to a given node of a hierarchy on a given day. Returns a raw number of lines, with duplicate lines of code counted separately. |
| Daily files committed | Number of source code files committed to a given node of a hierarchy on a given day. Returns a raw number of files, with duplicate files counted separately. |

[1] Picklist attributes provide a preconfigured set of
values.
