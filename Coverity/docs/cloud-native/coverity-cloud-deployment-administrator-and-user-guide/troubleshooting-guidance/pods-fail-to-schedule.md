---
title: "Pods fail to schedule"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/pods-fail-to-schedule.html"
content_id: "lCV4KmL1yfTBPO2GYO9RHw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:53.549664+00:00"
---

# Pods fail to schedule

Verify the following:

- Make sure that the cluster has sufficient CPU and memory for your pods.
- Make sure that one or more nodes has sufficient available memory and CPU for your
  largest pods.

If Kubernetes is unable to find a node with sufficient CPU or memory for a given pod, the
pod will fail to schedule and will be stuck in a `Pending` state. This
can be diagnosed using the following command.

```
kubectl describe -n $NS $POD
```
