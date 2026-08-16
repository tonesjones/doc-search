---
title: "Pods - Pull logs from pods"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/pods-pull-logs-from-pods.html"
content_id: "26rw6d2Yt~V3pj7nhR3f7Q"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:23.977521+00:00"
---

# Pods - Pull logs from pods

```
kubectl logs -f -n "$NS" "${POD}" "$CONTAINER"
```

"$NS" is the namespace name, "${POD}" is the pod name, and "$CONTAINER" is the Coverity
Connect Kubernetes container name.
