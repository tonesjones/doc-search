---
title: "Retrieve issue occurrence counts by category"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-issue-occurrence-counts-by-category.html"
content_id: "uERI3iF~9A~8tBHfpJ6TJQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:00.917580+00:00"
---

# Retrieve issue occurrence counts by category

This example POST request segments all issue occurrences by the `checker`
column and returns the count of issue occurrences per `checker` column
value.

**cURL request**

```
curl --location \
--request POST \
"http://my_connect_host:8080/api/v2/issueOccurrences/searchByCategory?locale=en_us&\
offset=0&queryType=bySnapshot&rowCount=100&groupBy=checker&sortColumn=count" \
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
    }, 
    {
      "columnKey": "displayImpact",
      "matchMode": "noneMatch",
      "matchers": [
        {
          "key": "Medium",
          "type": "keyMatcher"
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
  "groupBy": "checker",
  "rows": [
    {
      "category": "FB.BC_BAD_CAST_TO_ABSTRACT_COLLECTION",
      "count": 1
    },
    {
      "category": "FB.DE_MIGHT_IGNORE",
      "count": 1
    },
    {
      "category": "FB.UUF_UNUSED_FIELD",
      "count": 2
    },
    {
       "category": "FB.UUF_UNUSED_PUBLIC_OR_PROTECTED_FIELD",
       "count": 2
    }
  ]
}
```
