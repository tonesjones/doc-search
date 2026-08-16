---
title: "Gateway API"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/gateway-api.html"
content_id: "nphRB8Tvrndy1fl_1fvXKw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:27.771805+00:00"
---

# Gateway API

The `cnc` chart now supports [Kubernetes Gateway API](https://gateway-api.sigs.k8s.io/) as an alternative to
the existing NGINX Ingress Controller integration. Both continue to be supported;
enabling one does not require disabling the other, but in practice you will run only
one.

For further information on the gateway API, see:

- For an introduction, see the Kubernetes article: <https://gateway-api.sigs.k8s.io/docs/introduction/>
- For gateway Helm keys, see: cim.gateway Helm keys
- For ingress Helm keys, see:cim.ingress Helm keys
