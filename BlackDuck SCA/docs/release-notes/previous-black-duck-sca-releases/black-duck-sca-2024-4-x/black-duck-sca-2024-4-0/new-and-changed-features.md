---
title: "New and changed features"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features.html"
content_id: "Bf96TVKL4HxbSFIuAJg1GA"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:16.335473+00:00"
---

# New and changed features

## Preliminary support for PostgreSQL 16

Black Duck 2024.4.0 adds preliminary support for using PostgreSQL 16 as an external
database. This support is for *testing only*; production use IS NOT
SUPPORTED.

## New malware scans

scans allow you to get access to enhanced malware and
threat intel data via our  partnership. Using complex
binary analysis powered by , developers and DevOps teams can analyze
first party, open source, and commercial software to identify the presence of
threats such as malware, maldocs, suspicious files, potentially unwanted
applications (PUAs), protestware, and suspicious file structure malformations to
help avoid dangerous software supply chain attacks.

## New Unmatched component auto-creation

In an SBOM management workflow, the SBOM is the input and all of the components
included in the SBOM need to be persisted in the SBOM management solution so that
visibility isn't lost, regardless if there is a match to the KnowledgeBase. This
feature provides the option to automatically create unmatched components in the BOM
with custom components of the same name in an SBOM import as long as the component
has an associated PURL in the SBOM.

In addition, you also have the ability to configure the default license applied to
auto-created components where the SBOM license tag value is NOASSERTION.

## New SBOM templates

SBOM Templates is a new feature that effectively replaces and enhances the ability to
determine what is included in an SBOM report. The SBOM Template allows users to
select which of those fields they want to include in the generated SBOM as well as
some other configuration items like whether to include vulnerability info (for
CycloneDX) or Dev/Build tools. SBOM templates can then be selected when creating
SBOM reports to generate desired outputs.

Please note, some SBOM field configurations were moved from project group settings to
the SBOM template configuration. Customers are encouraged to review and configure
SBOM templates after upgrading to Black Duck 2024.4.0 before
generating new SBOM reports.

## Added new CLI command line option for project groups

You can now add the `--project-group` option to the Signature Scan
command line which sets the 'Project Group' to assign the project to. If the project
doesn't already exist, a new project will be created in the corresponding project
group.

This parameter has no effect if the project already exists or if the specified
project group does not exist.

## Added support for CycloneDX 1.5

You can now export the Software Bill of Materials report for your projects in
CycloneDX v1.5 format. This can be done by viewing a project version, clicking the
Reports tab, clicking the Create Report button, and then selecting CycloneDX v1.5 -
JSON. For more information on CycloneDX v1.5, please visit the [CycloneDX v1.5 reference page](https://cyclonedx.org/docs/1.5/json/).

## Enhanced missing container scan registration error handling

Container scans will now fail with an appropriate message if your Black Duck
registration key does not have Container Scanning enabled.

## Enhanced SBOM import error handling

SBOM import error handling has been improved to provide better visibility as to why
an SBOM import may have failed, including specific lines/fields that failed the
validation. In addition, you can export the failure to a log file so that it can be
researched outside of the Black Duck UI and re-import attempted
after the necessary updates have been made to the SBOM.

## Updated method of setting HUB_MAX_MEMORY

Starting with Black Duck 2024.4.0, the configuration parameter
`HUB_MAX_MEMORY` is automatically set for relevant containers in
Kubernetes-based deployments. The value is computed as a percentage of the memory
limit, with 90% being the default. In the gen04 deployment sizings, the
`hubMaxMemory` setting has been replaced with
`maxRamPercentage` to control the percentage used; the values for
this setting were chosen so that `HUB_MAX_MEMORY` has the same values
as before.

This change does not apply to Swarm-based deployments.

## Updated match score confidence for components imported via SBOM

When viewing a project version's BOM where components were imported from a SBOM file,
the match score displayed will always be 100% and the match type will indicate SBOM
as the origin.

## Updated binary match type results with BDBA package manager support

Previously, all container and binary scans produced a single binary match type. With
the expanded package manager support from BDBA, we can now identify additional match
types based on the BDBA matching method. As a result, you will see changes in your
BOM, with components identified through binary and container scanning gaining or
changing their match types.

## Removal of the blackduck-webui container

The blackduck-webui container has been removed and its builds are now included in the
blackduck-nginx container. The blackduck-nginx container will now follow the same
release cadence as the rest of the blackduck stack.

## Supported browser versions

- Safari Version 17.4.1

  - Safari versions 14 and below are no longer supported
- Chrome Version 123.0.6312.124 (Official Build) (x86_64)

  - Chrome versions 91 and below are no longer supported
- Firefox Version 124.0.2 (64-bit)

  - Firefox versions 89 and below are no longer supported
- Microsoft Edge Version 123.0.2420.97 (Official build) (64-bit)

  - Microsoft Edge versions 91 and below are no longer supported

## Container versions

- blackducksoftware/blackduck-postgres:14-1.22
- blackducksoftware/blackduck-postgres-upgrader:14-1.4
- blackducksoftware/blackduck-postgres-waiter:1.0.12
- blackducksoftware/blackduck-cfssl:1.0.26
- blackducksoftware/blackduck-nginx:2024.4.0-RC
- blackducksoftware/blackduck-logstash:1.0.36
- blackducksoftware/bdba-worker:2024.3.0
- blackducksoftware/rabbitmq:1.2.37
- blackducksoftware/blackduck-authentication:2024.4.0
- blackducksoftware/blackduck-bomengine:2024.4.0
- blackducksoftware/blackduck-documentation:2024.4.0
- blackducksoftware/blackduck-integration:2024.4.0
- blackducksoftware/blackduck-jobrunner:2024.4.0
- blackducksoftware/blackduck-matchengine:2024.4.0
- blackducksoftware/blackduck-redis:2024.4.0
- blackducksoftware/blackduck-registration:2024.4.0
- blackducksoftware/blackduck-scan:2024.4.0
- blackducksoftware/blackduck-storage:2024.4.0
- blackducksoftware/blackduck-webapp:2024.4.0
