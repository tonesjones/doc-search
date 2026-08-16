---
title: "Retrieve Coverity Connect license information"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-coverity-connect-license-information.html"
content_id: "sWlyjVfaVNjxoMw7OCwvNA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:14.579607+00:00"
---

# Retrieve Coverity Connect license information

Example GET request to retrieve information about the installed Coverity Connect
license.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/licenses/configuration" \
--header 'Accept: application/json' \
--user my_username:my_password
```

**Response body**

```
{
  "customer": "Acme",
  "expirationDate": "2022-10-23T07:56:10.801-07:00",
  "licenseEditionName": "Enterprise",
  "loc": 2312341,
  "locLimit": 100000000,
  "userCount": 104,
  "userLimit": "3000"
}
```
