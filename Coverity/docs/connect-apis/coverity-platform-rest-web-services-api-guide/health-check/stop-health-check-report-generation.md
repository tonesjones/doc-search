---
title: "Stop health check report generation"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/stop-health-check-report-generation.html"
content_id: "QuObuaAWpb_LS3LqBHPEVg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:53:55.730113+00:00"
---

# Stop health check report generation

Example DELETE request to stop the generation of an in-progress health check report.

Note: The request must be sent by the same user that sent the request to generate the
report.

**cURL request**

```
curl --location \
--request DELETE "http://my_connect_host:8080/api/v2/healthcheck/stopGeneration" \
--header 'Accept: application/json' \
--user my_username:my_password
```
