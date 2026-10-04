---
title: "Google Kubernetes Engine (GKE)"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/google-kubernetes-engine-gke-.html"
content_id: "a5mqP01n96jHFAFM94OiVw"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:28.048948+00:00"
---

# Google Kubernetes Engine (GKE)

Two options are available on GKE: NGINX Gateway Fabric (NGF) and the GKE-native Gateway
controller. Both implement the standard Kubernetes Gateway API and are compatible with
the CNC chart. Choose based on your operational requirements.

| Dimension | Option A: NGINX Gateway Fabric | Option B: GKE Native Controller |
| --- | --- | --- |
| Gateway implementation | NGF controller pod in cluster | Fully managed by Google |
| Load balancer type | GCP TCP/UDP Network Load Balancer | Google Cloud Application Load Balancer |
| L7 features | NGF-native (SnippetsFilter, ClientSettingsPolicy) | GKE-native (Cloud Armor, HealthCheckPolicy) |
| IP allowlisting | `SnippetsPolicy` / `SnippetsFilter` | Google Cloud Armor |
| External IP location | `kubectl get svc` (NGF proxy Service) | `kubectl get gateway` (directly on Gateway) |
| GatewayClass | `nginx` | `gke-l7-global-external-managed` (and others) |

## GKE Gateway API NEG provisioning

GKE Gateway API automatically provisions Network Endpoint Groups (NEGs) for any
Service referenced as a `backendRef` in an HTTPRoute. No
`cloud.google.com/neg` annotation is required on the Service. The
annotation is needed for only the legacy Ingress path or when you also expose the
Service via a standalone NEG outside the Gateway controller.
