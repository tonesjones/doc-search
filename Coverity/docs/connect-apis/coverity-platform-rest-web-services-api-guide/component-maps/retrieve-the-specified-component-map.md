---
title: "Retrieve the specified component map"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-the-specified-component-map.html"
content_id: "~iDtDQ1Qk0T7oUgfC8rJbg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:53:39.282885+00:00"
---

# Retrieve the specified component map

Example GET request to retrieve the specified component map.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/componentMaps/vxvim-comp" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "name": "vsvim-comp",
  "description": null,
  "componentPathRules": [
    {
      "name": "vsvim-comp.testcomp1",
      "pathPattern": ".*/Src/VimApp/.*"
    },
    {
      "name": "vsvim-comp.testcomp2",
      "pathPattern": ".*/Test/.*"
    }
  ],
  "components": [
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
      "subscribers": []
    },
    {
      "roleAssignments": [
        {
          "group": null,
          "roleAssignmentType": "user",
          "roleName": "developer",
          "scope": "component",
          "username": "foo"
        }
      ],
      "name": "vsvim-comp.testcomp1",
      "subscribers": []
    },
    {
      "roleAssignments": [
        {
          "group": null,
          "roleAssignmentType": "user",
          "roleName": "developer",
          "scope": "component",
          "username": "hoge"
        }
      ],
      "name": "vsvim-comp.testcomp2",
      "subscribers": []
    }
  ],
  "defectRules": [
    {
      "componentName": "vsvim-comp.Other",
      "defaultOwner": null
    },
    {
      "componentName": "vsvim-comp.testcomp1",
      "defaultOwner": "foo"
    },
    {
      "componentName": "vsvim-comp.testcomp2",
      "defaultOwner": "hoge"
    }
  ],
  "roleAssignments": [
    {
      "group": null,
      "roleAssignmentType": "user",
      "roleName": "componentMapOwner",
      "scope": "componentMap",
      "username": "admin"
    }
  ],
  "code": null,
  "message": null
}
```
