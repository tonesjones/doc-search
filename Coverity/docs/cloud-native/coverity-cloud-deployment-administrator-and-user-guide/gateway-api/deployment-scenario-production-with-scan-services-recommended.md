---
title: "Deployment scenario — production with scan-services (recommended)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/deployment-scenario-production-with-scan-services-recommended-.html"
content_id: "HitlbY8GEZKMzYCGjajQNA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:36.176901+00:00"
---

# Deployment scenario — production with scan-services (recommended)

When `scan-services.enabled: true`, CIM pods run a TLS sidecar on port
8443 for pod-to-pod mTLS between scan-services and cimweb. The Gateway backend remains
**port 8080** — the HTTPRoute template hardcodes this unconditionally. The TLS
sidecar on 8443 is used exclusively for the scan-services → cimweb mTLS path, which does
not go through the Gateway.

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
        enabled: true
        port: 80
        redirect: true      # HTTP → HTTPS redirect
      https:
        enabled: true
        port: 443
        tlsSecretName: "coverity-tls"
```

**Resources created:** Gateway (HTTP + HTTPS) + CIM HTTPRoute + redirect HTTPRoute +
commit-server HTTPRoute
