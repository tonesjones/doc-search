---
title: "Announcements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements.html"
content_id: "cVa6fCLEJIQa9gLkYSF~_w"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:09.419916+00:00"
---

# Announcements

## Increased system resource requirement for object storage service

The minimum system resource requirements to deploy the object storage service has
increased for Black Duck 2023.1.0. The object storage service will require
approximately an additional 1 cpu, 1GB of memory, and 10GB of disk space. Please
note that these requirements will change again in future releases.

## Database object ownership change

Database objects (e.g., tables, views, etc.) owned by blackduck (or the
user-specified alternate, if provided) have had their ownership changed to
blackduck_user (or the user-specified alternate, if provided).

## End of support for Helm2

Black Duck no longer supports Helm2 for Kubernetes deployments. The minimum supported
version of Kubernetes has increased to 1.13 (the oldest version supported by
Helm3).

## Documentation localization

The 2022.10.0 version of the UI, online help, and release notes have been localized
to Japanese and Simplified Chinese.
