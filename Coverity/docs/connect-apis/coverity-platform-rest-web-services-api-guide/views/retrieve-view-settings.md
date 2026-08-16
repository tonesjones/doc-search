---
title: "Retrieve view settings"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-view-settings.html"
content_id: "X53H7QmvMHs1887O1AW4uw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:25.994332+00:00"
---

# Retrieve view settings

Example GET request to retrieve current settings for the specified view.

**cURL request**

```
curl -X 'GET' \
  'http://localhost:8080/api/v2/views/10024/settings?locale=en_us' \
  -H 'accept: application/json'
```

**Response body**

```
{
  "filters": [
    {
      "columnKey": "string",
      "matchMode": "oneOrMoreMatch",
      "matchers": [
        {}
      ]
    }
  ],
  "columns": [
    "string"
  ],
  "snapshotScope": {
    "show": {
      "scope": "last()",
      "includeOutdatedSnapshots": false
    },
    "compareTo": {
      "scope": "",
      "includeOutdatedSnapshots": false
    }
  },
  "isOccurrenceMode": true,
  "groupByColumn": "string"
}
```
