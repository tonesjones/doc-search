---
title: "Retrieve generation status on health check report"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/retrieve-generation-status-on-health-check-report.html"
content_id: "_5lSh_O_mj21PAseRW5Ygw"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:05.286601+00:00"
---

# Retrieve generation status on health check report

Example GET request to retrieve the status of the user's most recent request to generate
a health check report.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/healthcheck/status" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "generated":true,
  "inProgress":false,
  "lastGenerated":"2022-05-17T19:34:31.837Z",
  "status":null,
  "code":null,
  "message":null
}
```
