---
title: "Announcements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements.html"
content_id: "RjQX7WWZ_t6dGzZBroaEjg"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:47.919171+00:00"
---

# Announcements

## End of support for Docker 18.09.x and 19.03.x.

Support for Docker 18.09.x and 19.03.x has ended in Black Duck 2023.7.0. Docker
20.10.x will be the only version supported.

## Upcoming removal of gen02 sizing guidance

Black Duck 2023.10.0 will be removing gen02 sizing guidance and documents. Please
refer to the [Black Duck Hardware Scaling
Guidelines](https://docs.blackduck.com/access?ft:originId=f598e2689f20062534e28c8999b4550b/42e9daee77bcf342ae2692e1ec6e7746.topic) page for sizing reference.

## Upcoming end of support for PostgreSQL 13

With the upcoming 2023.10.0 release, Black Duck will end support for external
PostgreSQL 13. Please refer to the Black Duck 2023.10.0.
Please refer to the [PostgreSQL Upgrade
Schedule](https://docs.blackduck.com/access?ft:originId=f598e2689f20062534e28c8999b4550b/4d4ac073563d23104e9e1d3c2f88a25e.topic) page
for more information.

## Upcoming PostgreSQL container migration to version 14

Black Duck will migrate its PostgreSQL image to version 14 with the 2023.10.0
release. Customers not using the Black Duck-supplied PostgreSQL image will not be
affected.

## Upcoming upgrade restrictions for PostgreSQL container users

Starting with 2023.10.0, Black Duck will only support direct upgrades from Black Duck
versions that use the PostgreSQL 11 or PostgreSQL 13 containers (i.e., all Black
Duck versions between 2022.2.0 and 2023.7.x inclusive). Users of the
Black Duck-provided PG container upgrading from older Black Duck versions (i.e., all
Black Duck versions prior to 2022.2.0) will require a 2-step upgrade: upgrade to
2023.7.x and then upgrade to 2023.10.x.

## Documentation localization

The 2023.4.0 version of the UI, online help, and release notes have been localized
to Japanese and Simplified Chinese.
