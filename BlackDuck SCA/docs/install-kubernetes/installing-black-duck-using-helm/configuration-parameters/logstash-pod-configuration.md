---
title: "Logstash pod configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/logstash-pod-configuration.html"
content_id: "7wlQazYb0qy9jLfL3wUdGA"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-10-04T23:32:22.933914+00:00"
content_hash: "03019e5a3d5559185d5d1426c18c37939f90887887aa770641187d6a545c694c"
---

# Logstash pod configuration

| Parameter | Description | Default |
| --- | --- | --- |
| `logstash.registry` | Image repository to be override at container level |  |
| `logstash.imageTag` | Image tag to be override at container level | `1.0.38` |
| `logstash.resources.limits.memory` | Logstash container Memory Limit | `1024Mi` |
| `logstash.resources.requests.memory` | Logstash container Memory request | `1024Mi` |
| `logstash.maxRamPercentage` | Logsash maximum heap size | `90` |
| `logstash.persistentVolumeClaimName` | Point to an existing Logstash Persistent Volume Claim (PVC) |  |
| `logstash.claimSize` | Logstash Persistent Volume Claim (PVC) claim size | `20Gi` |
| `logstash.storageClass` | Logstash Persistent Volume Claim (PVC) storage class |  |
| `logstash.volumeName` | Point to an existing Logstash Persistent Volume (PV) |  |
| `logstash.nodeSelector` | Logstash node labels for pod assignment | `{}` |
| `logstash.tolerations` | Logstash node tolerations for pod assignment | `[]` |
| `logstash.affinity` | Logstash node affinity for pod assignment | `{}` |
| `logstash.securityContext` | Logstash security context at container level | `{}` |
