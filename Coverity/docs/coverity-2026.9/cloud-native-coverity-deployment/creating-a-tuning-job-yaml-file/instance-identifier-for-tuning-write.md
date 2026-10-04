---
title: "Instance identifier for tuning-write"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/instance-identifier-for-tuning-write.html"
content_id: "u4gqpe1gaztxOrVyi4Nx~A"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:27.008012+00:00"
---

# Instance identifier for tuning-write

If the database is present on a cloud provider (`<POSTGRES-DISTRO>` is
`rds`, `flexibleserver`, or
`cloudsql`), and if you are performing a tuning-write, add the instance
identifier/name. In the tuning yaml file, replace
`<INSTANCE_IDENTIFIER>` with the database instance name of the
instance from the cloud provider.

If `<POSTGRES-DISTRO>` is `other'`, the instance
identifier is not needed.
