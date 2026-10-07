---
title: "PostgreSQL Versions Supported by Black Duck SCA"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/postgresql-versions-supported-by-black-duck-sca.html"
content_id: "bR4URSvD3QrOxEDTSxmmjw"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-10-04T23:32:22.449374+00:00"
content_hash: "d19e470b18beda8f00ed97c1838ee496a556df5ed3f9911c1cbd6758f741663f"
---

# PostgreSQL Versions Supported by Black Duck SCA

Black Duck SCA continuously updates its support for PostgreSQL versions to enhance the performance and reliability of its services. This document summarizes supported versions for both internal PostgreSQL containers and external PostgreSQL instances, along with migration guidance.

## Supported PostgreSQL Versions

**Internal PostgreSQL Container:**

- As of **Black Duck SCA 2025.10.0**, PostgreSQL 16 is the supported version for the internal PostgreSQL container.
- Starting with **Black Duck SCA 2023.10.0**, PostgreSQL settings are automatically configured for deployments using the internal PostgreSQL container.

**External PostgreSQL Instances:**

- For new external PostgreSQL installations, Black Duck recommends using the latest stable version, **PostgreSQL 18**.
- **Preliminary testing support** for **PostgreSQL 19** will be introduced in **Black Duck SCA 2027.4.0**. This support will be for testing environments only and not for production use.

## Important Notes

- **PostgreSQL Sizing:** Refer to the [Black Duck SCA Hardware Scaling Guidelines](https://docs.blackduck.com/access?ft:originId=f598e2689f20062534e28c8999b4550b/42e9daee77bcf342ae2692e1ec6e7746.topic) for sizing recommendations.
- **Antivirus Caution:** Avoid running antivirus scans on the PostgreSQL data directory. Antivirus software may lock files and interfere with database operations, potentially causing errors such as "too many open files in the system."
