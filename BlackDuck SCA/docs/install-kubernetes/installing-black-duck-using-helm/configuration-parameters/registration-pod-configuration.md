---
title: "Registration pod configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/registration-pod-configuration.html"
content_id: "PALIVlGunHwmuzPymY22uw"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-10-04T23:32:23.121729+00:00"
content_hash: "b28238cc9b91ba3e061bb51077885e51a44a30200915f8fb1cac095003dece8d"
---

# Registration pod configuration

| Parameter | Description | Default |
| --- | --- | --- |
| `registration.registry` | Image repository to be override at container level |  |
| `registration.requestCpu` | Registration container CPU request | `1000m` |
| `registration.resources.limits.memory` | Registration container Memory Limit | `1024Mi` |
| `registration.resources.requests.memory` | Registration container Memory request | `1024Mi` |
| `registration.maxRamPercentage` | Registration container maximum heap size | `90` |
| `registration.persistentVolumeClaimName` | Point to an existing Registration Persistent Volume Claim (PVC) |  |
| `registration.claimSize` | Registration Persistent Volume Claim (PVC) claim size | `2Gi` |
| `registration.storageClass` | Registration Persistent Volume Claim (PVC) storage class |  |
| `registration.volumeName` | Point to an existing Registration Persistent Volume (PV) |  |
| `registration.nodeSelector` | Registration node labels for pod assignment | `{}` |
| `registration.tolerations` | Registration node tolerations for pod assignment | `[]` |
| `registration.affinity` | Registration node affinity for pod assignment | `{}` |
| `registration.podSecurityContext` | Registration security context at pod level | `{}` |
| `registration.securityContext` | Registration security context at container level | `{}` |
