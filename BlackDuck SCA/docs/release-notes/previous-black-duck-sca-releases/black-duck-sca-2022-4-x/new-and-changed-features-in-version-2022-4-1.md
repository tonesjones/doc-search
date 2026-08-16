---
title: "New and Changed Features in Version 2022.4.1"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features-in-version-2022.4.1.html"
content_id: "_5YkDOoIg8rPvYadNKLsJw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:37.154589+00:00"
---

# New and Changed Features in Version 2022.4.1

## New BDSA Auto Remediation setting to automatically ignore CVEs with related unmatched BDSA records

Activating this setting will automatically remediate new CVE vulnerabilities with
related unmapped BDSAs by setting the remediation status to IGNORED and adding a
message to describe why the vulnerability was remediated.

This new setting only applies to CVE vulnerabilities with a related BDSA
vulnerability. If the CVE is mapped to a component version, but its related BDSA
is not also mapped to that component version then the system may automatically
remediate the CVE vulnerability based on the system setting.

The BDSA Auto Remediation feature can be enabled from the Admin > System Settings
> BDSA Auto Remediation page.

## New Rapid Scan properties added

The following properties have been added to the output of Rapid Scans:

- `cweIds`: List of Common Weakness Enumeration (CWE) IDs
  for this security vulnerability.
- `shortTermUpgradeGuidance`: Suggested component version to
  upgrade to as a short term course of action to address this
  vulnerability as it is the same major version as the one in use.
- `longTermUpgradeGuidance`: Suggested component version to
  upgrade to as a long term course of action. Taking this course of action
  might require major version number upgrade and must be more carefully
  planned.

## Improved user permission evaluations performance

Improvements were made to user permission evaluations for most API requests. This
should result in more consistent loading times including loading BOMs regardless
of the user's role or permissions.

## Updated Black Duckctl

Black Duckctl has been updated to 3.0.1 to add Black Duck 2022.4.0 installation
support for sizes-gen03 deployment sizes.

## Container versions

- blackducksoftware/blackduck-postgres:11-2.11
- blackducksoftware/blackduck-authentication:2022.4.1
- blackducksoftware/blackduck-webapp:2022.4.1
- blackducksoftware/blackduck-scan:2022.4.1
- blackducksoftware/blackduck-jobrunner:2022.4.1
- blackducksoftware/blackduck-cfssl:1.0.7
- blackducksoftware/blackduck-logstash:1.0.18
- blackducksoftware/blackduck-registration:2022.4.1
- blackducksoftware/blackduck-nginx:2.0.16
- blackducksoftware/blackduck-documentation:2022.4.1
- blackducksoftware/blackduck-upload-cache:1.0.23
- blackducksoftware/blackduck-redis:2022.4.1
- blackducksoftware/blackduck-bomengine:2022.4.1
- blackducksoftware/blackduck-matchengine:2022.4.1
- blackducksoftware/blackduck-webui:2022.4.1
- blackducksoftware/bdba-worker:2022.3.0
- blackducksoftware/rabbitmq:1.2.7
