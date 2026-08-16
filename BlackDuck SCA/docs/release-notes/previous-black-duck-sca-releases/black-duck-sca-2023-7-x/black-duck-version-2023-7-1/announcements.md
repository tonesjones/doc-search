---
title: "Announcements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements.html"
content_id: "ppfh_cFJAuu_JHaD4d2Bzw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:44.572235+00:00"
---

# Announcements

## Upcoming scanning hardware requirements changes

Black Duck 2023.10.0 will see a number of changes in scanning hardware requirements
therefore Black Duck customers will need to update their environments and allocate
additional hardware resources where necessary per the guidance below.

Table 1. Hardware Scaling Guidelines

| Name | Details | |
| --- | --- | --- |
| 10sph | **Scans/Hour**: 50 **SPH % Increase**: 400%  **APIs/Hour**: 2,500  **Project Versions**: 10,000 | **IOPS**: Read: 15,000 / Write: 9,000 **Black Duck Services**: CPU: 10 core / Memory: 36 GB  **PostgreSQL**: CPU: 2 core / Memory: 8 GB  **Total**: CPU: 12 core / Memory: 44 GB |
| 120sph | **Scans/Hour**: 120 **SPH % Increase**: 0%  **APIs/Hour**: 3,000  **Project Versions**: 13,000 | **IOPS**: Read: 15,000 / Write: 15,000 **Black Duck Services**: CPU: 11 core / Memory: 56 GB  **PostgreSQL**: CPU: 4 core / Memory: 16 GB  **Total**: CPU: 15 core / Memory: 72 GB |
| 250sph | **Scans/Hour**: 300 **SPH % Increase**: 20%  **APIs/Hour**: 7,500  **Project Versions**: 15,000 | **IOPS**: Read: 15,000 / Write: 15,000 **Black Duck Services**: CPU: 16 core / Memory: 85 GB  **PostgreSQL**: CPU: 6 core / Memory: 24 GB  **Total**: CPU: 22 core / Memory: 109 GB |
| 500sph | **Scans/Hour**: 650 **SPH % Increase**: 30%  **APIs/Hour**: 18,000  **Project Versions**: 18,000 | **IOPS**: Read: 25,000 / Write: 25,000 **Black Duck Services**: CPU: 23 core / Memory: 133 GB  **PostgreSQL**: CPU: 16 core / Memory: 64 GB  **Total**: CPU: 39 core / Memory: 197 GB |
| 1000sph | **Scans/Hour**: 1400 **SPH % Increase**: 40%  **APIs/Hour**: 26,000  **Project Versions**: 25,000 | **IOPS**: Read: 25,000 / Write: 25,000 **Black Duck Services**: CPU: 44 core / Memory: 367 GB  **PostgreSQL**: CPU: 22 core / Memory: 88 GB  **Total**: CPU: 66 core / Memory: 455 GB |
| 1500sph | **Scans/Hour**: 1600 **SPH % Increase**: 6%  **APIs/Hour**: 41,000  **Project Versions**: 28,000 | **IOPS**: Read: 25,000 / Write: 25,000 **Black Duck Services**: CPU: 53 core / Memory: 464 GB  **PostgreSQL**: CPU: 26 core / Memory: 104 GB  **Total**: CPU: 79 core / Memory: 568 GB |
| 2000sph | **Scans/Hour**: 2300 **SPH % Increase**: 15%  **APIs/Hour**: 50,000  **Project Versions**: 35,000 | **IOPS**: Read: 30,000 / Write: 30,000 **Black Duck Services**: CPU: 64 core / Memory: 565 GB  **PostgreSQL**: CPU: 32 core / Memory: 128 GB  **Total**: CPU: 96 core / Memory: 693 GB |

Table 2. PostgreSQL Settings

| Name | Details | |
| --- | --- | --- |
| 10sph | **Scans/Hour**: 50 **PostgreSQL CPU/Memory**: 2 core / Memory: 8 GB  `shared_buffers` (MB): 2654  `effective_cache_size` (MB): 3185 | `autovacuum_max_workers`: 4 `maintenance_work_mem` (MB): 512 `max_connections`: 400  `work_mem` (MB): 50 |
| 120sph | **Scans/Hour**: 120 **PostgreSQL CPU/Memory**: CPU: 4 core / Memory: 16 GB  `shared_buffers` (MB): 5336  `effective_cache_size` (MB): 6404 | `autovacuum_max_workers`: 4 `maintenance_work_mem` (MB): 512 `max_connections`: 400  `work_mem` (MB): 50 |
| 250sph | **Scans/Hour**: 300 **PostgreSQL CPU/Memory**: CPU: 6 core / Memory: 24 GB  `shared_buffers` (MB): 8016  `effective_cache_size` (MB): 9619 | `autovacuum_max_workers`: 6 `maintenance_work_mem` (MB): 1024 `max_connections`: 500  `work_mem` (MB): 35 |
| 500sph | **Scans/Hour**: 650 **PostgreSQL CPU/Memory**: CPU: 16 core / Memory: 64 GB  `shared_buffers` (MB): 21439  `effective_cache_size` (MB): 25727 | `autovacuum_max_workers`: 6 `maintenance_work_mem` (MB): 1024 `max_connections`: 500  `work_mem` (MB): 35 |
| 1000sph | **Scans/Hour**: 1400 **PostgreSQL CPU/Memory**: CPU: 22 core / Memory: 88 GB  `shared_buffers` (MB): 29502  `effective_cache_size` (MB): 35403 | `autovacuum_max_workers`: 6 `maintenance_work_mem` (MB): 2048 `max_connections`: 600  `work_mem` (MB): 48 |
| 1500sph | **Scans/Hour**: 1600 **PostgreSQL CPU/Memory**: 26 core / Memory: 104 GB  `shared_buffers` (MB): 34878  `effective_cache_size` (MB): 41854 | `autovacuum_max_workers`: 8 `maintenance_work_mem` (MB): 4096 `max_connections`: 800  `work_mem` (MB): 58 |
| 2000sph | **Scans/Hour**: 2300 **PostgreSQL CPU/Memory**: 32 core / Memory: 128 GB  `shared_buffers` (MB): 42974  `effective_cache_size` (MB): 51569 | `autovacuum_max_workers`: 8 `maintenance_work_mem` (MB): 4096 `max_connections`: 800  `work_mem` (MB): 58 |
