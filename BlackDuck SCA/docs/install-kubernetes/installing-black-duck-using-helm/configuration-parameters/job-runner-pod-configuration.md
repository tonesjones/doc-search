---
title: "Job runner pod configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/job-runner-pod-configuration.html"
content_id: "W9M~GNExOsSezg62XdelTg"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:08.806211+00:00"
---

# Job runner pod configuration

| Parameter | Description | Default |
| --- | --- | --- |
| `jobrunner.registry` | Image repository to be override at container level |  |
| `jobrunner.replicas` | Job runner Pod Replica Count | `1` |
| `jobrunner.resources.limits.cpu` | Job runner container CPU Limit | `1000m` |
| `jobrunner.resources.requests.cpu` | Job runner container CPU request | `1000m` |
| `jobrunner.resources.limits.memory` | Job runner container Memory Limit | `4608Mi` |
| `jobrunner.resources.requests.memory` | Job runner container Memory request | `4608Mi` |
| `jobrunner.maxRamPercentage` | Job runner container maximum heap size | `90` |
| `jobrunner.nodeSelector` | Job runner node labels for pod assignment | `{}` |
| `jobrunner.tolerations` | Job runner node tolerations for pod assignment | `[]` |
| `jobrunner.affinity` | Job runner node affinity for pod assignment | `{}` |
| `jobrunner.podSecurityContext` | Job runner security context at pod level | `{}` |
| `jobrunner.securityContext` | Job runner security context at container level | `{}` |
