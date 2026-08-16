---
title: "Integration pod configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/integration-pod-configuration.html"
content_id: "WAuhWu0oEu3y~v4Jj_aV6g"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:07.682618+00:00"
---

# Integration pod configuration

| Parameter | Description | Default |
| --- | --- | --- |
| `integration.registry` | Image repository to be override at container level |  |
| `integration.replicas` | Integration Pod Replica Count | `1` |
| `integration.resources.limits.cpu` | Integration container CPU Limit | `1000m` |
| `integration.resources.requests.cpu` | Integration container CPU request | `500m` |
| `integration.resources.limits.memory` | Integration container Memory Limit | `5120Mi` |
| `integration.resources.requests.memory` | Integration container Memory request | `5120Mi` |
| `integration.maxRamPercentage` | Integration container maximum heap size | `90` |
| `integration.nodeSelector` | Integration node labels for pod assignment | `{}` |
| `integration.tolerations` | Integration node tolerations for pod assignment | `[]` |
| `integration.affinity` | Integration node affinity for pod assignment | `{}` |
| `integration.podSecurityContext` | Integration security context at pod level | `{}` |
| `integration.securityContext` | Integration security context at container level | `{}` |
