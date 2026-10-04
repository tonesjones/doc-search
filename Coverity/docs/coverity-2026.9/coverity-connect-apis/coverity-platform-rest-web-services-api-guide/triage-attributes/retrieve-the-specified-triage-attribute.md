---
title: "Retrieve the specified triage attribute"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/retrieve-the-specified-triage-attribute.html"
content_id: "lCV7uV62FwLlN11BoBCw~A"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:10.158595+00:00"
---

# Retrieve the specified triage attribute

Example GET request to retrieve the specified triage attribute.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/triageAttributes/Classification" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "name": "Classification",
  "displayName": "Classification",
  "description": "Classification of defect",
  "displayDescription": "Classification of issue",
  "attributeType": "LIST_OF_VALUES",
  "builtIn": true,
  "defaultValueName": "Unclassified",
  "showInTriage": true,
  "attributeValues": [
    {
      "name": "Unclassified",
      "displayValue": "Unclassified",
      "deprecated": false
    },
    {
      "name": "Pending",
      "displayValue": "Pending",
      "deprecated": false
    },
    {
      "name": "False Positive",
      "displayValue": "False Positive",
      "deprecated": false
    },
    {
      "name": "Intentional",
      "displayValue": "Intentional",
      "deprecated": false
    },
    {
      "name": "Bug",
      "displayValue": "Bug",
      "deprecated": false
    },
    {
      "name": "Untested",
      "displayValue": "Untested",
      "deprecated": false
    },
    {
      "name": "No Test Needed",
      "displayValue": "No Test Needed",
      "deprecated": false
    },
    {
      "name": "Tested Elsewhere",
      "displayValue": "Tested Elsewhere",
      "deprecated": false
    }
  ],
  "code": null,
  "message": null
}
```
