---
title: "Response"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/response.html"
content_id: "wpMNwWlFXS_ke6yokaR62Q"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:49.841844+00:00"
---

# Response

The response body contains a JSON array defined by the following name-value pairs.

| Name | Value | JSONPath |
| --- | --- | --- |
| views | **Type:** array  An array whose elements represent the views visible to the current user. | `$.views` |
| id | **Type:** number  Identifier for the view. | `$.views[*].id` |
| type | **Type:** string  The type of view. Describes the type information the view displays in Coverity Connect. | `$.views[*].type` |
| name | **Type:** string  Name of the view. | `$.views[*].name` |
| groupBy | **Type:** boolean  Indicates whether the view's **Group By** option is set.   - `true` – the view's **Group By** option is set. - `false` – the view's **Group By** option is not   set.   For information about the **Group By** view option, see the section "Group By" in the . | `$.views[*].groupBy` |
| columns | **Type:** array  An array whose elements describe the columns included in the view. Each array element is an object with the following name-value pairs:   - `name` – the column's identifier. - `label` – the column's user-visible label. | `$.views[*].columns` |
