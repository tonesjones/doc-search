---
title: "List and verify ingress"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/list-and-verify-ingress.html"
content_id: "fAVjq0dYhQfWm1ttJE0YHw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:46.081166+00:00"
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
