---
title: "Limitations of NGINX gateway fabric vs GKE gateway"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/limitations-of-nginx-gateway-fabric-vs-gke-gateway.html"
content_id: "b~fnc82xyzfOsuyRdqna~g"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:28.328932+00:00"
---

# Limitations of NGINX gateway fabric vs GKE gateway

| Feature | NGF | GKE Gateway |
| --- | --- | --- |
| IP allowlisting | `allowedSourceRanges` / `gatewayAllowedSourceRanges` | Google Cloud Armor (external) |
| Max body size | `clientSettings.body.maxSize` | BackendConfig / LB settings |
| Raw nginx directives | `filters[]` with SnippetsFilter | Not supported |
| Health check | Auto-configured via `HealthCheckPolicy` (chart-managed) | Auto-configured via `HealthCheckPolicy` (chart-managed) |
| Gateway IP location | ``` kubectl get               svc <release>-gateway-nginx ``` | ``` kubectl get               gateway <release>-gateway ``` |
| Proxy pod in namespace | Yes (NGF creates `<release>-gateway-nginx` pod) | No (GKE LB is fully managed) |
