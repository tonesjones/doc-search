---
title: "Retrieve current sign-in configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-current-sign-in-configuration.html"
content_id: "~we1_9S~ujxOFmcowqyO~A"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:48.497281+00:00"
---

# Retrieve current sign-in configuration

Example GET request to retrieve the current sign-in configuration.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/signInConfigurations" \
--header 'Accept: application/json' \
--user my_username:my_password
```

**Response body**

```
{
  "limitFailedSignIns":null,
  "maxFailedSignInAttempts":null,
  "disableLocalPasswordAuth":null, 
  "allowPasswordRecovery":null,
  "maxSessionIdleTime":null,
  "ldapUserAutoCreate":null,
  "requireLdapGroupMembership":false,
  "authenticationMethod":null,
  "code":null,
  "message":null
}
```
