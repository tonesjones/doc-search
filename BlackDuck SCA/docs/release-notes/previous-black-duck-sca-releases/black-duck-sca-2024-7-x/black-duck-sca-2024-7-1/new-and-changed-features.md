---
title: "New and changed features"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features.html"
content_id: "FajcrzZgTHACGkLkerDvLw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:04.918050+00:00"
---

# New and changed features

## Updated Component Origin Copyright Dialog

Currently, we show the `kbCopyright` text in the Component Origin
Copyright dialog box, but only if the copyright was modified. With this update, we
now always show the full copyright text in a second text block below the existing
block with the label “Full Copyright Text” for reference. This information is not
editable.

## Enhanced dashboard with LTS version indicator

The dashboard has been enhanced to include an indicator for projects that have a
Long-Term Support (LTS) version. Users can now more easily identify which projects
have LTS project versions directly from the dashboard, improving visibility and
management for long-term support projects.

## Enhanced BOM Components tab with External IDs

The BOM Components tab will now utilize the new `inputExternalIds`
field to provide more useful information for BINARY and CONTAINER matches. The
current message has been updated and will be displayed when the following conditions
are present on the component:

- `matchTypes` includes BINARY.
- `componentVersion` is missing in the response for the
  component.
- `origins` is empty in the response for the component.

The current message with the update is as follows (updated section in italics):

> **Unknown Version**
>
> This component has an unknown version. The license risks are estimated. For a
> more accurate result, manually specify a version for the component.
>
> *This identifier was found during binary scanning:*
>
> *<Data>*
>
> OR
>
> *These identifiers were found during binary scanning:*
>
> *<Data>*
>
> *<Data>*

For users utilizing the APIs, the `inputExternalIds` field is always
available for supported scans. While not present in all scan types, they will appear
for all BOM items in scans that utilize this feature.

## Container versions

- blackducksoftware/blackduck-postgres:14-1.25
- blackducksoftware/blackduck-postgres-upgrader:14-1.4
- blackducksoftware/blackduck-postgres-waiter:1.0.13
- blackducksoftware/blackduck-cfssl:1.0.28
- blackducksoftware/blackduck-nginx:2024.7.1
- blackducksoftware/blackduck-logstash:1.0.38
- blackducksoftware/bdba-worker:2024.6.3
- blackducksoftware/rabbitmq:1.2.40
- blackducksoftware/blackduck-authentication:2024.7.1
- blackducksoftware/blackduck-bomengine:2024.7.1
- blackducksoftware/blackduck-documentation:2024.7.1
- blackducksoftware/blackduck-integration:2024.7.1
- blackducksoftware/blackduck-jobrunner:2024.7.1
- blackducksoftware/blackduck-matchengine:2024.7.1
- blackducksoftware/blackduck-redis:2024.7.1
- blackducksoftware/blackduck-registration:2024.7.1
- blackducksoftware/blackduck-scan:2024.7.1
- blackducksoftware/blackduck-storage:2024.7.1
- blackducksoftware/blackduck-webapp:2024.7.1
