---
title: "Liveness probe keys"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/liveness-probe-keys.html"
content_id: "3J5n_MAZiQIJf1SDWeE81g"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:32.989238+00:00"
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
