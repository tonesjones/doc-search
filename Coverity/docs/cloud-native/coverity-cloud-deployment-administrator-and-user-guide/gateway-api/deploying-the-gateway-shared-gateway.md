---
title: "Deploying the gateway: shared gateway"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/deploying-the-gateway-shared-gateway.html"
content_id: "HUjiqSZVVEhTFMUzLk0jYA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:30.980864+00:00"
---

# Deploying the gateway: shared gateway

A single Gateway
lives in a central namespace (managed by a platform team or a dedicated Helm
release). Each CNC namespace creates only HTTPRoutes that attach to it. One external
IP serves all namespaces.

The following Helm key values create HTTP
routes:

```
cim:
  gateway:
    create: false             # do NOT create another Gateway    
    enabled: true             # DO create HTTPRoutes
    name: "shared-gateway"    # exact name of the Gateway above
    namespace: "infra"        # namespace where the shared Gateway lives
```

[image: image]

**Which pattern should you use?**

|  | Gateway per Namespace | Shared Gateway |
| --- | --- | --- |
| External IPs | One per namespace | One for all namespaces |
| TLS cert | One per namespace | One shared certificate that must cover all hostnames. |
| Isolation | Full — namespaces are independent | Partial — shared Gateway is a single point of control. |
| `create` / `enabled` | Both `true` | `create: false`, `enabled: true` in app namespaces. |
| `listeners.https.shared` | `false` (default) | `true` (required for cross-namespace routes) |
| Best for | Independent tenants, simple setup | Platform teams managing a central ingress point |
