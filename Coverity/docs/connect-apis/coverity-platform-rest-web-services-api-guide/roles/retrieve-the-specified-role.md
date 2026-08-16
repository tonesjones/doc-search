---
title: "Retrieve the specified role"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-the-specified-role.html"
content_id: "z7asRgdNxp_bSHLU1ffzHw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:35.329329+00:00"
---

# Retrieve the specified role

Example GET request to retrieve the specified role.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/roles/componentMapOwner" \
--header 'Accept: application/json' \
--user my_username:my_password
```

**Response body**

```
{
  "roles": [
    {
      "name": "componentMapOwner",
      "displayName": "Component Map Owner",
      "description": "componentMapOwner",
      "displayDescription": "Manage component maps",
      "deletable": false,
      "editable": false,
      "permissions": [
        "manageComponentMaps",
        "accessWebUI",
        "viewComponentMaps",
        "accessWS"
      ],
      "displayPermissions": [
        {
          "name": "manageComponentMaps",
          "displayName": "Manage component maps"
        },
        {
          "name": "accessWebUI",
          "displayName": "Log in to Coverity Connect"
        },
        {
          "name": "viewComponentMaps",
          "displayName": "View component maps"
        },
        {
          "name": "accessWS",
          "displayName": "Access web services"
        }
      ]
    }
  ],
  "code": null,
  "message": null
}
```
