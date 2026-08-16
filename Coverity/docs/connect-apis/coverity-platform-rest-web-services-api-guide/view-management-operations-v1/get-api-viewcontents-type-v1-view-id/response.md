---
title: "Response"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/response.html"
content_id: "tPxSzVy0z8Vg60yGq32f6A"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:54.415647+00:00"
---

# Response

The response body contains a JSON object defined by the following name-value pairs.

| Name | Value | JSONPath |
| --- | --- | --- |
| viewContentsV1 | **Type:** object  An object representing the view contents. | `$.viewContentsV1` |
| offset | **Type:** number  The number of rows that were skipped from the top of the sorted results, if any. | `$.viewContentsV1.offset` |
| totalRows | **Type:** number  The total number of rows in the table view, as it exists on Coverity Connect. Depending on the value specified in the `rowCount` query parameter, this value might not match the number of rows in the output. | `$.viewContentsV1.totalRows` |
| columns | **Type:** array  An array whose elements describe the columns included in the view. Each array element is an object with the following name-value pairs:   - `name` – the column's identifier. - `label` – the column's user-visible label. | `$.viewContentsV1.columns` |
| rows | **Type:** array  An array whose elements each describe one row in the view. Each array element is an object with a set of name-value pairs, each of which identifies a column (using the column's `name` value as specified in the `columns` array) and provides a corresponding value, for example, `"cid": 12345`. As such, the set of name-value pairs in each `rows` array element correlates with the set of elements in the `columns` array and varies from view to view. | `$.viewContentsV1.rows` |
