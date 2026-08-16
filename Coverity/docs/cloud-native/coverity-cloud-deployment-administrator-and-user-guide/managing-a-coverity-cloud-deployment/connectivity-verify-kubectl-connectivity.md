---
title: "Connectivity - verify kubectl connectivity"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/connectivity-verify-kubectl-connectivity.html"
content_id: "RxHkQsPJfGYjg5fAKKPSZQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:18.699302+00:00"
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
