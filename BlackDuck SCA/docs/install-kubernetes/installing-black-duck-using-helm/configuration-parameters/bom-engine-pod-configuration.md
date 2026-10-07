---
title: "BOM engine pod configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/bom-engine-pod-configuration.html"
content_id: "arcXtewFjEpAgn7vtGmnTg"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-10-04T23:32:22.775218+00:00"
content_hash: "ad0854362e11717608efcfcbfe32e5ba1550cbd1e0fa8b4c07154a49a3ecf7a8"
---

# BOM engine pod configuration

| Parameter | Description | Default |
| --- | --- | --- |
| `bomengine.registry` | Image repository to be override at container level |  |
| `bomengine.resources.limits.memory` | BOM Engine container Memory Limit | `1024Mi` |
| `bomengine.resources.requests.memory` | BOM Engine container Memory request | `1024Mi` |
| `bomengine.maxRamPercentage` | BOM Engine container maximum heap size | `90` |
| `bomengine.nodeSelector` | BOM Engine node labels for pod assignment | `{}` |
| `bomengine.tolerations` | BOM Engine node tolerations for pod assignment | `[]` |
| `bomengine.affinity` | BOM Engine node affinity for pod assignment | `{}` |
| `bomengine.podSecurityContext` | BOM Engine security context at pod level | `{}` |
| `bomengine.securityContext` | BOM Engine security context at container level | `{}` |
