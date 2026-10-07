---
title: "Configuring readiness probes"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-readiness-probes.html"
content_id: "Yq3GX5TPoq0qbP2IvNbw5g"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-10-04T23:32:23.474123+00:00"
content_hash: "26bcef514ffb7ea15209fb72d31cfee1a1bfb0beb780fe3e3f05a7dc3fd5c0c2"
---

# Configuring readiness probes

You can enable or disable the readiness probes by editing the following boolean flags in `values.yaml`:

```
enableLivenessProbe: true
enableReadinessProbe: true
enableStartupProbe: true
```
