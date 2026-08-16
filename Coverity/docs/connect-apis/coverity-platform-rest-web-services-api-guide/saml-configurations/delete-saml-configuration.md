---
title: "Delete SAML configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/delete-saml-configuration.html"
content_id: "M3drKHyLxWNDf7WmMpMZtQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:41.405651+00:00"
---

# Delete SAML configuration

Example DELETE request to delete the SAML configuration.

**cURL request**

```
curl --location \
--request DELETE "http://my_connect_host:8080/api/v2/samlConfigurations/my_saml_config" \
--header 'Accept: application/json' \
--user my_username:my_password
```
