---
title: "Retrieve all triage attributes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-all-triage-attributes.html"
content_id: "Yiia2jhRIfkWQL4pJnXRLQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:06.676740+00:00"
---

# Retrieve all triage attributes

Example GET request to retrieve all triage attributes.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/triageAttributes" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "attributes": [
    {
      "name": "Action",
      "displayName": "Action",
      "description": "Action to take on defect",
      "displayDescription": "Action to take on issue",
      "attributeType": "LIST_OF_VALUES",
      "builtIn": true,
      "defaultValueName": "Undecided",
      "showInTriage": true,
      "attributeValues": [
        {
          "name": "Undecided",
          "displayValue": "Undecided",
          "deprecated": false
        },
        {
          "name": "Fix Required",
          "displayValue": "Fix Required",
          "deprecated": false
        },
        {
          "name": "Fix Submitted",
          "displayValue": "Fix Submitted",
          "deprecated": false
        },
        {
          "name": "Modeling Required",
          "displayValue": "Modeling Required",
          "deprecated": false
        },
        {
          "name": "Ignore",
          "displayValue": "Ignore",
          "deprecated": false
        }
      ]
    },
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
      ]
    },
    {
      "name": "Ext. Reference",
      "displayName": "Ext. Reference",
      "description": "External Reference",
      "displayDescription": "External Reference",
      "attributeType": "STRING",
      "builtIn": true,
      "defaultValueName": null,
      "showInTriage": true,
      "attributeValues": []
    },
    {
      "name": "Fix Target",
      "displayName": "Fix Target",
      "description": "Release by which the defect should be fixed",
      "displayDescription": "Release by which the issue should be fixed",
      "attributeType": "LIST_OF_VALUES",
      "builtIn": true,
      "defaultValueName": "Untargeted",
      "showInTriage": false,
      "attributeValues": [
        {
          "name": "Untargeted",
          "displayValue": "Untargeted",
          "deprecated": false
        }
      ]
    },
    {
      "name": "Legacy",
      "displayName": "Legacy",
      "description": "Is this a legacy defect",
      "displayDescription": "Is this a legacy defect",
      "attributeType": "LIST_OF_VALUES",
      "builtIn": true,
      "defaultValueName": "False",
      "showInTriage": false,
      "attributeValues": [
        {
          "name": "False",
          "displayValue": "False",
          "deprecated": false
        },
        {
          "name": "True",
          "displayValue": "True",
          "deprecated": false
        }
      ]
    },
    {
      "name": "Severity",
      "displayName": "Severity",
      "description": "Severity of defect",
      "displayDescription": "Severity of issue",
      "attributeType": "LIST_OF_VALUES",
      "builtIn": true,
      "defaultValueName": "Unspecified",
      "showInTriage": true,
      "attributeValues": [
        {
          "name": "Unspecified",
          "displayValue": "Unspecified",
          "deprecated": false
        },
        {
          "name": "Major",
          "displayValue": "Major",
          "deprecated": false
        },
        {
          "name": "Moderate",
          "displayValue": "Moderate",
          "deprecated": false
        },
        {
          "name": "Minor",
          "displayValue": "Minor",
          "deprecated": false
        }
      ]
    }
  ],
  "code": null,
  "message": null
}
```
