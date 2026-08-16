---
title: "Retrieve all LDAP domains"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-all-ldap-domains.html"
content_id: "~Log5v3utWJC75Tj1H1~bw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:11.994606+00:00"
---

# Retrieve all LDAP domains

Example GET request to retrieve all LDAP domains.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/ldapConfigurations/serverDomains" \
--header 'Accept: application/json' \
--user my_username:my_password
```

**Response body**

```
{
  "domains": [
    "sts-ldap.internal.blackduck.com"
  ],
  "code": null,
  "message": null
}
```
