---
title: "IP allowlisting on GKE Gateway"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/ip-allowlisting-on-gke-gateway.html"
content_id: "Lhalsok2cYJ26~XpatCqiA"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:28.140397+00:00"
---

# IP allowlisting on GKE Gateway

`allowedSourceRanges` and `gatewayAllowedSourceRanges` are
silently skipped on GKE Gateway (SnippetsFilter/SnippetsPolicy are NGF-only). Use
**Google Cloud Armor** instead:

1. Create a Cloud Armor security policy with IP allowlist rules in the GCP Console or
   via `gcloud`
2. Create a `BackendConfig` in the same namespace referencing the
   policy:

   ```
   apiVersion: cloud.google.com/v1
   kind: BackendConfig
   metadata:
     name: coverity-backend-config
   spec:
     securityPolicy:
       name: "coverity-ip-allowlist"   # Cloud Armor policy name
   ```
3. Annotate the CIM Service to reference the BackendConfig:

   ```
   # in your values.yaml
   cim:
     serviceAnnotations:
       beta.cloud.google.com/backend-config: '{"default": "coverity-backend-config"}'
   ```
