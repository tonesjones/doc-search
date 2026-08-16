---
title: "Retrieve all users"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-all-users.html"
content_id: "aSCTwX6p0l6rG15DMUfwaw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:17.638851+00:00"
---

# Retrieve all users

Example GET request to retrieve all users.

**cURL request**

```
curl --location --request GET "http://my_connect_host:8080/api/v2/users?locale=en_us" \
--header 'Accept: application/json' \
--user my_username:my_password
```

**Response body**

```
{
  "users": [
    {
      "name": "admin-21",
      "domainName": null,
      "givenName": null,
      "familyName": null,
      "email": "admin-21@acme.com",
      "local": true,
      "locked": false,
      "disabled": false,
      "superUser": false,
      "dateCreated": "2021-08-09T19:28:33.404Z",
      "dateModified": "2021-08-09T19:44:22.414Z",
      "dateDeleted": null,
      "lastLogin": "2021-08-09T19:44:22.412Z",
      "passwordChanged": "2021-08-09T19:28:33.402Z",
      "createdBy": null,
      "modifiedBy": "system",
      "deletedBy": null,
      "groupNames": [
        "Users"
      ],
      "locale": "en_US",
      "roleAssignments": [
        {
          "group": null,
          "roleAssignmentType": "user",
          "roleName": "streamOwner",
          "scope": "stream",
          "username": "admin-21"
        },
        {
          "group": null,
          "roleAssignmentType": "user",
          "roleName": "sysAdmin",
          "scope": "global",
          "username": "admin-21"
        }
      ]
    },
    {
      "name": "fred_friendly",
      "domainName": null,
      "givenName": "Fred",
      "familyName": "Friendly",
      "email": "friendly@golly.com",
      "local": true,
      "locked": false,
      "disabled": false,
      "superUser": false,
      "dateCreated": "2021-07-16T02:04:12.960Z",
      "dateModified": "2021-07-16T02:04:12.963Z",
      "dateDeleted": null,
      "lastLogin": null,
      "passwordChanged": "2021-07-16T02:04:12.957Z",
      "createdBy": null,
      "modifiedBy": "admin",
      "deletedBy": null,
      "groupNames": [
        "Users"
      ],
      "locale": "ko_KR",
      "roleAssignments": [
        {
          "group": null,
          "roleAssignmentType": "user",
          "roleName": "developer",
          "scope": "global",
          "username": "fred_friendly"
        },
        {
          "group": null,
          "roleAssignmentType": "user",
          "roleName": "committer",
          "scope": "global",
          "username": "fred_friendly"
        }
      ]
    }
  ],
  "code": null,
  "message": null
}
```
