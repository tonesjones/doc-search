---
title: "Clone a snapshot"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/clone-a-snapshot.html"
content_id: "1OPZDmULa3N41dF7e5qSmQ"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:09.330584+00:00"
---

# Clone a snapshot

Example POST request to clone a snapshot.

**cURL request**

```
curl -X 'POST' \
  'http://localhost:8080/api/v2/snapshots/clone/10352?createNewTriageStore=true&locale=en_us' \
  -H 'accept: application/json' \
  -d ''
```

**Response body**

```
{
  "analysisCommandLine": "C:\\Program Files\\Coverity\\Coverity Static Analysis\\bin\\cov-analyze.exe --dir 
  C:\\Users\\dwcr\\coverity-idirs \\test -sf C:\\Program Files\\Coverity\\Coverity Static Analysis\\bin\\license.dat 
  --webapp-security --enable-fb",
  "analysisConfiguration": "C:\\Program Files\\Coverity\\Coverity Static Analysis\\config\\coverity_config.xml",
  "analysisHost": "MY_ANALYSIS_HOST_MACHINE",
  "analysisIntermediateDir": "C:\\coverity\\idirs\\my_idir",
  "analysisInternalVersion": "527f76eed9 p-2021.9-push-86",
  "analysisTime": 11,
  "analysisVersion": "2021.06",
  "buildCommandLine": "C:\\Program Files\\Coverity\\Coverity Static Analysis\\bin\\cov-build.exe --coverity-response-file=
  C:\\Users\\dwcr\\idirs\\my_idir\\desktop\\cov-build.rsp bash build.sh -d bash.exe build.sh -d",
  "buildConfiguration": "C:\\Program Files\\Coverity\\Coverity Static Analysis\\config\\coverity_config.xml",
  "buildFailureCount": "0",
  "buildHost": "MY_BUILD_HOST_MACHINE",
  "buildIntermediateDir": "C:\\coverity\\idirs\\my_idir",
  "buildSuccessCount": 2,
  "buildTime": 29,
  "codeVersionDate": "2016-07-17T11:46:38-07:00",
  "commitUser": "my_username",
  "functionsWithModelsPercentage": 28.36,
  "numberOfAnnotations": 10,
  "numberOfCustomModels": 10,
  "sourceFilesCapturedPercentage": 33.36,
  "sourceVersion": "3.5.2",
  "target": "x86_64",
  "description": "My snapshot description.",
  "dateCreated": "2016-07-23T07:56:10.801-07:00",
  "enabledCheckers": [
    "ATOMICITY",
    "BAD_CHECK_OF_WAIT_COND",
    "BAD_LOCK_OBJECT",
    "BAD_SHIFT",
    "CALL_SUPER",
    "CHECKED_RETURN",
    "CONSTANT_EXPRESSION_RESULT",
    "COPY_PASTE_ERROR",
    "DEADCODE",
    "DIVIDE_BY_ZERO",
    "FB.*"
  ],
  "hasSummaries": true,
  "impactHashVersion": 0,
  "portableAnalysisSettings": "string",
  "purgedOfDetails": false,
  "snapshotId": 10010,
  "streamId": 10201,
  "streamName": "my_stream"
}
```
