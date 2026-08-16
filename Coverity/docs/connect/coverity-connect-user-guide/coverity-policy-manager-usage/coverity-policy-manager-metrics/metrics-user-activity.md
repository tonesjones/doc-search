---
title: "Metrics: user activity"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/metrics-user-activity.html"
content_id: "y2NNiJ028wkXAOfvk59n8w"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:06.135694+00:00"
---

# Metrics: user activity

User activity metrics track usage of the Coverity Connect UI as it pertains software
issues, which are identified by a CID.

Table 1. Coverity Policy Manager user activity metrics

| Metric | Description | Available To[1] | Filters[2] | Segmentation | Primary Segmentation | Secondary Segmentation[3] |
| --- | --- | --- | --- | --- |
| Daily unique users | Number of unique users within the set of Daily unique issue views on a given day. For example, assume that a total of 2 different users viewed one or more CIDs on a day that the Daily unique issue views is 5. In this case, Daily unique users is 2 for that day. See also Monthly unique users. | Trend Reports | Component, Owner, Owner Name | None, Child Nodes, Component, Owner, Owner Name |
| Daily unique issue views | Total number of unique issues viewed by a unique user in the Coverity Connect Triage pane on a given day. If 5 different users view the same CID on the same day, this metric counts 5 separate unique views (of that CID). If a single user views 5 different CIDs on the same day, this metric counts these actions as 5 separate unique views. If a single user views the same CID a total of 5 separate times in one day, this metric counts only 1 unique view (of this CID for this user). |
| Daily unique issue views per user | Number of Daily unique issue views divided by the Daily unique users. Assume the following occurs on the same day: User 1 inspects CID 11 and CID 22. User 2 inspects CID 22. In this case, this metric is 1.5 (because the Daily unique issue views is 3, and the Daily unique users is 2). |
| Daily unique issue triages | Total number of unique CIDs that have been triaged by a unique user on a given day. Like Daily unique issue views, this metric counts unique CID and user combinations. If the same CID is triaged by the same user more than once on a given day, this metric counts only one triage action (for this CID), regardless of whether the user changed the values of different triage attributes. |
| Monthly unique users | The number of unique users per month. For example, if for ten days there is only one unique user per day (and the rest of the days in the month have zero unique users), the monthly unique users could be anywhere betwen 1 and 10, depending on whether the same user visited on ten different days (monthly unique users = 1), or ten different users visited during that period (monthly unique users = 10), or some number between 1 and ten. |

- [1] Lists of charts to which the metric is available: Heatmaps,
  Status Reports, and/or Trend Reports.
- [2] List of filters that you can apply to the data retrieved by the
  metric. For descriptions of filters, see Coverity Policy Manager filter and segmentation properties.
- [3] List of Segmentation, Primary
  Segmentation or Secondary
  Segmentation properties that you can apply to
  the chart data. For descriptions of these properties, Coverity Policy Manager filter and segmentation properties.
