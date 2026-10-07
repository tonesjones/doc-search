---
title: "IP Allowlisting on GKE Native Gateway"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/ip-allowlisting-on-gke-native-gateway.html"
content_id: "mZ2YpDTkpqXoS2jsx5_hsg"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:28.234807+00:00"
---

# IP Allowlisting on GKE Native Gateway

The NGF-specific resources (`SnippetsFilter`,
`SnippetsPolicy`) are not supported by the GKE native Gateway
controller. Use **Google Cloud Armor** for IP allowlisting:

1. Create a Cloud Armor security policy in the GCP console or via
   `gcloud`:

   ```
   gcloud compute security-policies create coverity-ip-allowlist \
     --description="CNC IP allowlist"

   gcloud compute security-policies rules create 1000 \
     --security-policy coverity-ip-allowlist \
     --src-ip-ranges="10.0.0.0/8,203.0.113.0/24" \
     --action=allow

   gcloud compute security-policies rules create 2147483647 \
     --security-policy coverity-ip-allowlist \
     --src-ip-ranges="*" \
     --action=deny-403
   ```
2. Create a `BackendConfig` in the release namespace:

   ```
   apiVersion: cloud.google.com/v1
   kind: BackendConfig
   metadata:
     name: coverity-backend-config
     namespace: <release-namespace>
   spec:
     securityPolicy:
       name: "coverity-ip-allowlist"
   ```
3. Annotate the CIM service via chart values:

   ```
   cim:
     serviceAnnotations:
       beta.cloud.google.com/backend-config: '{"default": "coverity-backend-config"}'
   ```
