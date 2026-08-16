---
title: "Binary scanner pod configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/binary-scanner-pod-configuration.html"
content_id: "RXEBewE7OBSnI~pTucYvXw"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:05.392461+00:00"
---

# Binary scanner pod configuration

| Parameter | Description | Default |
| --- | --- | --- |
| `binaryscanner.registry` | Image repository to be override at container level | `docker.io/sigblackduck` |
| `binaryscanner.imageTag` | Image tag to be override at container level | `2024.6.3` |
| `binaryscanner.resources.limits.Cpu` | Binary Scanner container CPU Limit | `1000m` |
| `binaryscanner.resources.requests.Cpu` | Binary Scanner container CPU request | `1000m` |
| `binaryscanner.resources.limits.memory` | Binary Scanner container Memory Limit | `2048Mi` |
| `binaryscanner.resources.requests.memory` | Binary Scanner container Memory request | `2048Mi` |
| `binaryscanner.nodeSelector` | Binary Scanner node labels for pod assignment | `{}` |
| `binaryscanner.tolerations` | Binary Scanner node tolerations for pod assignment | `[]` |
| `binaryscanner.affinity` | Binary Scanner node affinity for pod assignment | `{}` |
| `binaryscanner.podSecurityContext` | Binary Scanner security context at pod level | `{}` |
| `binaryscanner.securityContext` | Binary Scanner security context at container level | `{}` |
