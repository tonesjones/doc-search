---
title: "Grant cluster-admin permissions to user"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/grant-cluster-admin-permissions-to-user.html"
content_id: "tt3LGHritznyd3zIuXa_tw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:25.889737+00:00"
---

# Grant cluster-admin permissions to user

Grant cluster-admin permissions to user:

```
kubectl create clusterrolebinding cluster-admin-binding \
    --clusterrole=cluster-admin \
    --user=$GCP_USER
```
