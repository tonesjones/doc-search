---
title: "Refresh LDAP group"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/refresh-ldap-group.html"
content_id: "KBfENaEcs5B1osc3CsLGsA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:12.648528+00:00"
---

# Refresh LDAP group

Example POST request to refresh an LDAP-hosted user group.

**cURL request**

```
curl --location \
--request POST \
"http://my_connect_host:8080/api/v2/ldapConfigurations/refreshGroup" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "domainName": "my_ldap.my_domain.com",
  "ldapServer": "my_ldap.my_domain.com",
  "name": "Group1"
}'
```
