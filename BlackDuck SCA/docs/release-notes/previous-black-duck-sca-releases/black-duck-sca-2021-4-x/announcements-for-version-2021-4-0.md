---
title: "Announcements for Version 2021.4.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements-for-version-2021.4.0.html"
content_id: "zDWqbq34R5CZysmxlpUsbg"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:14.798881+00:00"
---

# Announcements for Version 2021.4.0

## New containers and changes to system requirements

In the 2021.6.0 release:

- A new container, blackduck-webui, will be added for improved Black Duck
  performance, better caching, and future scalability.

- The Rapid Scanning feature will be available to all Black Duck customers.
  This feature requires a new container, currently called blackduck-kb, which
  will manage connections to the Black Duck KnowledgeBase and cache
  KnowledgeBase results for short intervals.

The following will be the minimum hardware that will be needed to run a single
instance of all containers. Note that memory requirements depend on the number of
concurrent Rapid Scans you want to support.

- 7 CPUs
- 28.5 GB RAM for the minimum Redis configuration; 31.5 GB RAM for an optimal
  configuration providing higher availability for Redis-driven caching. This
  will support up to 100 concurrent Rapid Scans.

  30 GB RAM for the minimum Redis configuration; 33 GB RAM for an optimal
  configuration providing higher availability for Redis-driven caching. This
  will support more than 150 Rapid Scans, however, the maximum number of
  supported Rapid Scans is still being determined.
- 250 GB of free disk space for the database and other Black Duck containers
- Commensurate space for database backups

The following is the minimum hardware that is needed to run Black Duck with Black Duck Binary Analysis.

- 8 CPUs
- 32.5 GB RAM for the minimum Redis configuration; 35.5 GB RAM for an optimal
  configuration providing higher availability for Redis-driven caching. This
  will support up to 100 concurrent Rapid Scans.

  34 GB RAM for the minimum Redis configuration; 37 GB RAM for an optimal
  configuration providing higher availability for Redis-driven caching. This
  will support more than 150 Rapid Scans, however, the maximum number of
  supported Rapid Scans is still being determined.
- 350 GB of free disk space for the database and other Black Duck containers
- Commensurate space for database backups

Note: An additional CPU, 2 GB RAM, and 100 GB of free disk space will be needed for
every additional binaryscanner container.

## Retention period for unmapped code locations

(HUB-28195, 28355)In the Black Duck
2021.6.0 release, the default retention period for unmapped code locations will be
changing from 365 days to 30 days.

## Deprecated APIs

(HUB-28404)The following endpoint
has been deprecated and will be removed in a future release:

```
GET /api/scan/{scanId}/bom-entries
```

The following endpoint will be deprecated as of April 30, 2021:

```
GET /api/components/{componentId}/versions/{componentVersionId}/origins/{originId}/direct-dependencies
```

## New job implementation in 2021.6.0 release

HUB-28554In the Black Duck version
2021.6.0, the jobs subsystem is being replaced with a new implementation, which will
cause the following job Rest API calls not to function.

- ```
  GET /jobs/{jobID}
  ```

  This call gets the job details for a specific job by ID. As of the Black Duck
  2021.6.0 release, this call will return a 404 Not Found status code.

The following calls are out-of-service since Black Duck version 2020.2.0, returning a
404 Not Found status code, and will remain non-functional in Black Duck version
2021.6.0.

- ```
  PUT /jobs/{jobID}
  ```

  This call reschedules a job.
- ```
  DELETE /jobs/{jobID}
  ```

  This call terminates a job.

The functionality will be replaced with a new Job Rest API implementation which will
be available in a future release.

## Japanese language

The 2021.2.0 version of the UI, online help, and release notes has been localized to
Japanese.
