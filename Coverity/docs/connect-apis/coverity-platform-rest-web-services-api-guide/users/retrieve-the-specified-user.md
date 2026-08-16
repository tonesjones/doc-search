---
title: "Retrieve the specified user"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-the-specified-user.html"
content_id: "i0jCmwh0cleMjO6BSRBdxg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:19.540642+00:00"
---

# Retrieve the specified user

Example GET request to retrieve the specified user.

**cURL request**

```
curl -X 'GET' \
  'http://localhost:8080/api/v2/users/test?locale=en_us' \
  -H 'accept: application/json'
```

**Response body**

```
{
  "users": [
    {
      "createdBy": "string",
      "dateCreated": "2021-02-26T16:48:21.078-07:00",
      "dateDeleted": "2021-02-26T16:48:21.078-07:00",
      "dateModified": "2021-02-26T16:48:21.078-07:00",
      "deletedBy": "string",
      "disabled": true,
      "domainName": "string",
      "email": "string",
      "familyName": "string",
      "givenName": "string",
      "groupNames": [
        "string"
      ],
      "lastLogin": "2021-02-26T16:48:21.078-07:00",
      "local": true,
      "locale": "string",
      "locked": true,
      "modifiedBy": "string",
      "name": "string",
      "passwordChanged": "2021-02-26T16:48:21.078-07:00",
      "roleAssignments": [
        {
          "group": {
            "domainName": "string",
            "ldapServer": "string",
            "name": "string"
          },
          "roleAssignmentType": "group",
          "roleName": "string",
          "scope": "component",
          "username": "string"
        }
      ],
      "superUser": true
    }
  ],
  "totalRowCount": 100
}
```
