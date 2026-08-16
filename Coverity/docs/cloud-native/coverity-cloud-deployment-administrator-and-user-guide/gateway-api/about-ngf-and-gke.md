---
title: "About NGF and GKE"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/about-ngf-and-gke.html"
content_id: "4eQRdAWHpYGBuiu8h7hinA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:35.534659+00:00"
---

# About NGF and GKE

The `tlsSecretName` value and the Secret itself work identically on both.
The only difference is **which component reads the Secret**:

| NGF | GKE | Notes |
| --- | --- | --- |
| Who reads the Secret | NGF controller (in `nginx-gateway` namespace) | GKE Load Balancer controller |
| How you find the Gateway IP | `kubectl get svc` (NGF proxy Service) | `kubectl get gateway` (directly on Gateway) |
| Secret namespace requirement | Same namespace as Gateway | Same namespace as Gateway |

Everything else — creating the Secret, setting `tlsSecretName`, the
cert/key format — is the same.
