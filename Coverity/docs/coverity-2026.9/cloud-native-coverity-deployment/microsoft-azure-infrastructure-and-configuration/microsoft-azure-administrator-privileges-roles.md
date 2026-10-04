---
title: "Microsoft Azure administrator privileges/roles"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/microsoft-azure-administrator-privileges/roles.html"
content_id: "4kX95N0wiYtSSan~DX2_8Q"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:24.062272+00:00"
---

# Microsoft Azure administrator privileges/roles

The administrator needs project administrator privileges to create the following
resources:

- VNET.
- AKS cluster.
- Azure PostgreSQL Flexible server.
- For Scan Services, storage containers.
- For Scan Services, Redis.

Important:

In Microsoft Azure, the minimum storage blob permission must be **Storage Blob Data
Contributor**. This role allows users to manage and read/write data to the
storage account.

Refer to Microsoft Azure documentation at <https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions?view=azure-devops&tabs=preview-page>.
