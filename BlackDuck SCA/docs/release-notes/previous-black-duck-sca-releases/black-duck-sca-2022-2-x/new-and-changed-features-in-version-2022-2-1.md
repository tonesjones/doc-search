---
title: "New and Changed Features in Version 2022.2.1"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features-in-version-2022.2.1.html"
content_id: "onzUzXu_27nKXtLPJHto5w"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:43.506544+00:00"
---

# New and Changed Features in Version 2022.2.1

## Updated Data Removal feature (Beta)

The data removal feature allows you to explore ways to automatically delete
ProjectVersions according defined criteria. For users with version limits, disk
space constraints or database bottlenecks, the buildup of obsolete versions can
become problematic to either their process or to their system performance. This
feature is helpful if you generate multiple ProjectVersions over time which become
obsolete over time.

Added in Black Duck 2022.2.0, a new environment variable has been added:

- ```
  BLACKDUCK_AUTOMATIC_VERSION_REMOVAL_RELEASE_PHASES
  ```

  - Defines what ProjectVersion phases are applicable to the data removal
    process.
  - Release phases values are: Planning, Development, Released,
    Deprecated, Archived, and Prerelease
  - If not set, the default value is Development.
  - Values are case insensitive.
  - Multiple release phases can be added with the phases delimited by
    comma.

## Updated role assignment for Projects and Project Groups

You can now add users to Projects and Project Groups as a Project Viewer. When adding
a user to a Project or Project Group, the role of Project Viewer is now
automatically selected and serves as the default role. You can then add further
roles to the user as needed.

## Updated minimum scan interval configuration

Starting from Detect 7.13 and later, the Black Duck Hub scan setting for Minimum Scan
Interval will be disabled. Minimum scan interval should be configured as a command
argument through Detect as follows:

```
--detect.blackduck.signature.scanner.arguments='--min-scan-interval=##'
```

where `##` is the time in hours.

## Container versions

- blackducksoftware/blackduck-postgres:11-2.8
- blackducksoftware/blackduck-authentication:2022.2.1
- blackducksoftware/blackduck-webapp:2022.2.1
- blackducksoftware/blackduck-scan:2022.2.1
- blackducksoftware/blackduck-jobrunner:2022.2.1
- blackducksoftware/blackduck-cfssl:1.0.6
- blackducksoftware/blackduck-logstash:1.0.16
- blackducksoftware/blackduck-registration:2022.2.1
- blackducksoftware/blackduck-nginx:2.0.12
- blackducksoftware/blackduck-documentation:2022.2.1
- blackducksoftware/blackduck-upload-cache:1.0.21
- blackducksoftware/blackduck-redis:2022.2.1
- blackducksoftware/blackduck-bomengine:2022.2.1
- blackducksoftware/blackduck-matchengine:2022.2.1
- blackducksoftware/blackduck-webui:2022.2.1
- blackducksoftware/bdba-worker:2021.12.2
- blackducksoftware/rabbitmq:1.2.7
