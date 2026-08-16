---
title: "Retrieve metadata for all views"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-metadata-for-all-views.html"
content_id: "VqcaalvQ0VGMndDtsp9FCw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:23.436836+00:00"
---

# Retrieve metadata for all views

Example GET request to retrieve metadata for all views. Execution requires the **System
Admin** role at a global level; otherwise returns an error.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/views" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "views": [
    {
      "id": 10016,
      "name": "All In Project",
      "owner": {
        "username": "admin",
        "ldapServer": "local"
      },
      "sharedUsers": [],
      "sharedGroups": [],
      "hasViewNotifications": false,
      "ownerActive": true,
      "ownerDeleted": false
    },
    {
      "id": 10018,
      "name": "All In Project",
      "owner": {
        "username": "admin",
        "ldapServer": "local"
      },
      "sharedUsers": [],
      "sharedGroups": [],
      "hasViewNotifications": false,
      "ownerActive": true,
      "ownerDeleted": false
    },
    {
      "id": 10007,
      "name": "In Latest Snapshot",
      "owner": {
        "username": "admin",
        "ldapServer": "local"
      },
      "sharedUsers": [],
      "sharedGroups": [],
      "hasViewNotifications": false,
      "ownerActive": true,
      "ownerDeleted": false
    },
    {
      "id": 10022,
      "name": "All In Project",
      "owner": {
        "username": "admin",
        "ldapServer": "local"
      },
      "sharedUsers": [],
      "sharedGroups": [],
      "hasViewNotifications": false,
      "ownerActive": true,
      "ownerDeleted": false
    },
    {
      "id": 10023,
      "name": "All In Project",
      "owner": {
        "username": "admin",
        "ldapServer": "local"
      },
      "sharedUsers": [],
      "sharedGroups": [],
      "hasViewNotifications": false,
      "ownerActive": true,
      "ownerDeleted": false
    },
    {
      "id": 10004,
      "name": "All In Project",
      "owner": {
        "username": "admin",
        "ldapServer": "local"
      },
      "sharedUsers": [],
      "sharedGroups": [],
      "hasViewNotifications": false,
      "ownerActive": true,
      "ownerDeleted": false
    },
    {
      "id": 10003,
      "name": "Project Lifetime",
      "owner": {
        "username": "admin",
        "ldapServer": "local"
      },
      "sharedUsers": [],
      "sharedGroups": [],
      "hasViewNotifications": false,
      "ownerActive": true,
      "ownerDeleted": false
    },
    {
      "id": 10024,
      "name": "All Hierarchies",
      "owner": {
        "username": "admin",
        "ldapServer": "local"
      },
      "sharedUsers": [],
      "sharedGroups": [],
      "hasViewNotifications": false,
      "ownerActive": true,
      "ownerDeleted": false
    },
    {
      "id": 10001,
      "name": "All Tests",
      "owner": {
        "username": "admin",
        "ldapServer": "local"
      },
      "sharedUsers": [],
      "sharedGroups": [],
      "hasViewNotifications": false,
      "ownerActive": true,
      "ownerDeleted": false
    },
    {
      "id": 10005,
      "name": "In Latest Snapshot",
      "owner": {
        "username": "admin",
        "ldapServer": "local"
      },
      "sharedUsers": [],
      "sharedGroups": [],
      "hasViewNotifications": false,
      "ownerActive": true,
      "ownerDeleted": false
    },
    {
      "id": 10002,
      "name": "Currently Failing",
      "owner": {
        "username": "admin",
        "ldapServer": "local"
      },
      "sharedUsers": [],
      "sharedGroups": [],
      "hasViewNotifications": false,
      "ownerActive": true,
      "ownerDeleted": false
    },
    {
      "id": 10012,
      "name": "Outstanding Issues",
      "owner": {
        "username": "admin",
        "ldapServer": "local"
      },
      "sharedUsers": [],
      "sharedGroups": [],
      "hasViewNotifications": false,
      "ownerActive": true,
      "ownerDeleted": false
    },
    {
      "id": 10017,
      "name": "All Projects",
      "owner": {
        "username": "admin",
        "ldapServer": "local"
      },
      "sharedUsers": [],
      "sharedGroups": [],
      "hasViewNotifications": false,
      "ownerActive": true,
      "ownerDeleted": false
    },
    {
      "id": 10021,
      "name": "High Issue Density (>1)",
      "owner": {
        "username": "admin",
        "ldapServer": "local"
      },
      "sharedUsers": [],
      "sharedGroups": [],
      "hasViewNotifications": false,
      "ownerActive": true,
      "ownerDeleted": false
    },
    {
      "id": 10020,
      "name": "With Outstanding Issues",
      "owner": {
        "username": "admin",
        "ldapServer": "local"
      },
      "sharedUsers": [],
      "sharedGroups": [],
      "hasViewNotifications": false,
      "ownerActive": true,
      "ownerDeleted": false
    },
    {
      "id": 10019,
      "name": "With Untriaged Issues",
      "owner": {
        "username": "admin",
        "ldapServer": "local"
      },
      "sharedUsers": [],
      "sharedGroups": [],
      "hasViewNotifications": false,
      "ownerActive": true,
      "ownerDeleted": false
    },
    {
      "id": 10015,
      "name": "My Outstanding",
      "owner": {
        "username": "admin",
        "ldapServer": "local"
      },
      "sharedUsers": [],
      "sharedGroups": [],
      "hasViewNotifications": false,
      "ownerActive": true,
      "ownerDeleted": false
    },
    {
      "id": 10014,
      "name": "Outstanding Test Rules Violations",
      "owner": {
        "username": "admin",
        "ldapServer": "local"
      },
      "sharedUsers": [],
      "sharedGroups": [],
      "hasViewNotifications": false,
      "ownerActive": true,
      "ownerDeleted": false
    },
    {
      "id": 10011,
      "name": "High Impact Outstanding",
      "owner": {
        "username": "admin",
        "ldapServer": "local"
      },
      "sharedUsers": [],
      "sharedGroups": [],
      "hasViewNotifications": false,
      "ownerActive": true,
      "ownerDeleted": false
    },
    {
      "id": 10010,
      "name": "Outstanding Untriaged",
      "owner": {
        "username": "admin",
        "ldapServer": "local"
      },
      "sharedUsers": [],
      "sharedGroups": [],
      "hasViewNotifications": false,
      "ownerActive": true,
      "ownerDeleted": false
    },
    {
      "id": 10009,
      "name": "Uncovered By Tests",
      "owner": {
        "username": "admin",
        "ldapServer": "local"
      },
      "sharedUsers": [],
      "sharedGroups": [],
      "hasViewNotifications": false,
      "ownerActive": true,
      "ownerDeleted": false
    },
    {
      "id": 10008,
      "name": "High CCM (>15)",
      "owner": {
        "username": "admin",
        "ldapServer": "local"
      },
      "sharedUsers": [],
      "sharedGroups": [],
      "hasViewNotifications": false,
      "ownerActive": true,
      "ownerDeleted": false
    },
    {
      "id": 10006,
      "name": "Uncovered By Tests",
      "owner": {
        "username": "admin",
        "ldapServer": "local"
      },
      "sharedUsers": [],
      "sharedGroups": [],
      "hasViewNotifications": false,
      "ownerActive": true,
      "ownerDeleted": false
    }
  ],
  "code": null,
  "message": null
}
```
