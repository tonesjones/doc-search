---
title: "MinIO PersistentVolumeClaim (PVC) size"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/minio-persistentvolumeclaim-pvc-size.html"
content_id: "8ecGhp6fkxdr6CrAzb6RVw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:17.558383+00:00"
---

# MinIO PersistentVolumeClaim (PVC) size

When calculating the PersistentVolumeClaim (PVC) size in MinIO, consider the
following:

- Each analysis tool version needs 8GB.
- All artifacts, including 3rd-party artifacts, are stored in the same MinIO
  bucket.
- In the `cnc` chart `values.yaml` file, you can
  update the `minio.persistence.size:` Helm key value to satisfy
  your workload and supported tool versions. The default value is
  `50Gi`.

Note: If you are deploying MinIO in AWS and using AWS EBS persistent
storage as MinIO PVC, you will need to install the AWS EBS CSI driver EKS addon as
described in AWS: Using EBS persistent storage as MinIO PVC.
