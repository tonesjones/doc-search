---
title: "Delete LDAP configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/delete-ldap-configuration.html"
content_id: "W~7IkCGaQJKpTMMLcrj1wA"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:06.313052+00:00"
---

# Delete LDAP configuration

Example DELETE request to delete the specified LDAP configuration.

**cURL request**

```
curl --location \
--request DELETE \
"http://my_connect_host:8080/api/v2/ldapConfigurations/My%20LDAP%20Configuration" \
--header 'Accept: application/json' \
--user my_username:my_password
```
