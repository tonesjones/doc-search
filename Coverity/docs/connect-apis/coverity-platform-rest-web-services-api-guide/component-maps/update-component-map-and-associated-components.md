---
title: "Update component map and associated components"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/update-component-map-and-associated-components.html"
content_id: "O5TN~nZf7UjRvn0aJWd_JA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:53:40.574206+00:00"
---

# Update component map and associated components

Example PUT request to update the specified component map and associated components.

**cURL request**

```
curl --location \
--request PUT "http://my_connect_host:8080/api/v2/componentMaps/vsvim-comp" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "name": "vsvim-comp",
  "description": "The description has been changed",
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
}'
```
