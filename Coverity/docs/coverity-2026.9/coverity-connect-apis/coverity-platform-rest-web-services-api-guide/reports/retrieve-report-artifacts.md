---
title: "Retrieve report artifacts"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/retrieve-report-artifacts.html"
content_id: "dFPXARwoq9UfHEaM~LBSlw"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:07.882133+00:00"
---

# Retrieve report artifacts

Example GET request to retrieve a paginated, sorted, and filtered list of report
artifacts.

## **cURL request**

```
curl -X 'GET' \
  'http://my_connecthost:8080/api/v2/reports?offset=0&rowCount=50&sortColumn=created&sortOrder=desc&status=COMPLETED&status=FAILED&reportType=EU_CRA_REPORT&formatType=ZIP&createdBy=100&projectId=1&streamId=12&snapshotId=456&locale=en_us' \
  -H 'accept: application/json'
```

## **Response body**

```
{
  "offset": 0,
  "totalRows": 42,
  "artifacts": [
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
  ]
}
```
