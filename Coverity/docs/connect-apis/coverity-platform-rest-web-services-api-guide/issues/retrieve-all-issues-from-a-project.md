---
title: "Retrieve all issues from a project"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-all-issues-from-a-project.html"
content_id: "q81vaQ1n0JnvWdOPi3rTJQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:04.870121+00:00"
---

# Retrieve all issues from a project

Example POST request to retrieve all issues from a project in snapshot scope.

**cURL request**

```
curl --location \
--request POST "http://my_connect_host:8080/api/v2/issues/search?includeColumnLabels\
=true&locale=en_us&offset=0&queryType=bySnapshot&rowCount=200&sortOrder=asc" \
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
          "class": "Project",
          "name": "testcpp",
          "type": "nameMatcher"
        }
      ]
    }
  ],
  "columns": [
    "cid"
  ]
}'
```

**Response body**

```
{
  "offset": 0,
  "totalRows": 8,
  "columns": [
    "cid"
  ],
  "rows": [
    [
      {
        "key": "cid",
        "value": "10026"
      }
    ],
    [
      {
        "key": "cid",
        "value": "10027"
      }
    ],
    [
      {
        "key": "cid",
        "value": "10028"
      }
    ],
    [
      {
        "key": "cid",
        "value": "10030"
      }
    ],
    [
      {
        "key": "cid",
        "value": "10031"
      }
    ],
    [
      {
        "key": "cid",
        "value": "10032"
      }
    ],
    [
      {
        "key": "cid",
        "value": "10033"
      }
    ],
    [
      {
        "key": "cid",
        "value": "10034"
      }
    ]
  ]
}
```
