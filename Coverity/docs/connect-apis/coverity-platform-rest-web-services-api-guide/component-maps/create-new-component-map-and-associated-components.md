---
title: "Create new component map and associated components"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-new-component-map-and-associated-components.html"
content_id: "txpcCNAev4f7p9svTMAB4g"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:53:38.639484+00:00"
---

# Create new component map and associated components

Example POST request to create a new component map and associated components.

**cURL request**

```
curl --location --request POST "http://my_connect_host:8080/api/v2/componentMaps" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "name": "my-component-map", 
  "description": "This is my component map description.",
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
      "name": "my-component-map.assignment_one",
      "subscribers": []
    }
  ],
  "defectRules": [
    {
      "componentName": "my-component-map.defect_rule_one",
      "defaultOwner": null
    }
  ],
  "code": null,
  "message": null
}'
```
