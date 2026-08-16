---
title: "About TLS sidecar"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/about-tls-sidecar.html"
content_id: "88NXbTPIBPHIfgF1Kx8OVg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:34.236595+00:00"
---

# About TLS sidecar

You may see `cim.cimweb.tlsSidecar` in values.yaml. This is **not
related** to the Gateway TLS cert.

| Gateway TLS (`tlsSecretName`) | TLS Sidecar (`tlsSidecar`) | Notes |
| --- | --- | --- |
| What it is | Cert for the Gateway listener | nginx container inside the CIM pod |
| Listens on | Port 443 (external) | Port 8443 (internal) |
| Used for | Client ↔️ Gateway encryption | scan-services ↔️ cimweb pod-to-pod mTLS |
| Who reads it | The Gateway (NGF or GKE LB) | The nginx sidecar inside the pod |
| Needed for Gateway routing | ✅ Yes | ❌ No |
| Involved in client traffic | ✅ Yes | ❌ No — bypasses the Gateway entirely |

Think of it this way: the Gateway cert handles the **front door** (client-facing TLS).
The TLS sidecar handles an **internal back corridor** (scan-services to cimweb). They
are on completely different paths and use completely different certificates.
