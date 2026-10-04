---
title: "Retrieve the specified component"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/retrieve-the-specified-component.html"
content_id: "UtIwSBa~fhNwddIHIRpFkw"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:04.911179+00:00"
---

# Retrieve the specified component

Example GET request to retrieve the specified component.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/components/vsvim-comp.Other"
--header 'Accept: application/json' \
--user my_username:my_password \
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
      "scope": "component",
      "username": null
    }
  ],
  "name": "vsvim-comp.Other",
  "subscribers": [],
  "code": null,
  "message": null
}
```
