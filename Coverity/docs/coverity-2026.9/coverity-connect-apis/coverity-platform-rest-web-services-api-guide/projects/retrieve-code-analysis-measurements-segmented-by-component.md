---
title: "Retrieve code-analysis measurements segmented by component"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/retrieve-code-analysis-measurements-segmented-by-component.html"
content_id: "yfl6StGaYR2dMi2~oV34og"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:07.668852+00:00"
---

# Retrieve code-analysis measurements segmented by component

Example GET request to retrieve code-analysis measurements for two components in the
`testcpp` project.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/projects/testcpp/componentMetrics\
?componentNames=testcpp.Other&componentNames=testcpp.config" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "componentMetrics": [
    {
      "blankLineCount": 4760,
      "codeLineCount": 17521,
      "commentLineCount": 9368,
      "componentName": "testcpp.Other",
      "dismissedIssueCount": 0,
      "fixedIssueCount": 3,
      "metricsDate": "2022-08-16T20:54:57.423Z",
      "newIssueCount": 15,
      "outstandingIssueCount": 15,
      "totalIssueCount": 18,
      "triagedIssueCount": 0
    },
    {
      "blankLineCount": 479,
      "codeLineCount": 900,
      "commentLineCount": 636,
      "componentName": "testcpp.config",
      "dismissedIssueCount": 0,
      "fixedIssueCount": 0,
      "metricsDate": "2022-08-16T20:54:57.423Z",
      "newIssueCount": 0,
      "outstandingIssueCount": 0,
      "totalIssueCount": 0,
      "triagedIssueCount": 0
    }
  ],
  "code": null,
  "message": null
}
```
