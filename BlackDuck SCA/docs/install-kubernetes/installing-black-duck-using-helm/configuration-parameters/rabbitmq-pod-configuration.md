---
title: "RabbitMQ pod configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/rabbitmq-pod-configuration.html"
content_id: "JXI9G7MlUsUWsg6DGPJPWw"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-10-04T23:32:23.070925+00:00"
content_hash: "7d76f1bafd645fb0d52ca333e01aa9dda26aa1360e88c2149f3abe8ec167c1ed"
---

# RabbitMQ pod configuration

| Parameter | Description | Default |
| --- | --- | --- |
| `rabbitmq.registry` | Image repository to be override at container level |  |
| `rabbitmq.imageTag` | Image tag to be override at container level | `1.2.40` |
| `rabbitmq.resources.limits.memory` | RabbitMQ container Memory Limit | `1024Mi` |
| `rabbitmq.resources.requests.memory` | RabbitMQ container Memory request | `1024Mi` |
| `rabbitmq.nodeSelector` | RabbitMQ node labels for pod assignment | `{}` |
| `rabbitmq.tolerations` | RabbitMQ node tolerations for pod assignment | `[]` |
| `rabbitmq.affinity` | RabbitMQ node affinity for pod assignment | `{}` |
| `rabbitmq.podSecurityContext` | RabbitMQ security context at pod level | `{}` |
| `rabbitmq.securityContext` | RabbitMQ security context at container level | `{}` |
