---
title: "Generate health check report"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/generate-health-check-report.html"
content_id: "Za0pisHtyTHDJiT8_rMn8w"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:53:54.453079+00:00"
---

# Generate health check report

Example POST request to generate a health check report on the specified projects and
streams.

**cURL request**

```
curl --location --request POST "http://my_connect_host:8080/api/v2/healthcheck/generate" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "projectAndStreamsList": [ 
    { 
      "projectName": "200 snapshots project", 
      "streamNames": [ 
        "200 snapshot stream" 
      ] 
    } 
  ], 
  "startDate": "2012-04-30", 
  "endDate": "2022-06-28" 
}'
```
