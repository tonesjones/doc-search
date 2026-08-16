---
title: "Announcements for Version 2020.10.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements-for-version-2020.10.0.html"
content_id: "BjRc7NjhsMQwMj5jyO_uvw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:25.666817+00:00"
---

# Announcements for Version 2020.10.0

## New containers and changes to system requirements postponed to the 2020.12.0 release

Black Duck had announced previously that there would be two additional containers:
BOM Engine and RabbitMQ (now a required container), for the 2020.10.0 release. This
requirement has been postponed to the 2020.12.0 release.

For the 2020.12.0 release, the minimum system requirements to run a single instance
of all containers will be:

- 6 CPUs
- 26 GB RAM for the minimum Redis configuration; 29 GB RAM for an optimal
  configuration providing higher availability for Redis-driven caching
- 250 GB of free disk space for the database and other Black Duck containers
- Commensurate space for database backups

For the 2020.12.0 release, the minimum hardware that is needed to run Black Duck with Black Duck Binary Analysis will be:

- 7 CPUs
- 30 GB RAM for the minimum Redis configuration; 33 GB RAM for an optimal
  configuration providing higher availability for Redis-driven caching
- 350 GB of free disk space for the database and other Black Duck containers
- Commensurate space for database backups

Note: An additional CPU, 2 GB RAM, and 100 GB of free disk space will be needed for every
additional binaryscanner container.

## Japanese language

The 2020.8.0 version of the UI, online help, and release notes has been localized to
Japanese.
