---
title: "Deployment scenario — production without scan-services (HTTPS only)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/deployment-scenario-production-without-scan-services-https-only-.html"
content_id: "jZkg_Ti0qD3d8HPSwIX0nQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:36.838144+00:00"
---

# Deployment scenario — production without scan-services (HTTPS only)

When scan-services is disabled and TLS is still required.

```
cim:
  gateway:
    create: true
    enabled: true
    gatewayClassName: "nginx"
    hostnames:
      - "coverity.example.com"
    listeners:
      http:
        enabled: false      # no HTTP listener
      https:
        enabled: true
        port: 443
        tlsSecretName: "coverity-tls"
```
