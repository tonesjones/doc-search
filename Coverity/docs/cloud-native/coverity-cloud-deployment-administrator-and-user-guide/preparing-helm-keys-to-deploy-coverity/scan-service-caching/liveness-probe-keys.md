---
title: "Liveness probe keys"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/liveness-probe-keys.html"
content_id: "3J5n_MAZiQIJf1SDWeE81g"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:52.959823+00:00"
---

# Liveness probe keys

Liveness Probe, used with Kubernetes, indicates whether or not a container is running.
The following Helm keys define liveness probe variables for Cache Service. Accept the
default values. For information on the keys, refer to the section, scan-services Helm subchart: Helm keys.

```
cache-service:
  livenessProbe:
    initialDelaySeconds: 30
    periodSeconds: 180
    timeoutSeconds: 60
    failureThreshold: 3
```
