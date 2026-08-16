---
title: "Other platform properties for tuning-write"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/other-platform-properties-for-tuning-write.html"
content_id: "CWpMtV6lBswDTniaTWOREw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:20.648807+00:00"
---

# Other platform properties for tuning-write

If the PostgreSQL database is on-prem, on another physical or virtual machine, or on an
internal cloud, and if you are performing a tuning-write, set
`<POSTGRES-DISTRO>`, authentication, and authorization as
follows.

## POSTGRES-DISTRO

In the tuning yaml file, set `<POSTGRES-DISTRO>` to
`'other'`.

## Authentication

Not applicable.

## Authorization for tuning-write

For a tuning-write to continue, in `cim.properties`, the database user
must be a superuser.

Note: This authorization is not required with
tuning-suggest.
