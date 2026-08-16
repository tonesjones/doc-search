---
title: "Readiness probe keys"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/readiness-probe-keys.html"
content_id: "t~O2TYdUsnkQCrJ24ycGLQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:50.688215+00:00"
---

# Readiness probe keys

Readiness Probe, used with Kubernetes, indicates whether or not a container is ready to
accept traffic. The following Helm keys define readiness probe variables for Cache
Service. Accept the default values. For information on the keys, refer to the section,
scan-services Helm subchart: Helm keys.

```
cache-service:
  readinessProbe:
    initialDelaySeconds: 30
    periodSeconds: 180
    timeoutSeconds: 60
    failureThreshold: 3
```
