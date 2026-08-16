---
title: "New and Changed Features"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features.html"
content_id: "g60sZ9BbAS~4oEBOm9BuTw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:34:55.582678+00:00"
---

# New and Changed Features

## Registration page buttons disabled for airgapped installations

The **Refresh** and **Reset** buttons on the Product Registration page are now
disabled for air-gapped (offline) deployments of Black Duck SCA
when the air-gapped environment variable is enabled in the orchestration
configuration. Previously, using these buttons in an air-gapped environment could
leave the registration in an unrecoverable state, as the activation request cannot
reach the external registration server. These buttons are now automatically hidden
when the air-gapped flag is present, preventing potential registration issues.

## Include Subproject Vulnerabilities in VEX Reports

VEX CSAF 2.0 reports now support the inclusion of vulnerability data from
sub-projects. A new **Include Subproject Vulnerabilities** checkbox is available
in the report creation dialog when generating a VEX report from either the global
Reports page or a specific project version. When enabled, Black Duck SCA recursively discovers all sub-projects within the
selected project's hierarchy and merges their vulnerability data into the
report.

## Container versions

- blackducksoftware/blackduck-postgres:16-2.8
- blackducksoftware/blackduck-postgres-upgrader:16-1.4
- blackducksoftware/blackduck-postgres-waiter:1.0.20
- blackducksoftware/blackduck-cfssl:1.0.37
- blackducksoftware/blackduck-nginx:2026.4.1
- blackducksoftware/blackduck-logstash:1.0.45
- blackducksoftware/bdba-worker:2026.3.1
- blackducksoftware/rabbitmq:1.2.49
- blackducksoftware/blackduck-authentication:2026.4.1
- blackducksoftware/blackduck-bomengine:2026.4.1
- blackducksoftware/blackduck-documentation:2026.4.1
- blackducksoftware/blackduck-integration:2026.4.1
- blackducksoftware/blackduck-jobrunner:2026.4.1
- blackducksoftware/blackduck-redis:2026.4.1
- blackducksoftware/blackduck-registration:2026.4.1
- blackducksoftware/blackduck-scanmatch:2026.4.1
- blackducksoftware/blackduck-storage:2026.4.1
- blackducksoftware/blackduck-webapp:2026.4.1
