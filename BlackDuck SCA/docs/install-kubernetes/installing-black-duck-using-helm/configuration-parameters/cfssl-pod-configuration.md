---
title: "CFSSL pod configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/cfssl-pod-configuration.html"
content_id: "yHGUmurDcckPYNrksxxp0Q"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:06.525292+00:00"
---

# CFSSL pod configuration

| Parameter | Description | Default |
| --- | --- | --- |
| `cfssl.registry` | Image repository to be override at container level |  |
| `cfssl.imageTag` | Image tag to be override at container level | `1.0.28` |
| `cfssl.resources.limits.memory` | Cfssl container Memory Limit | `640Mi` |
| `cfssl.resources.requests.memory` | Cfssl container Memory request | `640Mi` |
| `cfssl.persistentVolumeClaimName` | Point to an existing Cfssl Persistent Volume Claim (PVC) |  |
| `cfssl.claimSize` | Cfssl Persistent Volume Claim (PVC) claim size | `2Gi` |
| `cfssl.storageClass` | Cfssl Persistent Volume Claim (PVC) storage class |  |
| `cfssl.volumeName` | Point to an existing Cfssl Persistent Volume (PV) |  |
| `cfssl.nodeSelector` | Cfssl node labels for pod assignment | `{}` |
| `cfssl.tolerations` | Cfssl node tolerations for pod assignment | `[]` |
| `cfssl.affinity` | Cfssl node affinity for pod assignment | `{}` |
| `cfssl.podSecurityContext` | Cfssl security context at pod level | `{}` |
| `cfssl.securityContext` | Cfssl security context at container level | `{}` |
