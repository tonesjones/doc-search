---
title: "Retreive code-analysis trends for specified project"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retreive-code-analysis-trends-for-specified-project.html"
content_id: "mF_BqjrWc4uxVdwrfPgCxg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:32.761590+00:00"
---

# Retreive code-analysis trends for specified project

Example GET request to retreive one record of code-analysis measurements for each day in
the specified date range for the `testcpp` project.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/projects/testcpp/trendRecords\
?startDate=2022-07-08&endDate=2022-07-09" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "trendRecords": [
    {
      "blankLineCount": 5262,
      "codeLineCount": 18481,
      "commentLineCount": 10098,
      "dismissedIssueCount": 0,
      "fixedIssueCount": 3,
      "metricsDate": "2022-07-08",
      "newIssueCount": 15,
      "outstandingIssueCount": 15,
      "totalIssueCount": 18,
      "triagedIssueCount": 0,
      "projectName": "testcpp"
    },
    {
      "blankLineCount": 5262,
      "codeLineCount": 18481,
      "commentLineCount": 10098,
      "dismissedIssueCount": 0,
      "fixedIssueCount": 3,
      "metricsDate": "2022-07-09",
      "newIssueCount": 15,
      "outstandingIssueCount": 15,
      "totalIssueCount": 18,
      "triagedIssueCount": 0,
      "projectName": "testcpp"
    }
  ],
  "code": null,
  "message": null
}
```
