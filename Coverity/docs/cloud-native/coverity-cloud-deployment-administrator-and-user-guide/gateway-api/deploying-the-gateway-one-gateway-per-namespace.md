---
title: "Deploying the gateway: one gateway per namespace"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/deploying-the-gateway-one-gateway-per-namespace.html"
content_id: "QE2NUdSQ0WIjGW7AfqkKEg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:29.702452+00:00"
---

# Deploying the gateway: one gateway per namespace

There are two ways to deploy the Gateway for CNC. Choose based on whether each namespace
should own its Gateway or whether a central Gateway should serve multiple
namespaces.

The following Helm values create a gateway for a namespace:

**Helm values for each namespace:**

```
cim:
  gateway:
    create: true    # chart creates Gateway in this namespace
    enabled: true   # chart creates HTTPRoutes
    name: ""        # auto-derived as "<release>-gateway"
```

[image: image]

Each namespace has its own external IP and TLS cert. Namespaces are fully isolated.
Misconfig one does not affect the other.
