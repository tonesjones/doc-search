---
title: "Trigger ETL process"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/trigger-etl-process.html"
content_id: "xoSOzJL4R5tHLS8i5IwVcg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:27.625075+00:00"
---

# Trigger ETL process

Example POST request to trigger the ETL (Extract, Transform, Load) process immediately. This operation can be used to update the current status (for status reports and policies) or to recalculate all historical data (trend reports).

**cURL request (incremental update)**

```
curl --location \
--request POST "http://my_connect_host:8080/api/v2/policyManager/runEtl?rebuildAll=false&locale=en_us" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password
```

**cURL request (full rebuild)**

```
curl --location \
--request POST "http://my_connect_host:8080/api/v2/policyManager/runEtl?rebuildAll=true&locale=en_us" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password
```

**Response body**

```
{
  "code": null,
  "message": "ETL process started."
}
```

**Note:** Set `rebuildAll=true` to delete and recalculate all past and current data (full rebuild). Set `rebuildAll=false` (default) to only update current status (incremental update).
