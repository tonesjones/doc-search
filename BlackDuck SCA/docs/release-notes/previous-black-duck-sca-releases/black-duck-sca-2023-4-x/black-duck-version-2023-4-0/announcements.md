---
title: "Announcements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements.html"
content_id: "cCZhMS_2DxO0hOkaWwlTnA"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:58.664019+00:00"
---

# Announcements

## Upgrading to 2023.4.0 for Azure PostgreSQL users

If you are upgrading or installing using Azure PostgreSQL, a database administrator
will need to enable installation of the `hstore` PostgreSQL extension
before installing or upgrading to 2023.4.0 or later.

## Moved pgcrypto extension into the st schema

Starting with Black Duck 2023.4.0, the pgcypto PostgreSQL extension is moved from the
public schema into the `st` schema. If you are upgrading, using an
external PostgreSQL instance, *and* the `blackduck` database
user is not a superuser, you will need to relocate the extension manually with:

```
alter extension pgcrypto set schema st ;
```

In all other cases, the move is performed automatically.

## Removed MAX_CONCURRENT_JOBS from use in jobrunner

MAX_CONCURRENT_JOBS was deprecated in Black Duck 2022.10.x and has been removed in
this release. Please refer to the Swarm and Kubernetes installation guides for
assistance with configuring the newer mechanisms.

## Deprecation of KBMATCH_SENDPATH in MaaS enabled systems

Match as a Service (MaaS) is now generally available with Black Duck 2023.4.0 and is
enabled by default for new customers and will become standard for all existing
customers. As a result of this update, the option to disable sending file path
metadata to the KnowledgeBase for matching, `KBMATCH_SENDPATH`, is
being removed in an upcoming Black Duck release.

Customers wanting to continue using this option will need to contact Black Duck
support to have MaaS disabled for their Black Duck registration keys.

## Upcoming end of support for Docker 18.09.x and 19.03.x

Starting with the 2023.7.0 release, Black Duck will no longer support Docker 18.09.x
and 19.03.x. Docker 20.10.x will be the only version supported.

## Upcoming end of life for Black Duckctl

Starting with the 2023.7.0 release, Black Duckctl will no longer be supported and there
will be no more updates. Documentation for Black Duckctl can be found at <https://github.com/blackducksoftware/hub/tree/master/kubernetes/blackduck>.

## Upcoming container scanning hardware requirements

With Black Duck 2023.10.0, the BDBA container will be required to perform container
scanning. This means customers who currently perform container scans in Black Duck
but do not have BDBA deployed with their Black Duck instance will need to allocate
additional hardware resources per our guidance for the 2023.10.0 release to make use
of the new container scanning functionality.

Existing functionality with container scanning will not be removed as part of this
change.

## Documentation localization

The 2023.1.0 version of the UI, online help, and release notes have been localized
to Japanese and Simplified Chinese.
