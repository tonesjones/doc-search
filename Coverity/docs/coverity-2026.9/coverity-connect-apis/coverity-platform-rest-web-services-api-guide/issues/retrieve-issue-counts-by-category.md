---
title: "Retrieve issue counts by category"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/retrieve-issue-counts-by-category.html"
content_id: "3qvh67bvBBeeBGVRNJFgPA"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:05.922396+00:00"
---

# Retrieve issue counts by category

This example POST request segments all issues by the `severity` column and
returns the issue count per `severity` column value.

**cURL request**

```
curl --location \
--request POST "my_connect_host:8080/api/v2/issues/searchByCategory?locale=en_us\
&offset=0&queryType=bySnapshot&rowCount=100&groupBy=severity&sortColumn=count\
&sortOrder=desc" \
--user  my_username:my_password \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data-raw \
'{
  "filters": [
    {
      "columnKey": "project",
      "matchMode": "oneOrMoreMatch",
      "matchers": [
        {
          "id": "10002",
          "type": "idMatcher"
        }
      ]
    }
  ],
  "snapshotScope": {
    "show": {
      "scope": "10004,10007",
      "includeOutdatedSnapshots": false
    },
    "compareTo": {
      "scope": "10001",
      "includeOutdatedSnapshots": false
    }
  }
}'
```

**Response body**

```
{
  "offset": 0,
  "totalRows": 4,
  "groupBy": "severity",
  "rows": [
    {
      "category": "Unspecified",
      "count": 8
    },
    {
      "category": "Moderate",
      "count": 6
    },
    {
      "category": "Major",
      "count": 1
    },
    {
      "category": "Minor",
      "count": 1
    }
  ]
}
```
