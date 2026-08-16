---
title: "Announcements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements.html"
content_id: "BwDHp1fZFwIucsG523m__A"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:07.691059+00:00"
---

# Announcements

## KnowledgeBase upgrade post upgrade

Please be aware that a KnowledgeBase update job will run upon completion of Black Duck upgrade. This update addresses outdated KnowledgeBase
component license data resulting from a previous bug. Depending on the size of your
deployment, the job may take up to 4 hours to complete, though typical durations are
shorter. This process will not impact scans or other Black Duck
processes. However, during the execution of this job, you may observe increased CPU
and memory usage in the Job runner pods.

## Updated Activity Audit Trail

The Activity Audit Trail feature allows for the retention of activity audit records
of user actions and key events, such as project version component and vulnerability
records, in the application affecting a project and/or project version.

With this update, the functionality can now be disabled to improve performance and
decrease storage costs, giving you greater flexibility and control over your
project's audit records. When Activity Audit Trail is disabled, activity data is not
tracked. Re-enabling it will start tracking activity from that moment on.

This feature is disabled by default for fresh installations but remains enabled for
existing installations and upgrades.

## PostgreSQL 16 support for external databases

Black Duck now supports and recommends PostgreSQL 16 for new installs that use
external PostgreSQL. However, Google CloudSQL for PostgreSQL does not yet support
PostgreSQL 16; on that platform, Black Duck recommends PostgreSQL 15.

Migrating to 2024.7.x does not require migration to PostgreSQL 16.

No action is required for users of the internal PostgreSQL container.

## Upcoming end of support for PostgreSQL 14

With the upcoming 2024.10.0 release, Black Duck will end support
for external PostgreSQL 14. Please refer to the Black Duck
2023.10.0. Please refer to the [PostgreSQL
Upgrade Schedule](https://docs.blackduck.com/access?ft:originId=f598e2689f20062534e28c8999b4550b/4d4ac073563d23104e9e1d3c2f88a25e.topic) page for more information.

## Upcoming PostgreSQL container migration to version 15

Black Duck will migrate its PostgreSQL image to version 15 with the 2024.10.0
release. Customers not using the Black Duck-supplied PostgreSQL image will not be
affected.

## Upcoming upgrade restrictions for PostgreSQL container users

For users of the Black Duck-provided PostgreSQL container, Black Duck
2024.10.0 will only support direct upgrades from earlier versions of Black Duck that use the PostgreSQL versions 13 or PG 14 containers
(2022.10.0 to 2024.7.x inclusive).

Upgrading from older Black Duck versions (prior to 2022.10.0) will
require a 2-step upgrade:

1. Upgrade to Black Duck 2023.7.x.
2. Upgrade to Black Duck 2024.10.x.

## Upcoming webserver technology replacement

In an upcoming Black Duck release (2024.10.0 or 2025.1.0), the
existing ingress webserver (NGiNX) will be replaced with a new technology, Apache
APISIX. Customers with existing custom NGiNX configuration will need to update their
settings to ensure compatibility.

## Documentation localization

The 2024.4.0 version of the UI, online help, and release notes have been localized
to Japanese and Simplified Chinese.

Starting with 2024.7.0, updated Japanese and Simplified Chinese localizations of the
documentation will be posted on the [Black Duck Documentation
Portal](https://docs.blackduck.com/access?ft:originId=dad2192abc2e53d01fcee1313e1aa841/5bbb905bedd31850d3fe34d6407f0c43.topic) immediately when available.
