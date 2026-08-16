---
title: "Retrieve configuration for purge analysis summaries process"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-configuration-for-purge-analysis-summaries-process.html"
content_id: "tmp3No0ylEO0hVJldXx3rw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:21.121597+00:00"
---

# Retrieve configuration for purge analysis summaries process

Example GET request to retrieve the configuration for the "purge analysis summaries"
process.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/maintenance/purgeAnalysisSummaries" \
--header 'Accept: application/json' \
--user my_username:my_password
```

**Response body**

```
{
  "daysBeforePurge": 700, 
  "minSnapshotsToKeep": 300
}
```
