---
title: "Enable Kubernetes deployment"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/enable-kubernetes-deployment.html"
content_id: "CMKTJhqDpA9Q~M9gxDADvQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:20.807505+00:00"
---

# Enable Kubernetes deployment

For any Coverity deployment in Kubernetes, leave this key value `true`. In
the `cnc` chart, the `cim.cimweb.enabled` key, if
`true`, enables Kubernetes deployment. If `false`,
Kubernetes will not be deployed. By default, this value is `true`:

```
cim:
  cimweb:
    enabled: true
```
