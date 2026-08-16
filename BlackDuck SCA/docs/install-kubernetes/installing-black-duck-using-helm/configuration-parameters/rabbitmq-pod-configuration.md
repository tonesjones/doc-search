---
title: "RabbitMQ pod configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/rabbitmq-pod-configuration.html"
content_id: "9088IP4O1Odl36Ku~zZDgg"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:12.342979+00:00"
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
