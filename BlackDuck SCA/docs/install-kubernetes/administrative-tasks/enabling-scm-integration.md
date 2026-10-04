---
title: "Enabling SCM Integration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/enabling-scm-integration.html"
content_id: "FfJgZbomlfSNQE482QwVAQ"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-10-04T23:32:23.565265+00:00"
content_hash: "47980f90c0e0202db5258ef75fc8c5670e8b33cb3b3836be40e8a9ad2bb6e5cc"
---

# Enabling SCM Integration

This feature is not enabled by default in Black Duck and must be activated by adding the feature to your Product Registration key and then adding the following in your `values.yaml` file:

```
enableIntegration: true
```

Note: Black Duck does not accept self-signed certificates for SCM integrations at this time.
