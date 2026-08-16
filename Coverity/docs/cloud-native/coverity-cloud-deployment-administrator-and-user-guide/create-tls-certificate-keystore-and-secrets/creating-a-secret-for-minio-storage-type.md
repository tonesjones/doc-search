---
title: "Creating a secret for MinIO storage type"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/creating-a-secret-for-minio-storage-type.html"
content_id: "Q69WzspkfyEi3yR3IuXSjg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:06.074811+00:00"
---

# Creating a secret for MinIO storage type

If you are using MinIO as a storage type with the Storage Service, you need to create a
MinIO secret using the `kubectl` command as follows:

```
kubectl create secret generic "${MINIO_SECRET_NAME}" \
  --namespace "${CNC_NS}" \
  --from-literal=root-user="${MINIO_ACCESS_KEY}" \
  --from-literal=root-password="${MINIO_SECRET_KEY}" \
  -o yaml
```

You will need to set the MinIO Helm keys as described in Setting MinIO storage type Helm keys.
