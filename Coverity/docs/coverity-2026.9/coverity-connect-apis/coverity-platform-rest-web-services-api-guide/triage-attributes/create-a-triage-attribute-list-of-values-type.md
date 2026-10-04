---
title: "Create a triage attribute (\"list of values\" type)"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/create-a-triage-attribute-list-of-values-type-.html"
content_id: "_3tGnuFoScb_13HOXA~QDw"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:10.073816+00:00"
---

# Create a triage attribute ("list of values" type)

Example POST request to create a triage attribute.

**cURL request**

```
curl --location --request POST "http://my_connect_host:8080/api/v2/triageAttributes" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "name": "aa",
  "description": "description",
  "attributeType": "LIST_OF_VALUES",
  "defaultValueName": "value1",
  "showInTriage": true,
  "attributeValues": [
    {
      "name": "value1",
      "deprecated": true
    },
    {
      "name": "value2",
      "deprecated": false
    }
  ]
  }
}'
```
