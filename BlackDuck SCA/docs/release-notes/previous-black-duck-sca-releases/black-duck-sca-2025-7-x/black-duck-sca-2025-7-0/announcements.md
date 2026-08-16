---
title: "Announcements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements.html"
content_id: "yWQyC1xDQisImo1VJe1uKg"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:27.836325+00:00"
---

# Announcements

## Updated project version BOM view with new Vulnerabilities tab

We have made significant updates to the project version BOM view by replacing the
Security tab with a new Vulnerabilities tab. This redesigned tab offers an improved
layout while continuing to provide essential vulnerability insights. Users will
benefit from enhanced filtering options, clearer presentation of vulnerability data,
and quicker access to remediation details in a more intuitive interface.

The new Vulnerabilities tab changes the way vulnerabilities are remediated, allowing
for remediation at the component version level. This means there is no longer a need
to remediate individual component origins identified from scans, reducing the
overall remediation steps required. Additionally, bulk remediation of multiple
vulnerabilities affecting one or more component versions is now supported.

We are also introducing new public vulnerability APIs to facilitate this
functionality for customers looking to automate remediation steps. The existing APIs
will remain available and have not been deprecated, but we encourage customers to
consider transitioning to the new, more efficient APIs that focus on component
version-level remediation. Existing remediation for component origins will be
carried forward when upgrading to version 2025.7.0.

## Upcoming PostgreSQL container migration to version 16

Starting in **2025.10.0**, Black Duck will upgrade the
PostgreSQL container image to PostgreSQL 16. This migration ensures improved
performance, stability, and access to the latest PostgreSQL features. Customers
using the packaged PostgreSQL container should validate their environments for
compatibility with PostgreSQL 16 prior to upgrading. No action is required for those
using external databases.

## Upcoming upgrade restriction for PostgreSQL container users

Starting in **2025.10.0**, Black Duck will only support
direct upgrades to the bundled PostgreSQL container (PostgreSQL 16) from versions
that already use PostgreSQL 14 or 15—specifically, Black Duck
2023.10.0 through 2025.7.x.

If you are using a Black Duck version prior to 2023.10.0, you
will need to perform a two-step upgrade:

1. First upgrade to 2024.7.x
2. Then upgrade to 2025.10.x

This change applies only to users of the Synopsys-provided PostgreSQL container.
Users with external database configurations are not affected.

## Upcoming end of support for PostgreSQL 15

Support for **PostgreSQL 15** will end with the **2025.10.0** release of Black Duck.

Users currently using the PostgreSQL 15 container should plan to upgrade to
PostgreSQL 16 by of before that release.

External database configurations should follow standard compatibility guidance.

## Extended Testing Period for PostgreSQL 17 Support

Black Duck is extending the testing-only period for PostgreSQL
17 as an external database option due to a discovered performance degradation with
PG 17.x. While our investigation is ongoing to resolve this issue, we do not
recommend using PG 17.x in production environments at this time. Therefore,
evaluation-only support for PG 17.x has been extended.

Please note, this extension does not affect our planned end of support for PostgreSQL
15.x, which will occur with the release of Black Duck
2025.10.0. Stay tuned for further updates as we work towards full production support
for PostgreSQL 17.x in future releases.

## PostgreSQL 17 support for external databases

Black Duck now supports and recommends PostgreSQL 17 for new
installs that use external PostgreSQL.

Migrating to 2025.7.x does not require migration to PostgreSQL 17.

No action is required for users of the internal PostgreSQL container.

## New requirement: `pg_trgm` extension for PostgreSQL

Starting in Black Duck 2025.7.0, the `pg_trgm`
PostgreSQL extension is required for the `bds_hub` database.

- If you are using the Black Duck-provided PostgreSQL
  container, no action is required—the extension will be installed
  automatically during the upgrade.
- If you are using an external PostgreSQL instance, the upgrade process will
  attempt to install the extension. However, this may fail in environments
  with restricted permissions (such as Amazon RDS or other managed
  services).

To avoid migration issues, Black Duck strongly recommends
ensuring that the `pg_trgm` extension is installed in the
`bds_hub` database before upgrading to 2025.7.0.

- For managed services, refer to your provider's documentation for instructions
  on enabling database extensions.
- For standard PostgreSQL installations, you can manually install the extension
  using:

  ```
  CREATE EXTENSION IF NOT EXISTS pg_trgm;
  ```

