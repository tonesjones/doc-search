---
title: "Enabling SCM Integration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/enabling-scm-integration.html"
content_id: "MwhrCY~9uCd3Tmr~OdRLrQ"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:23.249022+00:00"
---

# Enabling SCM Integration

This feature is not enabled by default in Black Duck and must be activated by adding the
feature to your Product
Registration key and then adding the following in your
`values.yaml` file:

```
enableIntegration: true
```

Note: Black Duck does not accept self-signed certificates for SCM integrations at this
time.
