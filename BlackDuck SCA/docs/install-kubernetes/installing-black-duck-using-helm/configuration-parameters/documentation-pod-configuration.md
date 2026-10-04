---
title: "Documentation pod configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/documentation-pod-configuration.html"
content_id: "FaJcGQxVKXezuGgZPbLDRA"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-10-04T23:32:22.827123+00:00"
content_hash: "09562543d26ed107f9492cd938dd765fd63f7413d3564857eecbda928601a9bf"
---

# Documentation pod configuration

| Parameter | Description | Default |
| --- | --- | --- |
| `documentation.registry` | Image repository to be override at container level |  |
| `documentation.resources.limits.memory` | Documentation container Memory Limit | `512Mi` |
| `documentation.resources.requests.memory` | Documentation container Memory request | `512Mi` |
| `documentation.maxRamPercentage` | Documentation container Memory request | `90` |
| `documentation.nodeSelector` | Documentation node labels for pod assignment | `{}` |
| `documentation.tolerations` | Documentation node tolerations for pod assignment | `[]` |
| `documentation.affinity` | Documentation node affinity for pod assignment | `{}` |
| `documentation.podSecurityContext` | Documentation security context at pod level | `{}` |
| `documentation.securityContext` | Documentation security context at container level | `{}` |
