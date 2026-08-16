---
title: "PostgreSQL pod configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/postgresql-pod-configuration.html"
content_id: "PCJdxgfWumSYHH7M3GN0RA"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:10.619131+00:00"
---

# PostgreSQL pod configuration

| Parameter | Description | Default |
| --- | --- | --- |
| `postgres.registry` | Image repository | `docker.io/centos` |
| `postgres.isExternal` | If true, External PostgreSQL will be used | `true` |
| `postgres.host` | PostgreSQL host (required only if external PostgreSQL is used) |  |
| `postgres.port` | PostgreSQL port | `5432` |
| `postgres.pathToPsqlInitScript` | Full file path of the PostgreSQL initialization script | `external-postgres-init.pgsql` |
| `postgres.ssl` | PostgreSQL SSL | `true` |
| `postgres.adminUserName` | PostgreSQL admin username | `postgres` |
| `postgres.adminPassword` | PostgreSQL admin user password | `testPassword` |
| `postgres.userUserName` | PostgreSQL non admin username | `blackduck_user` |
| `postgres.userPassword` | PostgreSQL non admin user password | `testPassword` |
| `postgres.resources.requests.cpu` | PostgreSQL container CPU request (if external postgres is not used) | `1000m` |
| `postgres.resources.requests.memory` | PostgreSQL container Memory request (if external postgres is not used) | `3072Mi` |
| `postgres.persistentVolumeClaimName` | Point to an existing PostgreSQL Persistent Volume Claim (PVC) (if external postgres is not used) |  |
| `postgres.claimSize` | PostgreSQL Persistent Volume Claim (PVC) claim size (if external postgres is not used) | `150Gi` |
| `postgres.storageClass` | PostgreSQL Persistent Volume Claim (PVC) storage class (if external postgres is not used) |  |
| `postgres.volumeName` | Point to an existing PostgreSQL Persistent Volume (PV) (if external postgres is not used) |  |
| `postgres.confPersistentVolumeClaimName` | Point to an existing PostgreSQL configuration Persistent Volume Claim (PVC) (if external postgres is not used) |  |
| `postgres.confClaimSize` | PostgreSQL configuration Persistent Volume Claim (PVC) claim size (if external postgres is not used) | `5Mi` |
| `postgres.confStorageClass` | PostgreSQL configuration Persistent Volume Claim (PVC) storage class (if external postgres is not used) |  |
| `postgres.confVolumeName` | Point to an existing PostgreSQL configuration Persistent Volume (PV) (if external postgres is not used) |  |
| `postgres.nodeSelector` | PostgreSQL node labels for pod assignment | `{}` |
| `postgres.tolerations` | PostgreSQL node tolerations for pod assignment | `[]` |
| `postgres.affinity` | PostgreSQL node affinity for pod assignment | `{}` |
| `postgres.podSecurityContext` | PostgreSQL security context at pod level | `{}` |
| `postgres.securityContext` | PostgreSQL security context at container level | `{}` |
