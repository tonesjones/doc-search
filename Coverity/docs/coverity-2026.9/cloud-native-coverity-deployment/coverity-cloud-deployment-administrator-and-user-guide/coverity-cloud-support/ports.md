---
title: "Ports"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/ports.html"
content_id: "42uyl~VkEQBGidEbXGRlIw"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:41.138840+00:00"
---

# Ports

The following table specifies the Helm keys and default port values, and provides links
for further information.

Table 1. Ports

| Port | Helm key | Default | Notes |
| --- | --- | --- | --- |
| PostgreSQL | ``` postgres:   port: ``` | 5432 | The port for Connect access to the PostgreSQL database. |
| ``` cim:   postgres:     port: ``` |  | This value is inherited from `postgres.port`. |
| ``` scan-service:   postgres:     port: ``` |  | This value is inherited from `postgres.port`. |
| ``` storage-service:   postgres:     port: ``` |  | This value is inherited from `postgres.port`. |
| MinIO | ``` cache-service:   minio:     port: ``` | 9000 |  |
| Redis | ``` cache-service:   redis:     port: ``` | 6379 |  |
| Commit | ``` cim:   cimweb:     commitPort: ``` | 9090 |  |
