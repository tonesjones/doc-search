---
title: "Find out whether the database is accepting new commits of analysis results"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/find-out-whether-the-database-is-accepting-new-commits-of-analysis-results.html"
content_id: "jhIsNoMVg4BnWQgrJpaZ3w"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:53:36.293808+00:00"
---

# Find out whether the database is accepting new commits of analysis results

Example GET request to find out whether the database is accepting new commits of analysis
results.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/commitGate/commitState?locale=zh_cn" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "currentCommitCount": 0,
  "isAcceptingNewCommits": false,
  "code": null,
  "message": null
}
```
