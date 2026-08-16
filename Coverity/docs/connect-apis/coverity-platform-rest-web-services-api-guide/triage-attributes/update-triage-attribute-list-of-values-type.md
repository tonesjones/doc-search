---
title: "Update triage attribute (\"list of values\" type)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/update-triage-attribute-list-of-values-type-.html"
content_id: "szl_KKdO9ooDUzIwMEl1ow"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:07.304467+00:00"
---

# Update triage attribute ("list of values" type)

Example PUT request to update the specified triage attribute.

**cURL request**

```
curl --location \
--request PUT "http://my_connect_host:8080/api/v2/triageAttributes/aa" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "name": "aaa",
  "description": "new description",
  "attributeType": "LIST_OF_VALUES",
  "defaultValueName": "value1",
  "showInTriage": false,
  "attributeValues": [
    {
      "name": "value1",
      "deprecated": true
    },
    {
      "name": "value3",
      "deprecated": false
    }
  ]
}'
```
