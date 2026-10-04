---
title: "GCP ingress controller taints and tolerations"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/gcp-ingress-controller-taints-and-tolerations.html"
content_id: "V8x08wS~Zu8kTh~G2yZH1A"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:21.819242+00:00"
---

# GCP ingress controller taints and tolerations

GCP adds Kubernetes-managed taints for ARM64 nodes, therefore you must add the following
toleration in the ingress controller deployment.

```
- key: "kubernetes.io/arch"
  operator: "Equal"
  value: "arm64"
  effect: "NoSchedule"
```

Note: Refer to <https://cloud.google.com/kubernetes-engine/docs/how-to/prepare-arm-workloads-for-deployment>.

Note: The pod cannot schedule on a GCP ARM64 node pool if it does not
have a respective toleration.
