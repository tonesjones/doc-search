---
title: "Logstash pod configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/logstash-pod-configuration.html"
content_id: "OVtoaS~UZ5ok~Sam3nKwnA"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:09.385898+00:00"
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
