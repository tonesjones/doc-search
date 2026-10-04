---
title: "Update triage attribute values"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/update-triage-attribute-values.html"
content_id: "6kRIWzMWh74O5~PkR4CUPQ"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:06.010505+00:00"
---

# Update triage attribute values

Example PUT request to update triage attribute values for the specified issues.

**cURL request**

```
curl --location \
--request PUT "http://my_connect_host:8080/api/v2/issues/triage?\
triageStoreName=Default%20Triage%20Store" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "cids": [
    10003, 10022
  ],
  "attributeValuesList": [
    {
      "attributeName": "Severity",
      "attributeValue": "Major"
    },
    {
      "attributeName": "Action",
      "attributeValue": "Fix Required"
    },
    {
      "attributeName": "Comment",
      "attributeValue": "new comment"
    },
    {
      "attributeName": "Owner",
      "attributeValue": "admin"
    }
  ]
}'
```
