---
title: "Match engine pod configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/match-engine-pod-configuration.html"
content_id: "qub6sXZ6qqrk2EUcFQvhXg"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-10-04T23:32:22.958739+00:00"
content_hash: "9740b884f132cc77f1aabbea7cd50f0a6cd8e692fe1e4ebcdf615cb1bf441c13"
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
