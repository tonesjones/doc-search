---
title: "Announcements for Version 2022.7.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements-for-version-2022.7.0.html"
content_id: "O1Q2WVADhR7K1wSTxbuDmg"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:31.942900+00:00"
---

# Announcements for Version 2022.7.0

## PostgreSQL 9.6 deprecation

As previously announced, support for running Black Duck on PostgreSQL 9.6 ended with
the 2021.6.0 release of Black Duck. Starting with the 2022.7.0 release of Black
Duck, attempting to run Black Duck with PostgreSQL 9.6 will generate an error, and
Black Duck will fail to start.

## Upcoming PostgreSQL 11 deprecation

Support for running Black Duck on PostgreSQL 11 will end with the 2022.10.0 release.
Starting with that release, attempting to run Black Duck with PostgreSQL 11 will
generate an error and Black Duck will fail to start.

## PostgreSQL container migration from 11 to 13

Black Duck will migrate its PostgreSQL image from version 11 to version 13 with the
**2022.10.0** release. Customers not using the Black Duck-supplied PostgreSQL
image will not be affected.

## Upcoming custom-fields API change

In the 2023.1.0 release of Black Duck, the following APIs will change to return
errors when trying to read or change a custom field that is disabled. The field will
need to be re-enabled before it can be accessed.

- ```
  GET api/components/{componentId}/custom-fields/{custom-field-id}
  ```
- ```
  PUT api/components/{componentId}/custom-fields/{custom-field-id}
  ```
- ```
  GET api/components/{componentId}/versions/{componentVersionId}/custom-fields/{custom-field-id}
  ```
- ```
  PUT api/components/{componentId}/versions/{componentVersionId}/custom-fields/{custom-field-id}
  ```

## Support for legacy signature scans and legacy package manager scans deprecation

This functionality will be officially sunset in the Black Duck 2023.7.0 release.

Customers should upgrade to Detect 8.x to ensure compatibility. Detect 8.x is
tentatively targeted for release in May/June 2022 which aligns with Black Duck
2022.7.0 release and this deprecation release note. This will give customers a one
year period to upgrade Detect in alignment to the future sunset date.

## Upcoming Helm2 end of support

Starting with the 2023.1.0 release, Black Duck will no longer support Helm2 for
Kubernetes deployments. The minimum supported version of Kubernetes will increase to
1.13 (the oldest version supported by Helm3).

## Correction: Git repository SCM Integration - Phase 1

Instructions provided in the 2022.4.0 release notes regarding enabling Git repository
SCM Integration in Black Duck for Swarm users were incorrect. The correct variable
setup is as follows:

For your `docker-compose.yaml` webapp environment:

```
webapp:
  environment:
    blackduck.scan.scm.enableIntegration: 'true'
```

Also, in your `blackduck-config.env` file, add the following:

```
blackduck.scan.scm.enableIntegration=true
```

## Updated PostgreSQL support schedule

Starting with the upcoming **2022.10.0** release, Black Duck will end support for
external PostgreSQL 11. Please see the table below for the projected dates for the
beginning and end of support for future PostgreSQL versions.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| PG Version | First Release | Last Release | BD External Support Added | BD External Support End |
| 16.x | Late 2023 | Late 2028 | 2024.7.0 | 2026.10.0 |
| 15.x | Late 2022 | Late 2027 | 2023.7.0 | 2025.10.0 |
| 14.x | September 2021 | November 2026 | 2022.7.0 | 2024.10.0 |
| 13.x | September 2020 | November 2025 | 2021.8.0 | 2023.10.0 |
| 12.x | October 2019 | November 2024 | X | X |
| 11.x | October 2018 | November 2023 | 2020.6.0 | 2022.10.0 |

## Japanese language

The 2022.4.0 version of the UI, online help, and release notes has been localized to
Japanese.

## Simplified Chinese language

The 2022.4.0 version of the UI, online help, and release notes has been localized to
Simplified Chinese.
