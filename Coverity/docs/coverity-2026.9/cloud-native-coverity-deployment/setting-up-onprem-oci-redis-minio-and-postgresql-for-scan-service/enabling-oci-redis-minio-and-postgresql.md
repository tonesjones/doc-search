---
title: "Enabling OCI Redis, MinIO, and PostgreSQL"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/enabling-oci-redis-minio-and-postgresql.html"
content_id: "uu18IB6X7kXKOxd_0TxE6g"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:34.451803+00:00"
---

# Enabling OCI Redis, MinIO, and PostgreSQL

For Redis and MinIO, you can optionally deploy the onPrem OCI Redis, MinIO, and PostgreSQL
Helm charts and images. The onPrem OCI Redis, MinIO, and PostgreSQL Helm charts are included
within the `cnc` chart. To enable onPrem Redis, MinIO, and PostgreSQL, set the
following Helm keys to `true`. This will engage the Redis and MinIO
dependencies in the `Chart.yaml` file. The default value for these keys is
`false`, which disables onPrem Redis and MinIO.

```
onPrem:
  redis: true
  minio: true
  postgres: true
```

The Redis, MinIO, and PostgreSQL Helm overrides that follow are valid when deploying Coverity
in AWS, GCP, and Azure with OnPrem Redis, MinIO, and PostgreSQL.
