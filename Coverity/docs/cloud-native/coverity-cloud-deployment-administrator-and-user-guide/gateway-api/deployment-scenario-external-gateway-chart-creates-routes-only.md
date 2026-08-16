---
title: "Deployment scenario — external gateway (chart creates routes only)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/deployment-scenario-external-gateway-chart-creates-routes-only-.html"
content_id: "LOE0O2AheUCMzid1R86o8A"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:38.124184+00:00"
---

# Deployment scenario — external gateway (chart creates routes only)

When the Gateway is managed outside of this Helm release (e.g. shared Gateway for
multiple services).

```
cim:
  gateway:
    create: false           # do NOT create a Gateway resource
    enabled: true           # DO create HTTPRoute resources
    name: "shared-gateway"  # name of the existing Gateway
    namespace: "infra"      # namespace where the external Gateway lives
    gatewayClassName: "nginx"
    hostnames:
      - "coverity.example.com"
    listeners:
      https:
        enabled: true
        port: 443
        tlsSecretName: "coverity-tls"
```

**Resources created:** CIM HTTPRoute + commit-server HTTPRoute (no Gateway)
