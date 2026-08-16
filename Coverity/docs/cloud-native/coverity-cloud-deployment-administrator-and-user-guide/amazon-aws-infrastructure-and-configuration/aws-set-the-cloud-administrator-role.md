---
title: "AWS: Set the cloud administrator role"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/aws-set-the-cloud-administrator-role.html"
content_id: "uNB~6sC5H_0nfk~XGt1X0A"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:06.706294+00:00"
---

# AWS: Set the cloud administrator role

The administrator needs project administrator role to create the following resources:

- VPC. optional
- EKS clusters.
- RDS.
- For Scan Services, S3.
- For Scan Services, AWS elastic cache.

Refer to the Amazon documentation at <https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-role-administrator.html>.
