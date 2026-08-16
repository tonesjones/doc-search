---
title: "Taints and tolerations"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/taints-and-tolerations.html"
content_id: "JSMANNIqcw5loHcKbNz4TQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:12.937294+00:00"
---

# Taints and tolerations

Coverity scans are resource intensive and running applications pods on scan job nodes
might cause the system to become unstable as application pods can be evicted. We
recommend using taints and tolerations to prevent application pods from being scheduled
on the scan job nodes. Taints and tolerations work together to ensure that pods are not
scheduled onto inappropriate nodes.

For additional information, refer to [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/_print/#pg-ede4960b56a3529ee0bfe7c8fe2d09a5).

See also [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)
