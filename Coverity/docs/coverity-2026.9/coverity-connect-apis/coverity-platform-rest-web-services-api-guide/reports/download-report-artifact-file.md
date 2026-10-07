---
title: "Download report artifact file"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/download-report-artifact-file.html"
content_id: "vV2qeqDsNqSKocGrnPdxHw"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:07.927314+00:00"
---

# Download report artifact file

Example GET request to stream the generated report file for the given job
ID.

Note: This request is only available when status is COMPLETED.

## **cURL request**

```
curl -X 'GET' \
  'http://my_connecthost:8080/api/v2/reports/10001/download?locale=en_us' \
  -H 'accept: application/octet-stream'
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
