---
title: "Generate EU-CRA compliance report"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/generate-eu-cra-compliance-report.html"
content_id: "rmfDH73y2fEMmEaTZaKpBw"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:07.834753+00:00"
---

# Generate EU-CRA compliance report

Example POST request to generate reports.

## **cURL request**

```
curl -X 'POST' \
  'http://my_connecthost:8080/api/v2/reports/generate?projectName=MyProject&streamName=MyStream&snapshotId=456&reportTypes=EU_CRA_REPORT&reportTypes=CSAF%2FVEX&locale=en_us' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "filters": [
    {
      "columnKey": "string",
      "matchMode": "oneOrMoreMatch",
      "matchers": [
        {}
      ]
    }
  ],
  "snapshotScope": {
    "show": {
      "scope": "last()",
      "includeOutdatedSnapshots": false
    },
    "compareTo": {
      "scope": "",
      "includeOutdatedSnapshots": false
    }
  }
}'
```

## **Response body**

```
{
{
  "jobs": [
    {
      "jobId": 10001,
      "reportType": "EU_CRA_REPORT",
      "status": "PENDING"
    }
  ]
}
```
