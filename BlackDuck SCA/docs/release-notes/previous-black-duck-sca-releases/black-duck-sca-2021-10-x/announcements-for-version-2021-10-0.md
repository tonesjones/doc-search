---
title: "Announcements for Version 2021.10.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements-for-version-2021.10.0.html"
content_id: "8Q55JBfgvIw9~J6Ky8~S0A"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:52.689122+00:00"
---

# Announcements for Version 2021.10.0

## Enhanced Signature Scanning

The same performance improvements that were introduced to Package Manager Scanning in
the 2021.8.0 release are available in the 2021.10.0 release for Signature Scanning.
A key part of these improvements is Duplicate BOM Detection. With this feature, if a
Signature Scan will not alter the BOM already associated with the specific Project
and Version, then BOM Computation is bypassed.

Additionally, with Enhanced Signature Scanning the JobRunner no longer plays a role
in processing of incoming Package Manager or Signature Scans. Although more system
resources are not required to run Enhanced Signature Scans, it is possible that
minor rebalancing of the containers is required. Please reach out to Black Duck
support who can help you understand if any rebalancing is needed. We encourage all
our customers to do so and take advantage of these improved capabilities.

## Clarification on Detect 7.4 with Black Duck 2021.8.0

In order to ensure full functionality and compatibility, Black Duck version 2021.8.0
requires Detect 7.4. Users can continue to use older versions of Detect with Black
Duck, but may encounter inaccurate dependency types or source views in the BOM when
using aggregated BDIO files.

Upgrading to Detect 7.4 will ensure you avoid these inaccuracies in the BOM.

## PostgreSQL container migration from 9.6 to 11

Black Duck will migrate its PostgreSQL image from version 9.6 to version 11 with the
**2022.2.0** release. Customers not using the Black Duck-supplied PostgreSQL
image will not be affected.

## Black Duck PostgreSQL 9.6 deprecation

As announced in the Black Duck 2020.6.0 release, Black Duck was to end support for
external PostgreSQL 9.6 for the 2021.6.0 release. Starting with the **2022.2.0**
release, Black Duck will no longer work with PostgreSQL 9.6 and will fail to start
if pointed to a PostgreSQL 9.6 instance.

## PostgreSQL support schedule

Starting with the upcoming **2022.10.0** release, Black Duck will end support for
external PostgreSQL 11. Please see the table below for the projected dates for the
beginning and end of support for future PostgreSQL versions.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| PG Version | First Release | Last Release | BD External Support Added | BD External Support End |
| 16.x | Late 2023 | Late 2028 | 2024.10.0 | 2026.10.0 |
| 15.x | Late 2022 | Late 2027 | 2023.10.0 | 2025.10.0 |
| 14.x | September 2021 | November 2026 | 2022.10.0 | 2024.10.0 |
| 13.x | September 2020 | November 2025 | 2021.8.0 | 2023.10.0 |
| 12.x | October 2019 | November 2024 | X | X |
| 11.x | October 2018 | November 2023 | 2020.6.0 | 2022.10.0 |

## Database bds_hub_report deprecation starting with 2021.10.0

Starting with 2021.10.0, new installations of Black Duck will no longer create the
`bds_hub_report` database. We plan to finally delete
`bds_hub_report` in 2022.10.0.

Also, the `hub_create_data_dump.sh` and
`hub_db_migrate.sh` scripts (which are distributed with our
orchestration files) will no longer fail if `bds_hub_report` does not
exist.

- The `hub_create_data_dump.sh` script will dump
  `bds_hub_report` if it exists but will not fail if it
  doesn't. If `bds_hub_report` is absent, the script will
  print a message saying it was skipped.
- The `hub_db_migrate.sh` script will try to restore
  `bds_hub_report` if it exists, regardless of whether
  or not a dump file is present (matching the behavior of prior releases).
  If `bds_hub_report` is not present, it will not try to
  restore it, also regardless of whether or not a dump file is
  present.
- A new script, `hub_recreate_reportdb.sh` is added to recreate
  `bds_hub_report` if a user wants propagate their
  `bds_hub_report` DBs from 2021.8.x or earlier to a new
  install of 2021.10.0 or later. In this case;
  - Run `hub_create_data_dump.sh` on the old BD
    instance.
  - Run `hub_recreate_reportdb.sh` on the new BD
    instance.
  - Run `hub_db_migrate.sh` on the new BD instance
    with the dumps created in step #1.

## Upcoming max page limit enforcement for API requests

Starting with Black Duck **2022.2.0**, max page limits on API requests will be
enforced. Users should make singular requests that include a limit request parameter
smaller or equal to the documented page limit. Requests for pages greater than the
documented limit will be truncated to only return the maximum accepted page limit.
Requests for page sizes will not be rejected but return a maximum number of results
per paged request.

This will be an ongoing effort lasting subsequent releases to improve application
stability and prevent performance degradation from unreasonably large requests.

## Deprecated APIs

The following defunct endpoints will now return a 404 NOT FOUND error to indicate
that access to the target resource is no longer available:

- GET /oauthclients
- POST /oauthclients
- DELETE /oauthclients/{oAuthClientId}
- GET /oauthclients/{oAuthClientId}
- PUT /oauthclients/{oAuthClientId}
- POST /vulnerabilities/vulndb-copy

## Japanese language

The 2021.8.0 version of the UI, online help, and release notes has been localized to
Japanese.

## Simplified Chinese language

The 2021.8.0 version of the UI, online help, and release notes has been localized to
Simplified Chinese.
