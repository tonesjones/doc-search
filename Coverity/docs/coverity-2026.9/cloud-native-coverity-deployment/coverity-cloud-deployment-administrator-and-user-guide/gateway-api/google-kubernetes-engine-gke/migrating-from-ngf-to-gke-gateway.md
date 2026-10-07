---
title: "Migrating from NGF to GKE Gateway"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/migrating-from-ngf-to-gke-gateway.html"
content_id: "6RFxjf3A8wFGcG_INKIgOQ"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:28.280361+00:00"
---

# Migrating from NGF to GKE Gateway

## Prerequisites for GKE Gateway

GKE Gateway is built into GKE — no separate NGF installation needed. Ensure that:

- GKE version ≥ 1.24 with Gateway API enabled on the cluster:

  ```
  # Enable during cluster creation
  gcloud container clusters create ... --gateway-api=standard

  # Or enable on an existing cluster
  gcloud container clusters update CLUSTER --gateway-api=standard --region=REGION
  ```
- Verify that the GatewayClasses are available:

  ```
  kubectl get gatewayclass
  # Should show gke-l7-global-external-managed, gke-l7-rilb, etc.
  ```

## Migrating

If you previously used NGINX Gateway Fabric (`gatewayClassName:
nginx`), NGF creates a dedicated nginx proxy pod and LoadBalancer Service
**inside your namespace** (e.g. `<release>-gateway-nginx`
pod + Service). When you switch GatewayClass to `gke-*`, NGF stops
managing the Gateway but does **not** clean up the proxy pod/Service it
created.

After switching, delete the orphaned NGF resources manually:

```
# Find them
kubectl get pods,svc -n <namespace> | grep "gateway-nginx"

# Delete
kubectl delete pod <release>-gateway-nginx-<hash> -n <namespace>
kubectl delete svc <release>-gateway-nginx -n <namespace>
```

Important: Update DNS to point to the new GKE Gateway
IP, not the old NGF LoadBalancer IP. Run `kubectl get gateway
<release>-gateway -n <namespace>` to get the new IP.
