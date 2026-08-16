---
title: "Docker base images"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/docker-base-images.html"
content_id: "2wq4tpqj0JatpN8_p~GzHA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:58.914761+00:00"
---

# Docker base images

The following tables specify the Docker base images used by Black Duck to create the Coverity container images for the
Coverity cloud services. The tables specify base images for:

- Docker base images for Alpine Linux and debian Linux.
- Docker base images for Universal Base Image (UBI).
- Docker base images for third-party container images.

For further information on Docker base images, see <https://docs.docker.com/build/building/base-images/>.

The following table identifies the base images used for Coverity Connect and Scan
Services container images.

Table 1. Docker base images for Alpine Linux and debian Linux

| Black Duck® Coverity® container image | Base image used |
| --- | --- |
| `cim-downloads:2026.6.0` | Alpine Linux: 3.21 |
| `cov-manage-im:2026.6.0` |
| `cache-service:2026.6.0` | Azul Zulu on Alpine Linux:  azul/zulu-openjdk-alpine:21-jre |
| `cim-tools:2026.6.0` | Azul Zulu on Alpine Linux:  azul/zulu-openjdk-alpine:17-jre |
| `cim-web:2026.6.0` |
| `scan-service-migration:2026.6.0` | Azul Zulu on Alpine Linux:  azul/zulu-openjdk-alpine:11-jre |
| `storage-service-migration:2026.6.0` |
| `job-runner:2026.6.0` | debian Linux: bullseye-slim |
| `common-infra:2026.6.0` | scratch |
| `scan-service:2026.6.0` |
| `storage-service:2026.6.0` |

The following table identifies the base images used for Coverity Connect and Scan
Services container images created for Red Hat UBI.

Table 2. Docker base images for Red Hat UBI

| Black Duck® Coverity® container image | Base image used |
| --- | --- |
| `cache-service:2026.6.0-ubi` | Red Hat UBI 9.5 |
| `cim-downloads:2026.6.0-ubi` | Red Hat UBI 9.5 |
| `job-runner:2026.6.0-ubi` |
| `cim-tools:2026.6.0-ubi` | Red Hat UBI 9 openjdk-17:1.22 |
| `cim-web:2026.6.0-ubi` |
| `scan-service-migration:2026.6.0-ubi` |
| `storage-service-migration:2026.6.0-ubi` |
| `common-infra:2026.6.0-ubi` | scratch |
| `scan-service:2026.6.0-ubi` |
| `storage-service:2026.6.0-ubi` |

The following table identifies the base image used for third-party container images.

Table 3. Docker base image for third-party container images

| Third-party container image | Base image used |
| --- | --- |
| `nginx:1.27.4` | `nginx:1.27.4` |
| `pgpool:4.6.0` | The Pgpool container image base file is `minideb`, which is a small Debian-based container image. |

Note: For customer-provided client containers running
pg_dump/pg_restore outside the product, the base image must be Ubuntu 22+ or an
equivalent distribution.
