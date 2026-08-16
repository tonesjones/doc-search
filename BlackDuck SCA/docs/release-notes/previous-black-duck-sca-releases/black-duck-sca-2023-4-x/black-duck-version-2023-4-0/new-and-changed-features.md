---
title: "New and changed features"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features.html"
content_id: "aAIydtUYj4yWzSK82D_gwQ"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:59.300285+00:00"
---

# New and changed features

## New SBOM upload functionality

The Scans page in Black Duck has been updated to separate the possible file types
accepted when upload a report. When clicking the Upload File button, you can select
from BDIO Scan, SBOM-SPDX, and SBOM-CycloneDX.

## New BOM match score functionality

When we run signature scans, sometimes there is ambiguity in what we match. We might
match a particular component and version, but there are multiple others that could
match as well.

New in 2023.4.0, BOMs for your project versions will display a new column containing
components' *match score*. The higher the match score, the more sure we can be
that the matched component is in fact the component and version that we think.

You can configure how the match score thresholds are calculated in Admin > System
Settings > Component Match Score. By configuring your match score thresholds, you
can reduce ambiguous and low percentage matches, resulting in fewer false positives
that will be displayed in your match results. Please note that configuring the
thresholds too high might result in losing true positives in your match results.

As a result of improvements made with the new match ambiguity logic, you might see
different results when viewing your BOMs.

## New centralized Black Duck Detect hosting and version management

Black Duck now offers a new means to connect with Black Duck Detect to better
suit your needs; Black Duck Hosted. This method works best with non-airgapped
customers who want Blackduck to manage the version of Detect to use. In system
settings, Black Duck will provide a dropdown list of major Detect versions and their
latest exact versions from which you can select to perform your scans.

## New Artifactory Integration functionality

Black Duck 2023.4.0 now allows Kubernetes users using JFrog Artifactory to do both
Binary and Docker Image/Container scans on their artifacts, extending the signature
scan supported in the earlier phase. Currently, we support two deployment options:
Full on-premise and Hybrid. Please see the Kubernetes install guide for deployment
requirements and instructions.

## New scan rate limiting on all scan ingress endpoints

Based on heap memory, if the scan container uses more than 80% of the available
allocated heap (`HUB_MAX_MEMORY`), it waits until the heap usage
reaches 60% before allowing scans through again. The container will also allow one
scan through every 300 seconds per (which is the default value of
`blackduck.scan.ingress.scanPassThroughIntervalSecs`), even if
the rate limiting is enabled and active.

## New Black Duck storage container

Added in Black Duck 2023.1.0, a new storage service was introduced which enables you
to move static files, such as SBOMs and other reports, to persistent storage, which
frees up the database and enables scan performance and scalability enhancements.

NOTE: This item was accidentally left out of the Black Duck 2023.1.0 release
notes.

## New configuration of custom volumes for Blackduck Storage

Starting in 2023.4.0, the storage container may be configured to use up to three (3)
volumes for the storage of file based objects. In addition, the configuration can be
set up to migrate objects from one volume to another. The backup scripts
`hub_create_data_dump.sh` and `hub_db_migrate.sh`
have been updated to save the file provider volume accordingly.

## New filtering support for heatmaps

You can now filter the data displayed in the heatmap. Filtering options include code
location ID, code location name, project name, scan data, scan status, scan type,
and version name.

## Enhanced Rapid Scan results data for BOM support

You can now configure Rapid Scan to provide a full results format to include data
points for BOM support. To do so, set the following environment variable:
`BLACKDUCK_RAPID_SCAN_EXTENDED_DATA=true`. The new data points
include:

|  |  |  |
| --- | --- | --- |
| - componentDescription - Homepage link - OpenHub link - Declared License definition | - Release date - Meta links to component id, component version id and   component version origin URIs - External namespace - Package URL | - SPDX license ID - Source (NVD or BDSA) - Match type |

## Enhanced policy violation management

You can now set an expiration date for policy overrides on the Black Duck BOM page.
By clicking the violation icon for a component, you can enter a date until which the
policy violation is overridden. When it expires it will return to a violation
state.

## Enhanced dependency tree view

You can now highlight needed information in the Dependency Tree view in order to
copy/paste it.

## Removed CentOS download link for Detect Desktop

The Tools page has been updated to remove the CentOS download link for Detect Desktop
as it is no longer supported for Black Duck.

## Preliminary support for PostgreSQL 15

Black Duck 2023.4.0 adds preliminary support for using PostgreSQL 15 as an external
database. This support is for *testing only*; production use IS NOT
SUPPORTED.

## Supported browser versions

- Safari Version 16.3 (17614.3.7.1.7, 17614)
  - Safari versions 13.1 and below are no longer supported
- Chrome Version 111.0.5563.146 (Official Build) (x86_64)
  - Chrome versions 79 and below are no longer supported
- Firefox Version 111.0.1 (64-bit)
  - Firefox versions 74 and below are no longer supported
- Microsoft Edge Version 111.0.1661.62 (Official build) (64-bit)
  - Microsoft Edge versions 79 and below are no longer supported

## Container versions

- blackducksoftware/blackduck-postgres:13-2.22
- blackducksoftware/blackduck-authentication:2023.4.0
- blackducksoftware/blackduck-webapp:2023.4.0
- blackducksoftware/blackduck-scan:2023.4.0
- blackducksoftware/blackduck-jobrunner:2023.4.0
- blackducksoftware/blackduck-cfssl:1.0.17
- blackducksoftware/blackduck-logstash:1.0.29
- blackducksoftware/blackduck-registration:2023.4.0
- blackducksoftware/blackduck-nginx:2.0.38
- blackducksoftware/blackduck-documentation:2023.4.0
- blackducksoftware/blackduck-upload-cache:1.0.40
- blackducksoftware/blackduck-redis:2023.4.0
- blackducksoftware/blackduck-bomengine:2023.4.0
- blackducksoftware/blackduck-matchengine:2023.4.0
- blackducksoftware/blackduck-webui:2023.4.0
- blackducksoftware/blackduck-storage:2023.4.0
- blackducksoftware/bdba-worker:2023.3.0
- blackducksoftware/rabbitmq:1.2.21
