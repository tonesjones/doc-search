---
title: "GCP taints and tolerations for ARM64"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/gcp-taints-and-tolerations-for-arm64.html"
content_id: "cvXTQLya3molczsZNV5CRA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:04.746390+00:00"
---

# GCP taints and tolerations for ARM64

By default, GCP adds the Kubernetes taint
(`kubernetes.io/arch=arm64:NoSchedule`) to prevent scheduling to
ARM64 node pools. To allow pods to schedule on ARM64 node pools, you need to add
tolerations that allow services to be scheduled on ARM64 nodes. This section describes
these tolerations for Coverity cloud.

Note: See also:

- <https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/>
- <https://cloud.google.com/kubernetes-engine/docs/how-to/prepare-arm-workloads-for-deployment>

Note: To successfully deploy a Coverity cloud chart in a GCP ARM64
cluster, you must add tolerations to all CNC pods in the cluster. Otherwise, pods will
remain in a pending state.

You can set tolerations in the Helm chart either per-service or globally (preferred
method) as follows:

- You can pass tolerations as a global override in the Helm chart, setting tolerations
  for all services at once by configuring `global.tolerations: []`. As
  tolerations must be set for all Coverity Cloud services for GCP ARM64 node pools, it is
  better to create a global Helm override. For
  example:

  ```
  global:
    tolerations:
      - key: "kubernetes.io/arch"
        operator: "Equal"
        value: "arm64"
        effect: "NoSchedule"
  ```
- You can pass tolerations as Helm overrides for specific services. For example, pass
  `tolerations: []` under specific services in
  `values.yaml`.

  If you set tolerations on a service-by-service basis, in
  the Helm chart, you need to set the following tolerations to cover all
  services:

  ```
  cim:
    tolerations:
      - key: "kubernetes.io/arch"
        operator: "Equal"
        value: "arm64"
        effect: "NoSchedule"

  scan-services:
    cache-service:
      tolerations:
        - key: "kubernetes.io/arch"
          operator: "Equal"
          value: "arm64"
          effect: "NoSchedule"

  scan-services:
    common-infra:
      tolerations:
        - key: "kubernetes.io/arch"
          operator: "Equal"
          value: "arm64"
          effect: "NoSchedule"

  scan-services:
    scan-service:
      tolerations:
        - key: "kubernetes.io/arch"
          operator: "Equal"
          value: "arm64"
          effect: "NoSchedule"

  scan-services:
    storage-service:
      tolerations:
        - key: "kubernetes.io/arch"
          operator: "Equal"
          value: "arm64"
          effect: "NoSchedule"
  ```
