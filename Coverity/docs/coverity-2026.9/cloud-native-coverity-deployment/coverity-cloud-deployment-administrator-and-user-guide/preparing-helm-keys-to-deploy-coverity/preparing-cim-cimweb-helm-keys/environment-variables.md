---
title: "Environment variables"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/environment-variables.html"
content_id: "0OsFizfzb5eRQZNfhDelAA"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:31.618522+00:00"
---

# Environment variables

In the `cnc` chart, the `cim.cimweb.environment` key
enables you to inject additional cimweb environment variables into the container
environment.

```
cim:
  cimweb:
    environment: {}
```

See cnc Helm chart: Helm keys.
