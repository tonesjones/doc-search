---
title: "Deployment scenario — development / internal (HTTP only, no TLS)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/deployment-scenario-development/internal-http-only-no-tls-.html"
content_id: "xv~ILjP90SGnB7ESNK60sg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:37.483581+00:00"
---

# Deployment scenario — development / internal (HTTP only, no TLS)

For internal dev clusters where TLS is not required.

Do not use HTTP-only in production.

```
cim:
  gateway:
    create: true
    enabled: true
    gatewayClassName: "nginx"
    hostnames:
      - "coverity.internal"
    listeners:
      http:
        enabled: true
        port: 80
        redirect: false     # no redirect — HTTP only
      https:
        enabled: false      # no HTTPS listener
```

**Resources created:** Gateway (HTTP only) + CIM HTTPRoute (HTTP) + commit-server
HTTPRoute
