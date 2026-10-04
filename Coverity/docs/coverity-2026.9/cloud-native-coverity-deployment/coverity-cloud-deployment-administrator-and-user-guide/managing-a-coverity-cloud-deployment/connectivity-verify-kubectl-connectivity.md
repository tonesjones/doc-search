---
title: "Connectivity - verify kubectl connectivity"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/connectivity-verify-kubectl-connectivity.html"
content_id: "RxHkQsPJfGYjg5fAKKPSZQ"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:38.327185+00:00"
---

# Connectivity - verify kubectl connectivity

Using the following commands, verify that `kubectl` is configured to talk
to your cluster, and that the Kubernetes version installed on both the client and server
is supported. For supported versions of Kubernetes, see Third-party software and platform support matrix.

```
kubectl config get-contexts
kubectl config current-context
kubectl version
```
