---
title: "Redis pod configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/redis-pod-configuration.html"
content_id: "s~iNaYzetYY1DITKuF870w"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:12.896800+00:00"
---

# Redis pod configuration

| Parameter | Description | Default |
| --- | --- | --- |
| `redis.registry` | Image repository to be override at container level |  |
| `redis.resources.limits.memory` | Redis container Memory Limit | `1024Mi` |
| `redis.resources.requests.memory` | Redis container Memory request | `1024Mi` |
| `redis.tlsEnalbed` | Enable TLS connections between client and Redis | `false` |
| `redis.maxTotal` | Maximum number of concurrent client connections that can be connected to Redis | `128` |
| `redis.maxIdle` | Maximum number of concurrent client connections that can remain idle in the pool, without extra ones being released | `128` |
| `redis.nodeSelector` | Redis node labels for pod assignment | `{}` |
| `redis.tolerations` | Redis node tolerations for pod assignment | `[]` |
| `redis.affinity` | Redis node affinity for pod assignment | `{}` |
| `redis.podSecurityContext` | Redis security context at pod level | `{}` |
| `redis.securityContext` | Redis security context at container level | `{}` |
