---
title: "GCP: Create scan job node pool(s)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/gcp-create-scan-job-node-pool-s-.html"
content_id: "JC3nLCi7LpZWSzCWtwJURw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:30.486200+00:00"
---

# GCP: Create scan job node pool(s)

Create one or more node pools to run scan jobs. Refer to:

. Refer to:

- To create a node pool in GCP: <https://cloud.google.com/kubernetes-engine/docs/how-to/node-pools>
- For Coverity cloud scan job node pool information: Scan Service and Storage Service requirements
- For scan jobs node pool sizing: Scan job node pool sizing

For example, using the `gcloud` command:

```
gcloud container node-pools create ${CNC_NODEPOOL_NAME} \
    --cluster="${CNC_CLUSTER_NAME}" \
    --project="${CNC_PROJECT_ID}" \
    --zone="${CNC_ZONE}" \
    --node-taints=NodeType=ScannerNode:NoSchedule \
    --node-labels=pool-type="${CNC_ANALYSIS_POOL_LABEL}" \
    --node-version="${GKE_CLUSTER_VERSION}" \
    --image-type=COS_CONTAINERD \
    --machine-type="${CNC_ANALYSIS_POOL_NODE_INSTANCE_TYPE}" \
    --min-nodes="${MIN_SJ_NODES}" \
    --max-nodes="${MAX_SJ_NODES}" \
    --num-nodes="${NUM_SJ_NODES}" \
    --enable-autoscaling \
    --enable-private-nodes
```
