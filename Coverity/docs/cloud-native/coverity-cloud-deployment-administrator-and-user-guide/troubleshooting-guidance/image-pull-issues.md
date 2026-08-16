---
title: "Image pull issues"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/image-pull-issues.html"
content_id: "JjDuxnkTd0PnHHxu74AYkA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:52.915068+00:00"
---

# Image pull issues

If you are seeing `ImagePullBackoff` or `ImagePullError` in
your cluster, for each pod that is experiencing image pull errors, check the pod yaml
file:

```
kubectl get pod -n "$NS" "$POD" -o yaml
```

Verify that the `imagePullSecret` Helm key contains the name of the secret
that contains the Docker registry credentials, and that the secret exists in the
Coverity Connect cloud namespace (for example `cnc`).
