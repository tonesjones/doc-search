---
title: "Retrieve specific report"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/retrieve-specific-report.html"
content_id: "AU0mNTtCMoSe0~Ih4jcBrg"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:07.971370+00:00"
---

# Retrieve specific report

Example GET request to returns a single artifact by job ID with full
details.

## **cURL request**

```
curl -X 'GET' \
  'http://my_connecthost:8080/api/v2/reports/10001?locale=en_us' \
  -H 'accept: application/json'
```

## **Response body**

```
{
  "artifactId": 20001,
  "jobId": 10001,
  "status": "COMPLETED",
  "fileName": "eu-cra-report-stream12-20260707.zip",
  "formatType": "ZIP",
  "reportType": "EU_CRA_REPORT",
  "fileSizeBytes": 1048576,
  "createdBy": {
    "id": 100,
    "name": "jdoe",
    "displayName": "Jane Doe"
  },
  "created": "2026-07-07T14:35:00Z",
  "finished": "/api/v2/reports/10001/download",
  "projectId": 1,
  "streamId": 12,
  "snapshotId": 456
}
```
