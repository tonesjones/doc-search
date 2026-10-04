---
title: "Azure key"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/azure-key.html"
content_id: "Yiz_I5_pwfVbuCNyQGnR3g"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:33.112017+00:00"
---

# Azure key

If the `cache-service.​storageProvider` is `azure`, you
need to set the following Helm key which specifies the Cache Service secret name for
Microsoft Azure. For information on the key, refer to the section, scan-services Helm subchart: Helm keys.

```
cache-service:
  azure:
    secret: ""
```
