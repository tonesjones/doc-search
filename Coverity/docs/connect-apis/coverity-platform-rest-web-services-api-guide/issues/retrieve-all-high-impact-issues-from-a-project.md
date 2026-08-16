---
title: "Retrieve all high impact issues from a project"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-all-high-impact-issues-from-a-project.html"
content_id: "Et0f54fcQ_b0hzY9ODGWKA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:04.229240+00:00"
---

# Retrieve all high impact issues from a project

Example POST request to retrieve all high-impact issues from a project in project
scope.

**cURL request**

```
curl --location \
--request POST "http://my_connect_host:8080/api/v2/issues/search?includeColumnLabels\
=true&locale=en_us&offset=0&queryType=byProject&rowCount=200&sortOrder=asc" \
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
    },
    {
      "columnKey": "displayImpact",
      "matchMode": "oneOrMoreMatch",
      "matchers": [
        {
          "key": "High",
          "type": "keyMatcher"
        }
      ]
    }
  ],
  "columns": [
    "action",
    "cid",
    "column_standard_DISA-STIG V4R10",
    "cwe",
    "displayImpact"
  ]
}'
```

**Response body**

```
{
  "offset": 0,
  "totalRows": 3,
  "columns": [
    "action",
    "cid",
    "column_standard_DISA-STIG V4R10",
    "cwe",
    "displayImpact"
  ],
  "rows": [
    [
      {
        "key": "action",
        "value": "Undecided"
      },
      {
        "key": "cid",
        "value": "10030"
      },
      {
        "key": "column_standard_DISA-STIG V4R10",
        "value": "APSC-DV-003215"
      },
      {
        "key": "cwe",
        "value": "457"
      },
      {
        "key": "displayImpact",
        "value": "High"
      }
    ],
    [
      {
        "key": "action",
        "value": "Undecided"
      },
      {
        "key": "cid",
        "value": "10032"
      },
      {
        "key": "column_standard_DISA-STIG V4R10",
        "value": "APSC-DV-002590"
      },
      {
        "key": "cwe",
        "value": "416"
      },
      {
        "key": "displayImpact",
        "value": "High"
      }
    ],
    [
      {
        "key": "action",
        "value": "Undecided"
      },
      {
        "key": "cid",
        "value": "10033"
      },
      {
        "key": "column_standard_DISA-STIG V4R10",
        "value": "APSC-DV-002590"
      },
      {
        "key": "cwe",
        "value": "416"
      },
      {
        "key": "displayImpact",
        "value": "High"
      }
    ]
  ]
}
```
