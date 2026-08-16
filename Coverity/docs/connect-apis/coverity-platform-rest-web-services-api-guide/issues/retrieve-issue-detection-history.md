---
title: "Retrieve issue detection history"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-issue-detection-history.html"
content_id: "lp1cGbHaA21uCebNyxIEYA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:03.590089+00:00"
---

# Retrieve issue detection history

Example GET request to retrieve the detection history for a specified issue.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/issues/detectionHistory?\
cid=10003&streamName=sample-ces-app" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "detectionHistoryResponseList": [
    {
      "issueDetection": "FIRST_DETECTED",
      "detectionTime": "2013-07-23T07:53:46.288-0600 MDT",
      "inCurrentSnapshot": false,
      "snapshotId": 10001,
      "streamName": "sample-ces-app",
      "username": "admin"
    },
    {
      "issueDetection": "LAST_DETECTED",
      "detectionTime": "2015-07-23T07:55:01.177-0600 MDT",
      "inCurrentSnapshot": true,
      "snapshotId": 10007,
      "streamName": "sample-ces-app",
      "username": "admin"
    }
  ],
  "code": null,
  "message": null
}
```
