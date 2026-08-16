---
title: "PostgreSQL Versions Supported by Black Duck SCA"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/postgresql-versions-supported-by-black-duck-sca.html"
content_id: "6DRz86B48UrEyyRx~hmu~w"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:32:58.573979+00:00"
---

# PostgreSQL Versions Supported by Black Duck SCA

Black Duck SCA continuously updates its support for PostgreSQL versions
to enhance the performance and reliability of its services. This document summarizes
supported versions for both internal PostgreSQL containers and external PostgreSQL
instances, along with migration guidance.

## Supported PostgreSQL Versions

**Internal PostgreSQL Container:**

- As of **Black Duck SCA 2025.10.0**, PostgreSQL 16 is the supported
  version for the internal PostgreSQL container.
- Starting with **Black Duck SCA 2023.10.0**, PostgreSQL
  settings are automatically configured for deployments using the internal
  PostgreSQL container.

**External PostgreSQL Instances:**

- For new external PostgreSQL installations, Black Duck recommends using
  the latest stable version, **PostgreSQL 18**.
- **Preliminary testing support** for **PostgreSQL 19** will be
  introduced in **Black Duck SCA 2027.4.0**. This support will
  be for testing environments only and not for production use.

## Important Notes

- **PostgreSQL Sizing:** Refer to the [Black Duck SCA
  Hardware Scaling Guidelines](https://docs.blackduck.com/access?ft:originId=f598e2689f20062534e28c8999b4550b/42e9daee77bcf342ae2692e1ec6e7746.topic) for sizing recommendations.
- **Antivirus Caution:** Avoid running antivirus scans on the PostgreSQL data
  directory. Antivirus software may lock files and interfere with database
  operations, potentially causing errors such as "too many open files in the
  system."

## Migration Process for PostgreSQL 9.6 to Newer Versions

This section applies to upgrades from PostgreSQL 9.6-based Black Duck SCA versions (releases prior to 2022.2.0) to version
2022.10.0 or later:

- Migration is handled by the **blackduck-postgres-upgrader** container.
- Key migration steps include:
  - Rearrangement of PostgreSQL data volume folder layout to simplify future
    upgrades.
  - Change of the UID owner of the data volume to the new default UID
    (1001), with deployment-specific instructions available.
  - Execution of the `pg_upgrade` script to migrate the
    database to **PostgreSQL 13**.
  - Running a plain `ANALYZE` on the PostgreSQL 13 database
    to initialize query planner statistics.
- After these steps, the **blackduck-postgres-upgrader** container exits.

Note: Refer to [PostgreSQL Version Upgrade Schedule](https://docs.blackduck.com/access?ft:originId=f598e2689f20062534e28c8999b4550b/4d4ac073563d23104e9e1d3c2f88a25e.topic) for
supported upgrade paths from PostgreSQL 9.6 to Newer Versions.
