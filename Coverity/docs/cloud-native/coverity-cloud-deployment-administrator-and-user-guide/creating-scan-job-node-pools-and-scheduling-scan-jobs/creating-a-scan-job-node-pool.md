---
title: "Creating a scan job node pool"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/creating-a-scan-job-node-pool.html"
content_id: "pMZ3JJYFxUFjbHslTd_0_A"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:09.614352+00:00"
---

# Creating a scan job node pool

Coverity scanning is a time-consuming and resource-intensive process, therefore
performing scan jobs in a node pool created only for scan jobs is faster and more
reliable.

Important: For node pool sizing, see the section, Scan job node pool sizing.

Before you deploy Scan Service, do the following:

- Create a node pool for scan jobs. In a cloud environment with access to resources,
  you can create as many as five scan job node pools; one for each node pool type:
  small, medium, large, extra large, and custom.
- If you are deploying on-prem and have limited resources, you might build a single
  node pool and schedule all scan jobs to that node pool. For example, you can deploy
  an extra large node pool.
- Define how to [steer pods to specific nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/):
  - You can constrain job pods to run on specific nodes that provide resource
    characteristics for the job. For example, small job to small node, large job
    to large node, etc. Scan Service uses the NodeSelector field in the pod
    specification to steer pods to a dedicated node pool, for example, to run
    scan jobs on nodes dedicated for scan jobs. This method is good in cloud
    environments where nodes can easily be spun up to meet demand. For
    additional information, refer to <https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#step-one-attach-label-to-the-node>.
  - Alternatively, you can schedule all scan jobs to run on a single node that
    is labeled and dedicated for scan jobs. You might use this method in an
    environment with limited and fixed resources

To create scan job node pools in AWS, GCP, or Azure cloud environments, see:

- To create a scan job node pool on Amazon AWS: AWS: Create scan job node pool(s)
- To create a scan job node pool on Google GCP: GCP: Create scan job node pool(s)
- To create a scan job node pool on Microsoft AKS: Azure AKS: Create scan job node pool(s)

To deploy scan jobs on a scan job node pool, define Helm keys as described in:

- Configuring one scan job per node, multiple node pools
- `scan-service.environment` Helm keys in scan-service.environment Helm keys.
- Scheduling with taints and tolerations: Taints and tolerations
- Enabling single-node scan jobs: Enabling single vs multiple scan jobs per node
- Scheduling single-node scan jobs: Configuring multiple scan jobs per node, single node pool
