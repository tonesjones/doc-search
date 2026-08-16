---
title: "Retrieve column keys for the specified view type"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-column-keys-for-the-specified-view-type.html"
content_id: "Fp_GIU_NxnNRR82of~zZtA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:27.291223+00:00"
---

# Retrieve column keys for the specified view type

Example GET request to retrieve all column keys for the **functions** view type.

**cURL request**

```
curl --location \
--request GET \
"http://my_connect_host:8080/api/v2/functions/columns" \
--user  my_username:my_password \
--header 'Accept: application/json'
```

**Response body**

```
[
  {
    "columnKey": "function",
    "name": "Function"
  },
  {
    "columnKey": "component",
    "name": "Component"
  },
  {
    "columnKey": "newCount",
    "name": "New"
  },
  {
    "columnKey": "outstandingCount",
    "name": "Outstanding"
  },
  {
    "columnKey": "cyclomaticComplexity",
    "name": "CCM"
  },
  ...
]
```
