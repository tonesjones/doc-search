---
title: "Delete a report job"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/delete-a-report-job.html"
content_id: "XhGtcxJHh5KB_eQBVcZNRA"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:08.016597+00:00"
---

# Delete a report job

Example GET request to delete a report job and its associated artifact
file.

Note: Jobs with status IN_PROGRESS cannot be deleted.

## **cURL request**

```
curl -X 'DELETE' \
  'http://my_connecthost:8080/api/v2/reports/10001?locale=en_us' \
  -H 'accept: */*'
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
