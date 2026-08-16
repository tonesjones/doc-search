---
title: "Scan pod configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/scan-pod-configuration.html"
content_id: "9o3wRamdE8WxAFPw_p9uAA"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:14.034894+00:00"
---

# Scan pod configuration

| Parameter | Description | Default |
| --- | --- | --- |
| `scan.registry` | Image repository to be override at container level |  |
| `scan.replicas` | Scan Pod Replica Count | `1` |
| `scan.resources.limits.memory` | Scan container Memory Limit | `2560Mi` |
| `scan.resources.requests.memory` | Scan container Memory request | `2560Mi` |
| `scan.maxRamPercentage` | Scan container maximum heap size | `90` |
| `scan.nodeSelector` | Scan node labels for pod assignment | `{}` |
| `scan.tolerations` | Scan node tolerations for pod assignment | `[]` |
| `scan.affinity` | Scan node affinity for pod assignment | `{}` |
| `scan.podSecurityContext` | Scan security context at pod level | `{}` |
| `scan.securityContext` | Scan security context at container level | `{}` |
