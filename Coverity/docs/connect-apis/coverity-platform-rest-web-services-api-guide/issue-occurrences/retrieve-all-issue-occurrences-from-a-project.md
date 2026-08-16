---
title: "Retrieve all issue occurrences from a project"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-all-issue-occurrences-from-a-project.html"
content_id: "JpVRq_lhp_wjvfzvUZRomQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:00.252857+00:00"
---

# Retrieve all issue occurrences from a project

Example POST request to retrieve all issue occurrences from a project in snapshot
scope.

**cURL request**

```
curl --location \
--request POST \
"http://my_connect_host:8080/api/v2/issueOccurrences/search?includeColumnLabels=true&\
locale=en_us&offset=0&queryType=bySnapshot&rowCount=200&sortOrder=asc" \
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
  "totalRows": 9,
  "columns": [
    "cid"
  ],
  "rows" :[
    [
      {
        "key": "cid",
        "value": "10026"
      }
    ],
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
