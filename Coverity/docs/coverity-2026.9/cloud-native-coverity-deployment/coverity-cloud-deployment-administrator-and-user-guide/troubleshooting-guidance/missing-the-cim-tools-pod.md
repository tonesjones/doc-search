---
title: "Missing the cim-tools pod"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/missing-the-cim-tools-pod.html"
content_id: "cj8tY0XH0wYeUJgJGpb9jg"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:40.737109+00:00"
---

# Missing the cim-tools pod

The `cim-tools` pod is scaled down to 0 by default. You can scale up the
pod when you need to run it. Use the following commands to scale the pod up or down.

To scale up the cim-tools pod:

```
kubectl scale statefulsets ${RELEASE}-cim-tools -n $NS --replicas=1
```

To scale down the cim-tools pod:

```
kubectl scale statefulsets ${RELEASE}-cim-tools -n $NS --replicas=0
```
