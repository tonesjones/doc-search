---
title: "Redis and MinIO dependencies in cnc/Chart.yaml"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/redis-and-minio-dependencies-in-cnc/chart.yaml.html"
content_id: "m6ioyux2EkqpwmBZKbCmJA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:16.247558+00:00"
---

# Redis and MinIO dependencies in cnc/Chart.yaml

The `cnc` Helm chart is a top-level parent chart that now contains several
dependency subcharts: `postgresql`, `minio`,
`redis`, `scan-services,` and
`triage-suggestion-service`. Seeee these dependencies in the
`cnc` chart's `Chart.yaml` file as follows:

```
apiVersion: v2
name: cnc
description: Cloud Native Coverity
type: application
version: 0.0.1
appVersion: "CNC_APP_VERSION"
kubeVersion: ">= 1.31.0-0"
keywords:
  - Coverity
dependencies:
  - name: postgresql
    alias: postgresql
    condition: onPrem.postgres
    version: "18.6.5"
    repository: oci://us-docker.pkg.dev/coverity-cloud-sandbox-dev/bitnami
  - name: minio
    condition: onPrem.minio
    version: "17.0.21"
    repository: oci://us-docker.pkg.dev/coverity-cloud-sandbox-dev/bitnami
  - name: redis
    version: "23.1.3"
    condition: onPrem.redis
    repository: oci://us-docker.pkg.dev/coverity-cloud-sandbox-dev/bitnami
  - name: scan-services
    version: "SCANSERVICES_CHART_VERSION"
    repository: "COVERITY_GAR_HELM_REPO"
    condition: scan-services.enabled
  - name: triage-suggestion-service
    version: "TRIAGE_SUGGESTION_SERVICE_CHART_VERSION"
    repository: "TRIAGE_SUGGESTION_SERVICE_HELM_REPO"
    condition: triage-suggestion-service.enabled
```

The `Chart.yaml` file within the `cnc` chart contains the
following dependencies:

- `minio`: The `minio` dependency selects the optional
  `minio` Helm chart which is embedded within the
  `cnc` chart. See also Enabling OCI Redis, MinIO, and PostgreSQL.
- `redis`: The `redis` dependency selects the optional
  `redis` Helm chart which is embedded within the
  `cnc` chart. See also Enabling OCI Redis, MinIO, and PostgreSQL.
- `postgres`: The `postgres` dependency selects the
  optional `postgres` Helm chart which is embedded within the
  `cnc` chart. See also Enabling OCI Redis, MinIO, and PostgreSQL.
- `scan-services`: The `scan-services` dependency
  deploys the `scan-services`subchart when the condition
  `scan-services.enabled` in the `cnc` chart is
  `true`. If `scan-services.enabled` is
  `false`, the dependency is invalid and the
  `scan-services` subchart is not deployed. See also scan-services.enabled Helm key.

The following key within the redis dependency points to the Docker OCI (Open Container
Initiative) registry location that contains the Redis Helm charts and container
images.

Important: For the 2025.9.2 release, whether upgrading or
installing new, see the section Upgrading to 2025.9.2.

Important: As of the 2025.9.2 release, the registry and
repository that contain the Redis Helm charts and container images is
now:

```
repository: oci://registry-1.docker.io/bitnamicharts
```
