---
title: "Retrieve SAML configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/retrieve-saml-configuration.html"
content_id: "vOHiR1sRkrz_0jGEvqa8gQ"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:08.398606+00:00"
---

# Retrieve SAML configuration

Example GET request to retrieve the SAML configuration.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/samlConfigurations" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "samlConfigurations": [
    {
      "id": 10020,
      "name": "saml",
      "idpUrl": "default_registration_id",
      "entityId": "urn:test:cim:noop",
      "disabled": false,
      "idpMetadataAvailable": true,
      "used": false,
      "groupsEnabled": false
    }
  ],
  "code": null,
  "message": null
}
```
