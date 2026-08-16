---
title: "Examples"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/examples.html"
content_id: "WWao_z63SlPgEohW16_w3g"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:43.996099+00:00"
---

# Examples

**Example request for JSON output**

`curl -G -X PATCH --data
"username=my_target_user&ldap_server=my_target_ldap_server.my_domain.com" --user
"admin:pass" "http://localhost:8080/api/view/v1/view/10030"`

**Example JSON response body**

```
{
  "Updated View": {
    "owner": {
      "username":"my_target_user",
      "ldapServer":"my_target_ldap_server.my_domain.com"
    },
    "viewkey":"FilesTable",
    "name":"Uncovered By Tests_my_target_user"
  }
}
```
