---
title: "Coverity tools in a Coverity cloud deployment"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-tools-in-a-coverity-cloud-deployment.html"
content_id: "Co_EpKGzMOENEyKkbPMx2g"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:46:07.093697+00:00"
---

# Coverity tools in a Coverity cloud deployment

The following Coverity commands have cloud-specific requirements that you must meet as
described in the sections that follow. The following table identifies these commands and
provides links to the sections that describe the cloud requirements.

Table 1. Coverity tools

| Connect tool script or command | Section |
| --- | --- |
| `check-integrity.sh` | Checking database integrity: check-integrity.sh |
| `reset-admin-password.sh` | Resetting the Coverity Connect password: reset-admin-password.sh |
| `cov-archive.sh` | Managing archives: cov-archive.sh |
| `cov-manage-im` | Managing Coverity Connect: cov-manage-im |

Note: While performing operations defined in this chapter, these scripts and commands can be
used with all applicable options as described in the section Coverity Connect
commands in the Coverity 2026.6.0 Command Reference.

Note: For any script or command that will perform a write operation in
either a `cim-tools` pod or a `cnc-db-admin` pod, you must
write the output file to `/workdir`.

Note: If you encounter a Read Only File System error while executing
any of our scripts or binaries within a Connect pod, refer to Read-only file system error.
