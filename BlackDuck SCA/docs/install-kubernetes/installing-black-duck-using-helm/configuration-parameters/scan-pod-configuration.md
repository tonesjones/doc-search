---
title: "Scan pod configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/scan-pod-configuration.html"
content_id: "a1CZuADRX0Ec2M3q3KoYHA"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-10-04T23:32:23.147692+00:00"
content_hash: "88735b6261d0deab43b0659c90c35bc9a6a73109304f0adbc391c4c7cbb464a3"
---

# Scan pod configuration

| Parameter | Description | Default |
| --- | --- | --- |
| `scan.registry` | Image repository to be override at container level |  |
| `scan.replicas` | Scan Pod Replica Count | `1` |
| `scan.resources.limits.memory` | Scan container Memory Limit | `2560Mi` |
| `scan.resources.requests.memory` | Scan container Memory request | `2560Mi` |
| `scan.maxRamPercentage` | Scan container maximum heap size | `90` |
| `scan.nodeSelector` | Scan node labels for pod assignment | `{}` |
| `scan.tolerations` | Scan node tolerations for pod assignment | `[]` |
| `scan.affinity` | Scan node affinity for pod assignment | `{}` |
| `scan.podSecurityContext` | Scan security context at pod level | `{}` |
| `scan.securityContext` | Scan security context at container level | `{}` |
