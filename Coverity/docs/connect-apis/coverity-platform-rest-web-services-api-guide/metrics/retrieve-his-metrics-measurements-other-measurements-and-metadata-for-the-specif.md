---
title: "Retrieve HIS-metrics measurements, other measurements, and metadata for the specified function"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-his-metrics-measurements-other-measurements-and-metadata-for-the-specified-function.html"
content_id: "T_xDpP718NeIkf4gbZPokQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:25.060089+00:00"
---

# Retrieve HIS-metrics measurements, other measurements, and metadata for the specified function

Example GET request to retrieve HIS-metrics measurements, other measurements, and
metadata for the specified function.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/metrics/functions?projectName=my_project\
&streamName=tar115-stream&filePath=/data00/tar-1.15/rmt/rmt.c&functionName=main" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "functionMetrics": {
    "backedgeCount": 11,
    "blockCount": 151,
    "componentId": 10004,
    "componentName": "New Component 1",
    "cyclomaticComplexity": 60,
    "forwardedgeCount": 198,
    "fullPath": "/data00/tar-1.15/rmt/rmt.c",
    "halsteadEffort": 74578.1,
    "halsteadErrors": "1.47732",
    "lineCount": 304,
    "operandCount": 139,
    "operationCount": 26,
    "pathCount": "15920",
    "statementPathCount": "500",
    "totalOperandCount": 532,
    "totalOperationCount": 336
  },
  "hisMetrics": {
    "callingCount": 0,
    "callsCount": 27,
    "ccmCount": 60,
    "comf": 0.05844155699014664,
    "gotoCount": 16,
    "levelCount": 16,
    "paramCount": 2,
    "pathCount": 78,
    "returnCount": 9,
    "stmtCount": 154,
    "vocf": 5.260606288909912
  },
  "code": null,
  "message": null
}
```
