---
title: "Announcements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements.html"
content_id: "zt4Bnhkjpl0ptcw_FxQpEw"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:29.267646+00:00"
content_hash: "26d58bb519e9fab48d278506eff4f8db6212c18f1cc6bc160b210077df01a013"
---

# Announcements

## Upcoming requirement: `pg_trgm` extension for PostgreSQL

Starting in Black Duck 2025.7.0, the `pg_trgm` PostgreSQL extension will be required for the `bds_hub` database.

- If you are using the Black Duck-provided PostgreSQL container, no action is required—the extension will be installed automatically during the upgrade.
- If you are using an external PostgreSQL instance, the upgrade process will attempt to install the extension. However, this may fail in environments with restricted permissions (such as Amazon RDS or other managed services).

To avoid migration issues, Black Duck strongly recommends ensuring that the `pg_trgm` extension is installed in the `bds_hub` database before upgrading to 2025.7.0.

- For managed services, refer to your provider's documentation for instructions on enabling database extensions.
- For standard PostgreSQL installations, you can manually install the extension using:

  ```
  CREATE EXTENSION IF NOT EXISTS pg_trgm;
  ```

## Preliminary PostgreSQL 17 support

Black Duck 2025.4.0 introduces preliminary support for PostgreSQL 17 as an external database. This support is for **testing purposes only**, and **production use is not supported** at this time. Customers can evaluate PostgreSQL 17 in non-production environments to assess compatibility ahead of future full support.

## PostgreSQL images now sourced from Docker Library

Starting in Black Duck 2025.4.0, PostgreSQL images will be sourced from Docker Library instead of Bitnami as the base images for Black Duck's PostgreSQL deployment. This transition occurs automatically and requires no action from users.

## HBOM view removed following CVSS 2.0 deprecation

With the removal of CVSS 2.0 support, the HBOM view in Black Duck—previously reliant on CVSS 2.0—will no longer be functional. Customers should use alternative reporting and risk assessment views that support CVSS 3.x and 4.0 for vulnerability prioritization.

## Database migration notice

This release includes a database migration related to vulnerability remediation status handling (See HUB-44855 in the Fixed issues section of the release notes for more details). For customers with large databases, the migration process may take up to an hour or more to complete. No action is required, but we recommend planning for additional migration time during the upgrade process.
