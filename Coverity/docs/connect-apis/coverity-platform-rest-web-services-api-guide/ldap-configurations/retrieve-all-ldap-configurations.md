---
title: "Retrieve all LDAP configurations"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-all-ldap-configurations.html"
content_id: "_5f3DkoxDXnkxPne58DMmg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:10.068197+00:00"
---

# Retrieve all LDAP configurations

Example GET request to retrieve all LDAP configurations.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/ldapConfigurations" \
--header 'Accept: application/json' \
--user my_username:my_password
```

**Response body**

```
{
  "configurations": [
    {
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
    }
  ],
  "code": null,
  "message": null
}
```
