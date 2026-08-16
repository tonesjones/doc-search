---
title: "Disabling the scan-services Helm subchart for a Connect-only deployment"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/disabling-the-scan-services-helm-subchart-for-a-connect-only-deployment.html"
content_id: "RcUZjGQjd3glYbweauhbQA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:26.687764+00:00"
---

# Disabling the scan-services Helm subchart for a Connect-only deployment

If you are deploying ONLY Coverity Connect in the Kubernetes cluster, verify that the
`scan-services.enabled` Helm key, located in the `cnc`
chart, is set to `false`. This disables use of the
`scan-services` Helm subchart and prevents deployment of Scan
Services.

```
scan-services:
  enabled: false
```

See also scan-services.enabled Helm key.
