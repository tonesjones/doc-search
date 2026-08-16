---
title: "Update current sign-in configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/update-current-sign-in-configuration.html"
content_id: "jfLOib2oY7pEKYxJgAIE7A"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:49.142534+00:00"
---

# Update current sign-in configuration

Example PUT request to update the current sign-in configuration.

**cURL request**

```
curl --location \
--request PUT "http://localhost:8180/api/v2/signInConfigurations" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "maxFailedSignInAttempts":3
}'
```
