---
title: "Update view settings"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/update-view-settings.html"
content_id: "1rBkH7TpaJWSuMukjhczcw"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:11.415645+00:00"
---

# Update view settings

Example PUT request to update settings for specified view.

**cURL request**

```
curl --location \
--request PUT "http://my_connect_host:8080/api/v2/views/MyView/settings?viewType=issuesBySnapshots&showOccurrences=false&groupBy=displayType" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "filters": [
    {
      "columnKey": "displayImpact",
      "matchMode": "oneOrMoreMatch",
      "matchers": [
        {
          "key": "Low",
           "type": "keyMatcher"
        }
      ]
    }
  ],
  "columns": [
    "displayImpact"
  ],
  "snapshotScope": {
    "show": {
      "scope": "first()",
      "includeOutdatedSnapshots": false
    },
    "compareTo": {
      "scope": "last()",
      "includeOutdatedSnapshots": true
    }
  }
}'
```
