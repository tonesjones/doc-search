---
title: "Google GCP administrator privileges/roles"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/google-gcp-administrator-privileges/roles.html"
content_id: "LfpAI6GA3XmHPeiXrvfZmg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:21.943646+00:00"
---

# Google GCP administrator privileges/roles

Individual Google GCP account privileges include the following IAM roles:

Important:

In Google GCP, the minimum storage bucket permission must be
**storage.buckets.update** which is within the
**roles/storage.legacyBucketOwner** role.

Table 1. Google GCP IAM roles for Coverity cloud

| Role | Permission | Refer to |
| --- | --- | --- |
| `roles/owner` | Full access and control for all Google Cloud resources. | <https://cloud.google.com/memorystore/docs/redis/access-control> |
| `roles/redis.admin` | Redis administrator. Needed if you are deploying Scan Services. |
| `roles/container.admin` | Kubernetes engine administrator. | <https://cloud.google.com/iam/docs/understanding-roles> |
| `roles/compute.networkAdmin` | Compute network administrator. | <https://cloud.google.com/compute/docs/access/iam> |
| `roles/compute.securityAdmin` | Compute security administrator. |
| `roles/iam.serviceAccountUser` | Service account user. |
| `roles/compute.viewer` | Compute viewer. |
| `roles/cloudsql.admin` | Cloud SQL administrator. | <https://cloud.google.com/sql/docs/mysql/iam-roles> |
| `roles/storage.legacyBucketOwner` | The Storage Legacy Bucket Owner role contains permissions including `storage.buckets.update` which is required. | <https://cloud.google.com/storage/docs/access-control/iam-roles> |
