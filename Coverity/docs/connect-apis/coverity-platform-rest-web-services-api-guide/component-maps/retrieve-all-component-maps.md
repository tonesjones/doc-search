---
title: "Retrieve all component maps"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-all-component-maps.html"
content_id: "hGtwQF4q9r9y6XhY3E7~Vw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:53:39.923136+00:00"
---

# Retrieve all component maps

Example GET request to retrieve all component maps and filter the result set.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/componentMaps" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "componentMaps": [
    {
      "name": "Default",
      "description": "Built in Default component map",
      "componentPathRules": [],
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
          "name": "Default.Other",
          "subscribers": []
        }
      ],
      "defectRules": [
        {
          "componentName": "Default.Other",
          "defaultOwner": null
        }
      ],
      "roleAssignments": []
    },
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
      ]
    }
  ],
  "code": null,
  "message": null
}
}
```
