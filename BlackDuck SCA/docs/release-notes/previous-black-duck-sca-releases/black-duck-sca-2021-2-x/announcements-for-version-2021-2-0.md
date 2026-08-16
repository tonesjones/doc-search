---
title: "Announcements for Version 2021.2.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements-for-version-2021.2.0.html"
content_id: "pvakxOIB6kpWhw11lbon8w"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:18.767616+00:00"
---

# Announcements for Version 2021.2.0

## Notice for Azure customers

Black Duck version 2021.2.0 is being released with a known issue which impacts
customers who deploy on Azure Kubernetes Services (AKS) and use Azure Database for
PostgreSQL as an external database. Please note, this is the standard, recommended
configuration for Black Duck customers on the Azure platform. At this time, it is
NOT recommended that customers running on the Azure platform with an external
database upgrade to 2021.2.0. Doing so will leave your system inoperable and force
you to restore your installation back to the prior state.

We expect this to be resolved in a future release of Black Duck and will make the
announcement when the release details are known.

If you are running on AKS and use an internal PostgreSQL database, there is no issue
and the system works as expected. However, this would be an atypical installation on
the AKS platform.

If you have concerns and questions, please reach out to Black Duck support for
assistance.

## Deprecation of PostgreSQL version 9.6 for external databases

Black Duck will be ending support for PostgreSQL version 9.6 for external databases
starting with the Black Duck 2021.6.0 release.

As of the Black Duck 2021.6.0 release, Black Duck will only support
PostgreSQL version 11.x for external databases.

## Internet Explorer 11 no longer supported

Black Duck has ended support for Internet Explorer 11.

## Deprecated page

The Scans > Components page is deprecated as of the 2021.2.0 release and will be
removed in a future release.

## Japanese language

The 2020.12.0 version of the UI, online help, and release notes has been localized to
Japanese.
