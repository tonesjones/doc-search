---
title: "Update LDAP configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/update-ldap-configuration.html"
content_id: "CjmKdXHqnzu_qRJbvoDr2Q"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:10.709816+00:00"
---

# Update LDAP configuration

Example PUT request to update the specified LDAP configuration.

**cURL request**

```
curl --location \
--request PUT \
"http://my_connect_host:8080/api/v2/ldapConfigurations/My%20LDAP%20Configuration" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "anonymousBind": false,
  "baseDN": "my_ldap_base_dn.com",
  "bindName": "cn=Manager",
  "bindPassword": null,
  "groupFilter": null,
  "groupFullName": true,
  "groupMember": "member",
  "groupName": "cn",
  "groupObjectClass": "groupofnames",
  "groupSearchBase": "",
  "name": "My LDAP Configuration",
  "primary": true,
  "secureConnection": false,
  "serverDomain": "my_ldap.my_domain.com",
  "serverPort": 111,
  "tlsEnabled": false,
  "userEmail": "mail",
  "userFirstName": "givenName",
  "userLastName": "sn",
  "userName": "uid",
  "userObjectClass": "inetOrgPerson",
  "userSearchBase": ""
}'
```
