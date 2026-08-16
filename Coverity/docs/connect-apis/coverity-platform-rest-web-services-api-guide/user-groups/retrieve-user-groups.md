---
title: "Retrieve user groups"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-user-groups.html"
content_id: "b3zMWLFY~QmaZlHJKN8Vbw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:13.752718+00:00"
---

# Retrieve user groups

Example GET request to retrieve all user groups matching the specified pattern.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8180/api/v2/groups?\
locale=en_us&namePattern=Group*" \
--header 'Accept: application/json' \
--user my_username:my_password
```

**Response body**

```
{
  "groups": [
    {
      "name": {
        "domainName": null,
        "ldapServer": null,
        "name": "Group1"
      },
      "syncEnabled": false,
      "local": true,
      "roleAssignments": [
        {
          "group": {
            "domainName": null,
            "ldapServer": null,
            "name": "Group1"
          },
          "roleAssignmentType": "group",
          "roleName": "visitor",
          "scope": "global",
          "username": null
        }
      ]
    },
    {
      "name": {
        "domainName": null,
        "ldapServer": null,
        "name": "Group2"
      },
      "syncEnabled": false,
      "local": true,
      "roleAssignments": []
    }
  ],
  "code": null,
  "message": null
}
```
