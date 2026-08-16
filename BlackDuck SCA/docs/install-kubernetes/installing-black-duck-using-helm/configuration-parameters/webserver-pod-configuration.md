---
title: "Webserver pod configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/webserver-pod-configuration.html"
content_id: "CnFMzCRSkMJCk489A7HYWQ"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:15.790693+00:00"
---

# Webserver pod configuration

| Parameter | Description | Default |
| --- | --- | --- |
| `webserver.registry` | Image repository to be override at container level |  |
| `webserver.imageTag` | Image tag to be override at container level | `2024.7.1` |
| `webserver.resources.limits.memory` | Webserver container Memory Limit | `512Mi` |
| `webserver.resources.requests.memory` | Webserver container Memory request | `512Mi` |
| `webserver.nodeSelector` | Webserver node labels for pod assignment | `{}` |
| `webserver.tolerations` | Webserver node tolerations for pod assignment | `[]` |
| `webserver.affinity` | Webserver node affinity for pod assignment | `{}` |
| `webserver.podSecurityContext` | Webserver security context at pod level | `{}` |
| `webserver.securityContext` | Webserver security context at container level | `{}` |
