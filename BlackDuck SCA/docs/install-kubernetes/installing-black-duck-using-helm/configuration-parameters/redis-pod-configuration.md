---
title: "Redis pod configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/redis-pod-configuration.html"
content_id: "2iQYprsAcI0wu9YB48pgoA"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-10-04T23:32:23.096303+00:00"
content_hash: "d604b5729f0dafd7d2aa95e57ce31c81204ad5f65614d91eca5522a30f3b2f66"
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
