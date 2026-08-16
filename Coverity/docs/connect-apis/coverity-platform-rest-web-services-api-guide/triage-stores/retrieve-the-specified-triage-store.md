---
title: "Retrieve the specified triage store"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-the-specified-triage-store.html"
content_id: "9vpHxRtGchN1K8EzpSZH5A"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:10.519487+00:00"
---

# Retrieve the specified triage store

Example GET request to retrieve the specified triage store.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/triageStores/abc" \
--header 'Accept: application/json' \
--user my_username:my_password
```

**Response body**

```
{
  "roleAssignments": [      
    {
      "group": {
        "domainName": null,
        "ldapServer": null,
        "name": "Users"
      },
      "roleAssignmentType": "group",
      "roleName": "developer",
      "scope": "triageStore",
      "username": null
    },
    {
      "group": null,
      "roleAssignmentType": "user",
      "roleName": "triageStoreOwner",
      "scope": "triageStore",
      "username": "admin"
    }
  ],
  "description": "This is a triage store.",
  "name": "abc",
  "streamNames": [
    "testcpp-1"
  ],
  "code": null,
  "message": null
}
```
