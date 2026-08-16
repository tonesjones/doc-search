---
title: "Pods - describe pod"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/pods-describe-pod.html"
content_id: "~M2XOgoX43jCZvwznpJwYA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:22.694372+00:00"
---

# Pods - describe pod

Look at the very bottom for pod status. This is where errors are listed.

```
kubectl describe pod -n "$NS" "${POD}"
```

"$NS" is the namespace name and "${POD}" is the pod name.
