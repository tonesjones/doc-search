---
title: "Match engine pod configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/match-engine-pod-configuration.html"
content_id: "WjoFvWWt30O7wivMXrpgBA"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:09.952541+00:00"
---

# Match engine pod configuration

| Parameter | Description | Default |
| --- | --- | --- |
| `matchengine.registry` | Image repository to be override at container level |  |
| `matchengine.resources.limits.memory` | MATCH Engine container Memory Limit | `4608Mi` |
| `matchengine.resources.requests.memory` | MATCH Engine container Memory request | `4608Mi` |
| `matchengine.maxRamPercentage` | MATCH Engine maximum heap size | `90` |
| `matchengine.nodeSelector` | MATCH Engine node labels for pod assignment | `{}` |
| `matchengine.tolerations` | MATCH Engine node tolerations for pod assignment | `[]` |
| `matchengine.affinity` | MATCH Engine node affinity for pod assignment | `{}` |
| `matchengine.podSecurityContext` | MATCH Engine security context at pod level | `{}` |
| `matchengine.securityContext` | MATCH Engine security context at container level | `{}` |
