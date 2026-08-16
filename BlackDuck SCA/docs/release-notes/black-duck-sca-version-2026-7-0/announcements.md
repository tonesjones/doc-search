---
title: "Announcements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements.html"
content_id: "AXlJAlj9OnxEec_i7rP2ag"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:34:47.071525+00:00"
---

# Announcements

## Upcoming removal of the Archived project version phase

The Archived project version phase will be removed in a future release (2026.11.0).
Starting with that release, all capabilities related to the Archived project phase
will no longer be available.

If you have project versions currently in the archived phase, we strongly recommend
transitioning them to LTS before upgrading. Any Archived project versions remaining
at the time of upgrade will be automatically transitioned to LTS.

## Upcoming upgrade restrictions for PostgreSQL container users

In the upcoming 2026.10.0 release, users of the Black Duck SCA-supplied PostgreSQL container should be aware of new upgrade restrictions. This
version will only support direct upgrades from Black Duck SCA
versions that utilize PostgreSQL 15 or PG 16 containers, specifically covering all
Black Duck SCA versions between 2024.10.0 and 2026.7.x
(inclusive).

For users upgrading from older Black Duck SCA versions (prior to
2024.10.0), a two-step upgrade process will be required: first, upgrade to version
2025.7.x (or later), and then proceed to upgrade to version 2026.10.x.

## Upcoming PostgreSQL container migration to version 17

Starting in **2026.10.0**, Black Duck SCA will upgrade the
PostgreSQL container image to PostgreSQL 17. This migration ensures improved
performance, stability, and access to the latest PostgreSQL features. Customers
using the packaged PostgreSQL container should validate their environments for
compatibility with PostgreSQL 17 prior to upgrading. No action is required for those
using external databases.

## Upcoming end of support for PostgreSQL 16

Support for **PostgreSQL 16** will end with the **2026.10.0** release of Black Duck SCA.

Users currently using the PostgreSQL 16 container should plan to upgrade to
PostgreSQL 17 by of before that release.

External database configurations should follow standard compatibility guidance.

## PostgreSQL 18 support for external databases

Black Duck SCA now supports and recommends PostgreSQL 18 for new
installs that use external PostgreSQL.

Migrating to 2026.7.x does not require migration to PostgreSQL 18.

No action is required for users of the internal PostgreSQL container.
