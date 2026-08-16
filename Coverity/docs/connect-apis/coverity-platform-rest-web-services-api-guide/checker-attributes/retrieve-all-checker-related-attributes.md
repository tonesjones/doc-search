---
title: "Retrieve all checker-related attributes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-all-checker-related-attributes.html"
content_id: "lQFhrLKFAMmJROLAztIMTQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:53:34.253096+00:00"
---

# Retrieve all checker-related attributes

Example GET request to retrieve all checker-related attributes.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/checkerAttributes" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "checkerAttributes": [
    {
      "name": "displayType",
      "displayName": "Type"
    },
    {
      "name": "displayCategory",
      "displayName": "Category"
    },
    {
      "name": "checker",
      "displayName": "Checker"
    }
  ]
}
```
