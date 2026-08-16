---
title: "Azure key"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/azure-key.html"
content_id: "Yiz_I5_pwfVbuCNyQGnR3g"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:55.152479+00:00"
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
