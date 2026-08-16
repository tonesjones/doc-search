---
title: "Retrieve information about a snapshot"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-information-about-a-snapshot.html"
content_id: "B05kSuVY0hL4rniJ1wIbQw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:50.438164+00:00"
---

# Retrieve information about a snapshot

Example GET request to retrieve information about the specified snapshot, including
attribute values and commit, build, and analysis details. The snapshot's
`id` path parameter is available in the Coverity Connect GUI.

**cURL request**

```
curl --location \
--request GET "http://localhost:8080/api/v2/snapshots/10261" \
--header 'Accept: application/json' \
--user my_username:my_password
```

**Response body**

```
{
  "analysisCommandLine":"/cov-analysis/bin/cov-analyze --java --dir /intermediate",
  "analysisConfiguration": "/data00/tests/tmp/st-cov-cfg.10871/coverity_config.xml",
  "analysisHost": "sig_os129115611",
  "analysisIntermediateDir": "/data00/7722347/cim-create-ref-db/200Snapshots/interm",
  "analysisInternalVersion": "b36a940395 p-2021.12-push-504",
  "analysisTime": 2,
  "analysisVersion": "2021.12.0",
  "buildCommandLine": "make -j 4 build",
  "buildConfiguration": "/data00/stscovcfg.16107/coverity_config.xml",
  "buildFailureCount": null,
  "buildHost": "10.192.113.151",
  "buildIntermediateDir": "/data00/7722347/cim-create-ref-db/200Snapshots/interm",
  "buildSuccessCount": null,
  "buildTime": 1,
  "codeVersionDate": 1636188136.000000000,
  "commitUser": "admin",
  "sourceVersion": "snapshot 199",
  "target": "x86_64",
  "description": "snapshot 199",
  "dateCreated": 1603183340.548000000,
  "enabledCheckers": [
    "ALLOC_FREE_MISMATCH",
    "ANDROID_CAPABILITY_LEAK",
    "ANONYMOUS_DB_CONNECTION",
    "ARRAY_VS_SINGLETON",
    "ASSERT_SIDE_EFFECT",
    "XPATH_INJECTION",
    "XSS"
  ],
  "hasSummaries": true,
  "impactHashVersion": 0,
  "portableAnalysisSettings": "{\n \"covAnalyzeArgs\" : [\n \"--fb-include\",\n \"coverity-default\",\n \"--enable\",\n \"NULL_RETURNS\"\n  ],\n  \"fileOptions\" : [],\n  \"fileCheckerOptions\" : []\n}\n",
  "purgedOfDetails": false,
  "snapshotId": 10261,
  "streamId": 10301,
  "streamName": my_stream,
  "code": null,
  "message": null
}
```
