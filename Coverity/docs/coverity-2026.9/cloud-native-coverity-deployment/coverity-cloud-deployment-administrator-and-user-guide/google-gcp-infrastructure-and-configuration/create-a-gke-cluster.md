---
title: "Create a GKE cluster"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/create-a-gke-cluster.html"
content_id: "9eydxLlBAt9C9kVx8V5wcA"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:23.269813+00:00"
---

# Create a GKE cluster

Create a cluster. Refer to Google documentation, including:

- Create a Kubernetes cluster
- <https://cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview>
- <https://cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters>

The following example uses the `gcloud` command with options you might
use:

```
gcloud container clusters create "${CNC_CLUSTER_NAME}" \
    --project="${CNC_PROJECT_ID}" \
    --zone="${CNC_ZONE}" \
    --cluster-version="${GKE_CLUSTER_VERSION}" \
    --max-nodes="${MAX_NODES}" \
    --min-nodes="${MIN_NODES}" \
    --node-locations="${CNC_ZONE}" \
    --num-nodes="${NUM_NODES}" \
    --enable-autoscaling \
    --machine-type="${CNC_DEFAULT_POOL_NODE_INSTANCE_TYPE}"
```
