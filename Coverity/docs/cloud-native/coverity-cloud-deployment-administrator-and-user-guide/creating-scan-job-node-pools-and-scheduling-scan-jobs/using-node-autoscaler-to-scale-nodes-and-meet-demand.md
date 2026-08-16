---
title: "Using node autoscaler to scale nodes and meet demand"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-node-autoscaler-to-scale-nodes-and-meet-demand.html"
content_id: "d~GZxkHCVyyTMHQk~QoDBw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:10.283853+00:00"
---

# Using node autoscaler to scale nodes and meet demand

You can optionally enable and configure node autoscaler to scale nodes up or down to meet
demand. With this feature enabled, if a node is unavailable to run a scheduled scan job,
Kubernetes creates an additional node which can run additional scan jobs as resources
permit. Refer to your cloud provider for information on enabling and configuring node
autoscaler.

For information on using and configuring autoscaler in your cloud environment, refer to
the appropriate documentation:

- Amazon AWS:
  - About: [Scale cluster compute with Karpenter and
    Cluster Autoscaler](https://docs.aws.amazon.com/eks/latest/userguide/autoscaling.html)
  - Configuring: [Cluster Autoscaler on AWS](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/cloudprovider/aws/README.md)
- Google GKE:
  - About: [About GKE cluster autoscaling](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler)
  - Configuring: [Autoscaling a cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler)
- Microsoft Azure:
  - About: [Cluster autoscaling in Azure Kubernetes
    Service (AKS) overview](https://learn.microsoft.com/en-us/azure/aks/cluster-autoscaler-overview)
  - Configure: [Use the cluster autoscaler in Azure
    Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/cluster-autoscaler?tabs=azure-cli)
