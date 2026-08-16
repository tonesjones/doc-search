---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "k35txmaQPLySISrryKFp_Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:27.339248+00:00"
---

# Description

The `cov-import-sigma` command allows you to import Sigma output to
Coverity Connect.

Use this command after you use Sigma to analyze your code and to generate the JSON file
containing Sigma output. Use the `cov-commit-defects` command to commit
the imported results to Coverity Connect. For example:

```
> sigma analyze --format COVERITY --output sigma-output.json src/
> cov-import-sigma --dir tmp --sigma-result sigma-output.json
> cov-commit-defects --dir tmp <other options>
```
