---
title: "Creating Helm overrides to install Scan Service"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/creating-helm-overrides-to-install-scan-service.html"
content_id: "jDHi91M_LUDANDOhrszdzg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:37.756076+00:00"
---

# Creating Helm overrides to install Scan Service

The following sections describe how to create Helm overrides to install and configure
Scan Service.

Important:

When overriding any `scan-services` Helm subchart key from outside the
`scan-services` subchart `values.yaml` file, you
must precede the key name with `scan-services` to identify the key as
a `scan-services` chart key:

```
scan-services:
  cache-service:
    #overrides
  scan-service:
    #overrides
  storage-service:
    #overrides
```

For information on subcharts and overrides, see scan-services Helm subchart and [Subcharts and Global Values](https://helm.sh/docs/chart_template_guide/subcharts_and_globals/).
