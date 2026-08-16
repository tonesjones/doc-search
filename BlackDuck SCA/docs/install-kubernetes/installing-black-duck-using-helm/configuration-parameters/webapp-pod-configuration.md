---
title: "Webapp pod configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/webapp-pod-configuration.html"
content_id: "CeYeiFDJgOkllAJBr8hasg"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:15.240772+00:00"
---

# Webapp pod configuration

| Parameter | Description | Default |
| --- | --- | --- |
| `webapp.registry` | Image repository to be override at container level |  |
| `webapp.resources.requests.cpu` | Webapp container CPU request | `1000m` |
| `webapp.resources.limits.memory` | Webapp container Memory Limit | `2560Mi` |
| `webapp.resources.requests.memory` | Webapp container Memory request | `2560Mi` |
| `webapp.maxRamPercentage` | Webapp container maximum heap size | `90` |
| `webapp.persistentVolumeClaimName` | Point to an existing Webapp Persistent Volume Claim (PVC) |  |
| `webapp.claimSize` | Webapp Persistent Volume Claim (PVC) claim size | `2Gi` |
| `webapp.storageClass` | Webapp Persistent Volume Claim (PVC) storage class |  |
| `webapp.volumeName` | Point to an existing Webapp Persistent Volume (PV) |  |
| `webapp.nodeSelector` | Webapp node labels for pod assignment | `{}` |
| `webapp.tolerations` | Webapp node tolerations for pod assignment | `[]` |
| `webapp.affinity` | Webapp node affinity for pod assignment | `{}` |
| `webapp.podSecurityContext` | Webapp and Logstash security context at pod level | `{}` |
| `webapp.securityContext` | Webapp security context at container level | `{}` |
