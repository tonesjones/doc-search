---
title: "Retrieve triage history"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-triage-history.html"
content_id: "qGBsna5JYLRX2ql2rqveEg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:07.468985+00:00"
---

# Retrieve triage history

Example GET request to retrieve the triage history of a specified issue.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/issues/triageHistory?\
cid=10003&triageStoreNames=sample-ces-migrator&triageStoreNames=Default%20Triage%20Store" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "triageHistories": [
    {
      "id": 2029,
      "attributeValuesList": [
        {
          "attributeName": "classification",
          "attributeValue": "Pending"
        },
        {
          "attributeName": "action",
          "attributeValue": "Fix Required"
        },
        {
          "attributeName": "fixTarget",
          "attributeValue": "Untargeted"
        },
        {
          "attributeName": "severity",
          "attributeValue": "Minor"
        },
        {
          "attributeName": "legacy",
          "attributeValue": "False"
        },
        {
          "attributeName": "owner",
          "attributeValue": "test0"
        },
        {
          "attributeName": "userCreated",
          "attributeValue": "test2"
        },
        {
          "attributeName": "comment",
          "attributeValue": "Triaged via cov-manage-im"
        },
        {
          "attributeName": "dateCreated",
          "attributeValue": "2015-07-23T07:54:24.366-0600"
        }
      ]
    },
    {
      "id": 2028,
      "attributeValuesList": [
        {
          "attributeName": "classification",
          "attributeValue": "Unclassified"
        },
        {
          "attributeName": "action",
          "attributeValue": "Undecided"
        },
        {
          "attributeName": "fixTarget",
          "attributeValue": "Untargeted"
        },
        {
          "attributeName": "severity",
          "attributeValue": "Minor"
        },
        {
          "attributeName": "legacy",
          "attributeValue": "False"
        },
        {
          "attributeName": "owner",
          "attributeValue": "test0"
        },
        {
          "attributeName": "userCreated",
          "attributeValue": "admin"
        },
        {
          "attributeName": "dateCreated",
          "attributeValue": "2015-07-23T07:54:18.555-0600"
        }
      ]
    },
    {
      "id": 2024,
      "attributeValuesList": [
        {
          "attributeName": "classification",
          "attributeValue": "Unclassified"
        },
        {
          "attributeName": "action",
          "attributeValue": "Undecided"
        },
        {
          "attributeName": "fixTarget",
          "attributeValue": "Untargeted"
        },
        {
          "attributeName": "severity",
          "attributeValue": "Minor"
        },
        {
          "attributeName": "legacy",
          "attributeValue": "False"
        },
        {
          "attributeName": "owner",
          "attributeValue": "test0"
        },
        {
          "attributeName": "userCreated",
          "attributeValue": "admin"
        },
        {
          "attributeName": "dateCreated",
          "attributeValue": "2015-07-23T07:54:18.108-0600"
        }
      ]
    },
    {
      "id": 2021,
      "attributeValuesList": [
        {
          "attributeName": "classification",
          "attributeValue": "Unclassified"
        },
        {
          "attributeName": "action",
          "attributeValue": "Undecided"
        },
        {
          "attributeName": "fixTarget",
          "attributeValue": "Untargeted"
        },
        {
          "attributeName": "severity",
          "attributeValue": "Unspecified"
        },
        {
          "attributeName": "legacy",
          "attributeValue": "False"
        },
        {
          "attributeName": "owner",
          "attributeValue": "test0"
        },
        {
          "attributeName": "userCreated",
          "attributeValue": "admin"
        },
        {
          "attributeName": "dateCreated",
          "attributeValue": "2015-07-23T07:54:05.561-0600"
        }
      ]
    },
    {
      "id": 2011,
      "attributeValuesList": [
        {
          "attributeName": "classification",
          "attributeValue": "Unclassified"
        },
        {
          "attributeName": "action",
          "attributeValue": "Undecided"
        },
        {
          "attributeName": "fixTarget",
          "attributeValue": "Untargeted"
        },
        {
          "attributeName": "severity",
          "attributeValue": "Unspecified"
        },
        {
          "attributeName": "legacy",
          "attributeValue": "False"
        },
        {
          "attributeName": "owner",
          "attributeValue": "test0"
        },
        {
          "attributeName": "userCreated",
          "attributeValue": "admin"
        },
        {
          "attributeName": "dateCreated",
          "attributeValue": "2015-07-23T07:54:05.050-0600"
        }
      ]
    },
    {
      "id": 2005,
      "attributeValuesList": [
        {
          "attributeName": "classification",
          "attributeValue": "Unclassified"
        },
        {
          "attributeName": "action",
          "attributeValue": "Undecided"
        },
        {
          "attributeName": "fixTarget",
          "attributeValue": "Untargeted"
        },
        {
          "attributeName": "severity",
          "attributeValue": "Unspecified"
        },
        {
          "attributeName": "legacy",
          "attributeValue": "False"
        },
        {
          "attributeName": "userCreated",
          "attributeValue": "system"
        },
        {
          "attributeName": "comment",
          "attributeValue": "default triage, overridden by manual triage"
        },
        {
          "attributeName": "dateCreated",
          "attributeValue": "0001-01-01T00:00:00.000-0700"
        }
      ]
    },
    {
      "id": 2015,
      "attributeValuesList": [
        {
          "attributeName": "classification",
          "attributeValue": "Unclassified"
        },
        {
          "attributeName": "action",
          "attributeValue": "Undecided"
        },
        {
          "attributeName": "fixTarget",
          "attributeValue": "Untargeted"
        },
        {
          "attributeName": "severity",
          "attributeValue": "Unspecified"
        },
        {
          "attributeName": "legacy",
          "attributeValue": "False"
        },
        {
          "attributeName": "userCreated",
          "attributeValue": "system"
        },
        {
          "attributeName": "comment",
          "attributeValue": "default triage, overridden by manual triage"
        },
        {
          "attributeName": "dateCreated",
          "attributeValue": "0001-01-01T00:00:00.000-0700"
        }
      ]
    }
  ],
  "code": null,
  "message": null
}
```
