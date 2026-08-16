---
title: "Announcements for Version 2020.12.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements-for-version-2020.12.0.html"
content_id: "Tn9kvYQX2FrRvDII6XzTrQ"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:21.652628+00:00"
---

# Announcements for Version 2020.12.0

## New containers and changes to system requirements

There are two additional containers: BOM Engine and RabbitMQ (now a required
container) for the 2020.12.0 release.

The minimum system requirements to run a single instance of all containers
are:

- 6 CPUs
- 26 GB RAM for the minimum Redis configuration; 29 GB RAM for an optimal
  configuration providing higher availability for Redis-driven caching
- 250 GB of free disk space for the database and other Black Duck containers
- Commensurate space for database backups

The minimum hardware that is needed to run Black Duck with Black Duck Binary Analysis are:

- 7 CPUs
- 30 GB RAM for the minimum Redis configuration; 33 GB RAM for an optimal
  configuration providing higher availability for Redis-driven caching
- 350 GB of free disk space for the database and other Black Duck containers
- Commensurate space for database backups

Note: An additional CPU, 2 GB RAM, and 100 GB of free disk space will be needed for every
additional binaryscanner container.

## Ending support for Internet Explorer 11

Support for Internet Explorer 11 is deprecated and Black Duck will be ending
support for Internet Explorer 11 starting with the Black Duck
2021.2.0 release.

## Japanese language

The 2020.10.0 version of the UI, online help, and release notes has been
localized to Japanese.
