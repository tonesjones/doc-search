---
title: "Importing analysis results from Rapid Scan Static (Sigma)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/importing-analysis-results-from-rapid-scan-static-sigma-.html"
content_id: "DeBsmRfytXp3t~zSnQh8mw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:42.031821+00:00"
---

# Importing analysis results from Rapid Scan Static (Sigma)

Aside from using Rapid Scan Static (Sigma) as an integral part of Coverity, you can also import analysis
results from the standalone engine using the `cov-import-sigma` command.
The workflow is as follows:

```
sigma analyze --format COVERITY --output sigma-output.json src/
cov-import-sigma --dir tmp --sigma-result sigma-output.json
cov-commit-defects --dir tmp <other options>
```

The `cov-commit-defects` command commits the imported results to
Coverity Connect.
