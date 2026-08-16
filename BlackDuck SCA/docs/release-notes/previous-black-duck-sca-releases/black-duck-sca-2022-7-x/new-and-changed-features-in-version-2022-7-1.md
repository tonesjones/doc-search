---
title: "New and changed features in version 2022.7.1"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features-in-version-2022.7.1.html"
content_id: "fQkQUAnmH~Bpagkv582TNg"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:30.262140+00:00"
---

# New and changed features in version 2022.7.1

## Git repository SCM integration - Phase 2

Black Duck 2022.7.1 has updated the way users can add repository/branch fields when
creating a project and version. You now have the ability to add authorized SCM
providers (GitHub Standard and GitHub Enterprise only at this time) which can then
be selected when creating a new project. Doing so will automatically pre-populate
the repository URL and branch version in the Project Settings page for your new
project.

This feature is compatible with Detect 8.x and above, and will take effect with new
scans.

Please note that SCM integration is not enabled by default in Black Duck and must be
activated by adding the following in your environment:

For Swarm users, add the following to your `blackduck-config.env`
file:

```
blackduck.scan.scm.enableIntegration=true
```

For Kubernetes users, add the following to your `values.yaml` file
under the `environs` section:

```
environs:
  blackduck.scan.scm.enableIntegration: "true"
```

## New heatmap data download

You now have the ability to download the heatmap data which holds information for
terminal scans in the system. You can download this information by going to Administration > Diagnostics > System Information. From there, click the **Download Heatmap (.zip)** button. The
output is a `.csv` file.

## Creating reports using UTF8 with BOM

*Please note that this feature was added in Black Duck 2022.7.0 and was
accidentally omited from that version's release notes.*

Black Duck 2022.7.0 introduced support for UTF8 with BOM character encoding in
reports for customers using non-Western characters. To enable this feature, add the
following to the `blackduck-config.env` file:

```
USE_CSV_BOM=true
```

## New bulk actions for project version components

The bulk update feature now supports the following actions on components on the
project versions page:

- Ignore/unignore components
- Set component usage type
- Set include/exclude in notices file

## Container versions

- blackducksoftware/blackduck-postgres:11-2.16
- blackducksoftware/blackduck-authentication:2022.7.1
- blackducksoftware/blackduck-webapp:2022.7.1
- blackducksoftware/blackduck-scan:2022.7.1
- blackducksoftware/blackduck-jobrunner:2022.7.1
- blackducksoftware/blackduck-cfssl:1.0.9
- blackducksoftware/blackduck-logstash:1.0.20
- blackducksoftware/blackduck-registration:2022.7.1
- blackducksoftware/blackduck-nginx:2.0.27
- blackducksoftware/blackduck-documentation:2022.7.1
- blackducksoftware/blackduck-upload-cache:1.0.28
- blackducksoftware/blackduck-redis:2022.7.1
- blackducksoftware/blackduck-bomengine:2022.7.1
- blackducksoftware/blackduck-matchengine:2022.7.1
- blackducksoftware/blackduck-webui:2022.7.1
- blackducksoftware/bdba-worker:2022.6.0
- blackducksoftware/rabbitmq:1.2.13
