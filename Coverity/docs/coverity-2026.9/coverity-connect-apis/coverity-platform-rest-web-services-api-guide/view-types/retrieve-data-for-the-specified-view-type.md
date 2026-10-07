---
title: "Retrieve data for the specified view type"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/retrieve-data-for-the-specified-view-type.html"
content_id: "hKBpjpEINq_AHO5c~wplzQ"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:11.731790+00:00"
---

# Retrieve data for the specified view type

Example POST request to retrieve data for the **files** view type.

**cURL request**

```
curl --location \
--request POST \
"http://my_connect_host:8080/api/v2/files/content" \
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
          "type": "nameMatcher",
          "class": "Project",
          "name": "Insecure"
        }
      ]
    }
  ],
  "columns": [
    "project",
    "file",
    "newCount",
    "cycleCount"
  ],
  "snapshotScope": {
    "show": {
      "scope": "last()",
      "includeOutdatedSnapshots": false
    }
  }
}'
```

**Response
body**

```
{
  "offset": 0,
  "totalRows": 18,
  "columns": [
    "project",
    "file",
    "newCount",
    "cycleCount"
  ],
  "rows": [
    [
      {
        "key": "file",
        "value": "/webapp.war/test.abc"
      },
      {
        "key": "newCount",
        "value": "0"
      },
      {
        "key": "cycleCount",
        "value": "-1"
      }
    ],
    [
      {
        "key": "file",
        "value": "/webapp.war/subdirincludes.jsp"
      },
      {
        "key": "newCount",
        "value": "1"
      },
      {
        "key": "cycleCount",
        "value": "-1"
      }
    ]
  ]
}
```
