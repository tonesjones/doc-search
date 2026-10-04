---
title: "Binary scanner pod configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/binary-scanner-pod-configuration.html"
content_id: "vxwXEPtccjYpZTYPP7A_hw"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-10-04T23:32:22.748142+00:00"
content_hash: "2b27021659947fab95f2f1bbbaed8f1a55b3c7bec43f3ce8783de2e093184677"
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
