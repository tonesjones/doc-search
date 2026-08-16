---
title: "Setting MinIO storage type Helm keys"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/setting-minio-storage-type-helm-keys.html"
content_id: "s_7FpfPK4fhI_gJWs28aSA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:42.958395+00:00"
---

# Setting MinIO storage type Helm keys

If you are using MinIO as a storage type with the Storage Service, instead of setting the
storage type using the `cnc.storage-service.s3` Helm keys, you need to
set up MinIO using the following Helm keys in the `scan-services` chart:

- `storage-service.minio.bucket`
- `storage-service.minio.secret.name`
- `storage-service.minio.region`

Refer to these Helm keys in scan-services Helm subchart: Helm keys.

For information on the Storage Service MinIO secret, see Creating a secret for MinIO storage type.
