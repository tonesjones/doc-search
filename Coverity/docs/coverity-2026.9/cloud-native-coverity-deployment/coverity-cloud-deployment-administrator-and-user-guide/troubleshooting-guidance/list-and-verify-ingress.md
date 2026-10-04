---
title: "List and verify ingress"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/list-and-verify-ingress.html"
content_id: "fAVjq0dYhQfWm1ttJE0YHw"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:40.243866+00:00"
---

# List and verify ingress

Use the following command to list ingresses:

```
kubectl get ingress -n $NS -o yaml
```

Verify that all of the following are correct:

- host
- tls/hosts
- tls/secretName
