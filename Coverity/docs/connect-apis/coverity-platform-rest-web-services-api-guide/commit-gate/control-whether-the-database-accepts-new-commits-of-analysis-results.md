---
title: "Control whether the database accepts new commits of analysis results"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/control-whether-the-database-accepts-new-commits-of-analysis-results.html"
content_id: "h7XZ4VoBFhvf24OtVm5Rcg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:53:36.946293+00:00"
---

# Control whether the database accepts new commits of analysis results

Example PUT request to close the commit gate so that the database does not accept new
commits of analysis results.

**cURL request**

```
curl --location \
--request PUT "http://my_connect_host:8080/api/v2/commitGate/commitState\
?acceptNewCommits=false&locale=ja_jp" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
```
