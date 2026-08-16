---
title: "Amazon AWS account privileges"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/amazon-aws-account-privileges.html"
content_id: "sykve~m01JNGbx3n5nEwKg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:06.054667+00:00"
---

# Amazon AWS account privileges

The administrator needs project administrator role to create the following resources:

- VPC
- EKS clusters
- RDS
- For Scan Services, S3
- For Scan Services, AWS elastic cache

Refer to the Amazon documentation at <https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-role-administrator.html>.

## Storage Service privileges

For information on setting permissions and using a role-based AWS service account for
Storage Service and Cache Service, refert to Using a role-based AWS service account for Storage Service and Cache Service.
