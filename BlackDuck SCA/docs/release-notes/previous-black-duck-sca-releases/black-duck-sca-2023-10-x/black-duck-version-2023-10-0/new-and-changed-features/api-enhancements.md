---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "QyVCBIGbzAYeqYns8dhz9A"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:31.507942+00:00"
content_hash: "bb1783f43929b5dba4fb4c3d3e9697d629303a4cbbaa4d31a8774c086ea37d94"
---

# API enhancements

## Enhanced page navigation for REST API requests

REST APIs which returned paged results now provide links to other pages in the same sequence to help with iterating through the data.

## Updated GET /api/jobs-runtimes request

We now include whether or not a job is long running in the `GET /api/jobs-runtimes` response.

```
"longRunningThresholdMs" : 3300,
"longRunning" : false
```

The `longRunningThresholdMs` value determines the runtime threshold for the type of job. A job is considered long running if it exceeds this limit. The `longRunning` value determines whether or not the job is long running based on its runtime and the duration of previous job runs.

## Improved performance for /api/project requests

Performance has been improved on the following API requests:

- `/api/projects/{project id}`
- `/api/projects/{project id}/versions/{version id}/components`
- `/api/projects/{project id}/versions`
