---
title: "Create a triage attribute (\"free-form text\" type)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-a-triage-attribute-free-form-text-type-.html"
content_id: "s2FAtIPwQNyv2aeBlhyonA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:05.354370+00:00"
---

# Create a triage attribute ("free-form text" type)

Example POST request to create a triage attribute.

**cURL request**

```
curl --location --request POST "http://my_connect_host:8080/api/v2/triageAttributes" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "name": "bb",
  "description": "test",
  "showInTriage": true,
  "attributeType": "STRING",
  "attributeValues": null,
  "defaultValueName": null
}'
```
