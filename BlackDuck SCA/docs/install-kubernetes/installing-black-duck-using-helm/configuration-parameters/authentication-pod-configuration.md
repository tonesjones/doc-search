---
title: "Authentication pod configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/authentication-pod-configuration.html"
content_id: "wEvQBSdV47Xxs37OTbHx9Q"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-10-04T23:32:22.721441+00:00"
content_hash: "2624b809397df37cc8b1208fa0866ac7f7d8edadf67b27a7fbb342f216b28904"
---

# Authentication pod configuration

| Parameter | Description | Default |
| --- | --- | --- |
| `authentication.registry` | Image repository to be override at container level |  |
| `authentication.resources.limits.memory` | Authentication container Memory Limit | `1024Mi` |
| `authentication.resources.requests.memory` | Authentication container Memory request | `1024Mi` |
| `authentication.maxRamPercentage` | Authentication container maximum heap size | `90` |
| `authentication.persistentVolumeClaimName` | Point to an existing Authentication Persistent Volume Claim (PVC) |  |
| `authentication.claimSize` | Authentication Persistent Volume Claim (PVC) claim size | `2Gi` |
| `authentication.storageClass` | Authentication Persistent Volume Claim (PVC) storage class |  |
| `authentication.volumeName` | Point to an existing Authentication Persistent Volume (PV) |  |
| `authentication.nodeSelector` | Authentication node labels for pod assignment | `{}` |
| `authentication.tolerations` | Authentication node tolerations for pod assignment | `[]` |
| `authentication.affinity` | Authentication node affinity for pod assignment | `{}` |
| `authentication.podSecurityContext` | Authentication security context at pod level | `{}` |
| `authentication.securityContext` | Authentication security context at container level | `{}` |
