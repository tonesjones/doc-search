---
title: "Examples"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/examples.html"
content_id: "F7vfr8~UMhXJ6PEyuKIo5Q"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:12.095296+00:00"
---

# Examples

**Example request for JSON output**

`curl -G -X PATCH --data
"target_username=my_target_user&target_ldap=my_target_ldap_server.my_domain.com" --user
"admin:pass"
"http://localhost:8080/api/view/v1/username/my_source_user/ldap/my_source_ldap_server.my_domain.com"`

**Example JSON response body**

```
{
  "Updated Views":[
    {
      "owner": {
        "username":"my_target_user",
        "ldapServer":"my_target_ldap_server.my_domain.com"
      },
      "viewkey":"HierarchiesTable",
      "name":"All Hierarchies"
    },
    {
      "owner": {
        "username":"my_target_user",
        "ldapServer":"my_target_ldap_server.my_domain.com"
      },
      "viewkey":"FilesTable",
      "name":"Uncovered By Tests_my_source_user"
    }
  ]
}
```
