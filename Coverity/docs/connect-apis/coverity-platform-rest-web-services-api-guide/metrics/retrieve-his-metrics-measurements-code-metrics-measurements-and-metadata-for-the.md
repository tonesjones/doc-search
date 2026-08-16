---
title: "Retrieve HIS-metrics measurements, code-metrics measurements, and metadata for the specified source code file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-his-metrics-measurements-code-metrics-measurements-and-metadata-for-the-specified-source-code-file.html"
content_id: "a15t929Wi~Is1E~e16F57Q"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:24.407543+00:00"
---

# Retrieve HIS-metrics measurements, code-metrics measurements, and metadata for the specified source code file

Example GET request to retrieve HIS-metrics measurements, code-metrics measurements, and
metadata for the specified source code file.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/metrics/files\
?projectName=my_project&streamName=tar115-stream&filePath=/data00/tar-1.15/src/tar.c" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "fileMetrics": {
    "blankLines": 292,
    "codeLines": 1322,
    "commentLines": 144,
    "componentId": 1,
    "componentName": "Other",
    "fullPath": "/data00/tar-1.15/src/tar.c"
  },
  "hisMetrics": {
    "comf": 0.125,
    "cycleCount": 0
  },
  "code": null,
  "message": null
}
```
