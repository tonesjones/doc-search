---
title: "Announcements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements.html"
content_id: "vPXLby0sF122TZTD4EVAFQ"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:23.036288+00:00"
---

# Announcements

## Removal of upload-cache service

Encryption is now handled by the Black Duck secrets encryption libraries and key
rotation mechanisms. As a result, the `recover_master_key.sh` and
`bd_get_source_upload_master_key.sh` scripts for handling
SEAL_KEY changes have been removed.

Also, uploaded source files used by the Source tab in Black Duck are not migrated. If
needed, you can rescan the source in an existing or new, temporary project. Note
that source uploads must still be explicitly enabled with
`ENABLE_SOURCE_UPLOADS` (default false) and are still deleted
automatically to meet the `MAX_TOTAL_SOURCE_SIZE_MB` (default 4G) and
`DATA_RETENTION_IN_DAYS` (default 180 days) configuration
settings.

**NOTE**: Uploaded source code will not be migrated by default and migration
scripts are not included as part of the Black Duck 2024.1.0 release. Please contact
Black Duck Support if you require your uploaded source code migrated as part of your
upgrade.

## Scanning hardware requirements changes

Black Duck 2024.1.0 will see a number of changes in scanning hardware requirements
therefore Black Duck customers will need to update their environments and allocate
additional hardware resources where necessary per the guidance below.

Please see [Black Duck Hardware Scaling
Guidelines](https://docs.blackduck.com/access?ft:originId=f598e2689f20062534e28c8999b4550b/42e9daee77bcf342ae2692e1ec6e7746.topic) for
more information.

Table 1. Hardware Scaling Guidelines

| Name | Details | |
| --- | --- | --- |
| 120sph | **Scans/Hour**: 120 **SPH % Increase**: 0%  **APIs/Hour**: 3,000  **Project Versions**: 13,000 | **IOPS**: Read: 15,000 / Write: 15,000 **Black Duck Services**: CPU: 11 core / Memory: 56 GB  **PostgreSQL**: CPU: 4 core / Memory: 16 GB  **Total**: CPU: 15 core / Memory: 72 GB |
| 250sph | **Scans/Hour**: 300 **SPH % Increase**: 20%  **APIs/Hour**: 7,500  **Project Versions**: 15,000 | **IOPS**: Read: 15,000 / Write: 15,000 **Black Duck Services**: CPU: 16 core / Memory: 86 GB  **PostgreSQL**: CPU: 6 core / Memory: 24 GB  **Total**: CPU: 22 core / Memory: 110 GB |
| 500sph | **Scans/Hour**: 650 **SPH % Increase**: 30%  **APIs/Hour**: 18,000  **Project Versions**: 18,000 | **IOPS**: Read: 25,000 / Write: 25,000 **Black Duck Services**: CPU: 23 core / Memory: 133 GB  **PostgreSQL**: CPU: 16 core / Memory: 64 GB  **Total**: CPU: 39 core / Memory: 197 GB |
| 1000sph | **Scans/Hour**: 1400 **SPH % Increase**: 40%  **APIs/Hour**: 26,000  **Project Versions**: 25,000 | **IOPS**: Read: 25,000 / Write: 25,000 **Black Duck Services**: CPU: 46 core / Memory: 367 GB  **PostgreSQL**: CPU: 22 core / Memory: 88 GB  **Total**: CPU: 68 core / Memory: 455 GB |
| 1500sph | **Scans/Hour**: 1600 **SPH % Increase**: 6%  **APIs/Hour**: 41,000  **Project Versions**: 28,000 | **IOPS**: Read: 25,000 / Write: 25,000 **Black Duck Services**: CPU: 57 core / Memory: 459 GB  **PostgreSQL**: CPU: 26 core / Memory: 104 GB  **Total**: CPU: 80 core / Memory: 563 GB |
| 2000sph | **Scans/Hour**: 2300 **SPH % Increase**: 15%  **APIs/Hour**: 50,000  **Project Versions**: 35,000 | **IOPS**: Read: 30,000 / Write: 30,000 **Black Duck Services**: CPU: 64 core / Memory: 565 GB  **PostgreSQL**: CPU: 32 core / Memory: 128 GB  **Total**: CPU: 96 core / Memory: 693 GB |

## Documentation localization

The 2023.10.0 version of the UI, online help, and release notes have been localized
to Japanese and Simplified Chinese.
