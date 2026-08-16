---
title: "Query Parameters"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/query-parameters.html"
content_id: "tO3e3aTp01Tx1MxUeRTujw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:53.762242+00:00"
---

# Query Parameters

| Parameter name | Description |
| --- | --- |
| projectId | **Required.** The numeric or string name identifier of the Coverity Connect project with which the view is associated. |
| rowCount | Maximum number of rows to return in this query. The default value is `100`. To return all rows, set the value to `-1`. |
| offset | Offset to use when accessing rows; this is the number of rows that will be skipped from the top of the sorted results. The default value is `0`. |
| sortKey | Name of the column on which to sort the view. If unspecified, Coverity Connect chooses based on context. |
| sortOrder | Specifies the table's sort direction. Possible values:   - `asc` – ascending - `desc` – descending (Default) |
