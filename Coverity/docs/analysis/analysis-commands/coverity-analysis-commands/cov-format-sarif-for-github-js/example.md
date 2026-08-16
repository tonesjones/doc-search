---
title: "Example"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/example.html"
content_id: "eTh79PB7JGTzFwZg65Aunw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:58.400315+00:00"
---

# Example

Suppose that `https://github.com/WebGoat/WebGoat/commit/
121212121212121212121212121212121212121212` is checked out to directory
webgoat/src.

Next, the directory webgoat/src is captured, analyzed, and the results are
formatted by `cov-format-errors --json-output-v10` to get
webgoatResults.json.

SARIF for GitHub will be generated in the file webgoatSARIF.json by the
following command:

```
node cov-format-sarif-for-github.js \
--inputFile webgoatResults.json \
--outputFile webgoatSARIF.json \
--githubUrl https://github.com \
--repoName WebGoat/WebGoat \
--checkoutPath WebGoat/WebGoat webgoat/src 1212121212121212121212121212121212121212
```
