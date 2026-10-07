---
title: "Announcements for Version 2020.12.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements-for-version-2020.12.0.html"
content_id: "Lu9SitUekldUa3ZvPeJylA"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:36.124726+00:00"
content_hash: "b698f4979b3cef519b46b269c41e69b6fad288b38876b4300beb18a2bc3ddbee"
---

# Announcements for Version 2020.12.0

## New containers and changes to system requirements

There are two additional containers: BOM Engine and RabbitMQ (now a required container) for the 2020.12.0 release.

The minimum system requirements to run a single instance of all containers are:

- 6 CPUs
- 26 GB RAM for the minimum Redis configuration; 29 GB RAM for an optimal configuration providing higher availability for Redis-driven caching
- 250 GB of free disk space for the database and other Black Duck containers
- Commensurate space for database backups

The minimum hardware that is needed to run Black Duck with Black Duck Binary Analysis are:

- 7 CPUs
- 30 GB RAM for the minimum Redis configuration; 33 GB RAM for an optimal configuration providing higher availability for Redis-driven caching
- 350 GB of free disk space for the database and other Black Duck containers
- Commensurate space for database backups

Note: An additional CPU, 2 GB RAM, and 100 GB of free disk space will be needed for every additional binaryscanner container.

## Ending support for Internet Explorer 11

Support for Internet Explorer 11 is deprecated and Black Duck will be ending support for Internet Explorer 11 starting with the Black Duck 2021.2.0 release.

## Japanese language

The 2020.10.0 version of the UI, online help, and release notes has been localized to Japanese.
