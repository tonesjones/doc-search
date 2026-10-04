---
title: "Pods - list all pods"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/pods-list-all-pods.html"
content_id: "4E3mVLs8AsDqllW_1CS7rA"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:38.605505+00:00"
---

# Pods - list all pods

Look for pods that are not running – `CrashLoopBackoff`,
`ImagePullBackOff`, `Error`, etc. Also, look for pods
that have restarted.

```
kubectl get pods -A
```