## Upcoming scan and matchengine container merger

In the 2025.10.0 release, the `scan` and `matchengine`
containers will be merged into a single `scanmatch` container. This
change is part of ongoing efforts to reduce resource requirements and simplify Black Duck SCA deployments.

## Upcoming scan endpoint deprecations

To improve maintainability and streamline the Black Duck API,
several legacy scan-related endpoints are scheduled for deprecation in upcoming
releases. The table below outlines the endpoints affected, along with their
deprecation timelines.

- Only the specifically listed scan types are affected for the endpoints
  that support multiple scan types.
- Customers using any of the affected endpoints are encouraged to contact
  their account team or Technical Support for assistance or migration
  guidance.

Customers using a fully supported version of Detect (9, 10) at the time of API
removal will not be affected and do not need to take any action. None of the
supported Detect versions rely on the APIs scheduled for removal in 2026.4.0. By
2027.4.0, Detect 11 will be the oldest supported version, and it does not use any of
the deprecated APIs. For more information, see [Black Duck Detect end of support and service
schedule](https://docs.blackduck.com/access?ft:originId=f598e2689f20062534e28c8999b4550b/91f189a986ea2cd2782693d60ea03cbf.topic).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **API Endpoint** | **Content Type** | **Deprecated With** | **Removed With** | **Scan Types** |
| `POST /v1/scans` | *NULL, application/vnd.blackducksoftware.internal-cli-1* | 2025.7.0 | 2026.4.0 | - Package Manager - Signature |
| `PUT /v1/scans/{scanId}` | *NULL, application/vnd.blackducksoftware.internal-cli-1* | 2025.7.0 | 2026.4.0 | - Package Manager - Signature |
| `POST /bom-import` | *application/ld+json* | 2025.7.0 | 2028.1.0 | - Package Manager - Signature |
| `POST /intelligent-persistence-scans` | *application/vnd.blackducksoftware.intelligent-persistence-scan-1-ld-2+json*  *application/vnd.blackducksoftware.intelligent-persistence-scan-2-ld-2+json*  *application/vnd.blackducksoftware.intelligent-persistence-scan-3+protobuf* | 2025.7.0 | 2027.4.0 | - Package Manager - Signature - Binary - Container |
| `PUT /intelligent-persistence-scans/{scanId}` | *application/vnd.blackducksoftware.intelligent-persistence-scan-1-ld-2+json*  *application/vnd.blackducksoftware.intelligent-persistence-scan-2-ld-2+json*  *application/vnd.blackducksoftware.intelligent-persistence-scan-3+protobuf* | 2025.7.0 | 2027.4.0 | - Package Manager - Signature - Binary - Container |
| `POST /uploads` | *multipart/form-data* | 2025.1.0 | 2027.4.0 | - Binary |
| `POST /uploads/multipart` | *application/vnd.blackducksoftware.binary-multipart-upload-start-1+json* | 2025.1.0 | 2027.4.0 | - Binary |
| `PUT /uploads/multipart/{scanId}` | *application/vnd.blackducksoftware.multipart-upload-data-1+octet-stream* | 2025.1.0 | 2027.4.0 | - Binary |
| `POST /uploads/multipart/{id}/completed` | *application/vnd.blackducksoftware.multipart-upload-finish-1+json* | 2025.1.0 | 2027.4.0 | - Binary |
| `POST /storage/containers/{scanId}` | *application/vnd.blackducksoftware.container-scan-data-1+octet-stream* | 2025.1.0 | 2027.4.0 | - Container |
| `POST /storage/containers/{id}/message` | *application/vnd.blackducksoftware.container-scan-message-1+json* | 2025.1.0 | 2027.4.0 | - Container |
| `POST /storage/containers/{id}/multipart` | *application/vnd.blackducksoftware.multipart-upload-start-1+json* | 2025.1.0 | 2027.4.0 | - Container |
| `PUT /storage/containers/{id}/multipart` | *application/vnd.blackducksoftware.multipart-upload-data-1+octet-stream* | 2025.1.0 | 2027.4.0 | - Container |
| `POST /storage/containers/{id}/multipart/completed` | *application/vnd.blackducksoftware.multipart-upload-finish-1+json* | 2025.1.0 | 2027.4.0 | - Container |
