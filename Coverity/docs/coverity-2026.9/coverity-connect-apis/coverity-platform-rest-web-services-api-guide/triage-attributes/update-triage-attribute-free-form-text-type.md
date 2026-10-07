---
title: "Update triage attribute (\"free-form text\" type)"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/update-triage-attribute-free-form-text-type-.html"
content_id: "PpEBvG~fx98aWvbq9ljvEw"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:10.286812+00:00"
---

# Update triage attribute ("free-form text" type)

Example PUT request to update the specified triage attribute.

**cURL request**

```
curl --location \
--request PUT "http://my_connect_host:8080/api/v2/triageAttributes/bb" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "name": "bbb",
  "description": " new description",
  "showInTriage": false,
  "attributeType": "STRING",
  "attributeValues": null,
  "defaultValueName": null
}'
```
