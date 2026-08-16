---
title: "New and changed features"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features.html"
content_id: "IuacOjZB7_4EvnIEjAUkXQ"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:23.673584+00:00"
---

# New and changed features

## New Black Duck Automated Security Advisories (ASA)

Automated Security Advisories (ASA) are automatically created by Black Duck's Cyber
Security Research Center using automated AI tools. ASAs are created from various
trusted security feeds such as the GitHub Security Advisories (GHSA) feeds along
with automated vetting using AI tooling. These advisories are designed to supplement
the BDSAs identified and verified by our [Cyber Security Research Center](https://www.blackduck.com/resources/cybersecurity-research-center.html).

You will find ASA-tagged BDSAs in all areas where other vulnerability tags are
found.

## New Download Location value for a BOM Component

A new Download Location SBOM field has been added to the list of Additional Fields.
The Download Location is found under the BOM Component section and is configurable,
allowing you to add the URL or other specific location within a version control
system (VCS) where the component was downloaded. This new information is displayed
in the SBOM report as:

- SPDX: Under the `packages` > *`package
  ID`* section as `downloadLocation`.
- CycloneDX: Under the `components` >
  `externalReferences` section as `url`.

## New copyright text, license comment, and homepage data for SBOM reports

The available SBOM report options under project group settings were updated to
support inclusion of copyright data, license comments, and homepage URL to the SBOM
reports. Copyright text, license comments, and homepage URLs are included in both
CycloneDX and SPDX reports if the group setting is enabled.

## New SCM repository auto-scanning

SCM repository auto-scanning allows Black Duck to check daily for any changes such as
commits, pushes, or merges in the repository branch mapped to your SCM projects and
perform scans if changes were made. To take advantage of this feature, you must
enable it through to Admin → Jobs → Scheduled.

In addition, two new SCM repository auto-scanning jobs have been added to Black Duck
to support this feature:

- SCM Onboarding daily auto scanning: Schedules nightly job that performs auto
  scanning of previously onboarded SCM repositories.
- SCM Onboarding daily cleanup: Schedules nightly job that cleans up from SCM
  Onboarding.

## Added CISA Known Exploited Vulnerability tag

Vulnerabilities listed in the CISA Known Exploited Vulnerability Catalog are now
tagged as such in Black Duck. This allows you to add CISA Known Exploited
Vulnerabilities as a Vulnerability Conditions policy filter. Please visit [CISA's Known Exploited Vulnerability
Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) page for more information.

## Updated SCM integration

Black Duck 2024.1.0 has added two new SCM providers to the list of SCM integrations:

- GitLab SaaS
- Bitbucket

You can now add these authorized SCM providers which can then be selected when
creating a new project. Doing so will automatically pre-populate the repository URL
and branch version in the Project Settings page for your new project.

This feature is compatible with Detect 8.x and above, and will take effect with new
package manager scans.

Please note that SCM integration is not enabled by default in Black Duck and must be
activated by adding the following in your environment:

For Swarm users, add the following to your `blackduck-config.env`
file:

```
blackduck.scan.scm.enableIntegration=true
```

For Kubernetes users, add the following to your `values.yaml` file
under the environs section:

```
environs:
                blackduck.scan.scm.enableIntegration: "true"
```

## Updated SBOM report relationship information

SBOM reports were updated to add dependency information. SPDX reports the
dependencies now include the dependency type in the `relationships`
section. Note that this applies only to SPDX 2.3 reports. CycloneDX reports do not
include dependency types.

## Updated deep license data management for snippet component matches

Customers leveraging Deep License Data (DLD) and snippet matching together can now
configure their projects to see deep license risk appearing for files present in the
components found in their code.

The feature has been broken up into two separate functions:

- **Apply Deep License Data to Bill of Materials**: Enabling this checkbox
  will apply deep license data to your non-snippet components and allow
  visibility to embedded licenses which may exist in your components beyond
  declared licenses.
- **Apply Deep License Data to Snippet Component Matches**: If enabled,
  component snippet matches are included in the deep license data
  calculation.

## Enhanced license conflict management for project hierarchies

Previously, license conflicts were calculated only from a single project license and
did not factor in project hierarchies. With Black Duck 2024.1.0, subprojects within
the parent project will now also factor in the calculation.

Hierarchical licence conflicts are enabled by default with Black Duck 2024.1.0 but
can be configured in your environment. However, license conflict information is not
automatically enabled. System Administrators must enable the Legal and License
Conflicts tab to view license conflicts. Use the project's Settings tabs to enable
the feature for current projects.

## Enhanced component vulnerability history graph

The Vulnerability History graph displayed on a component's page now includes data for
vulnerabilities of unknown origin.

## Enhanced Kubernetes probes for SCA

Improvements have been made to the readiness probes used in Kubernetes
environments:

- A new startupProbe has been added to verify whether the application within a
  container is started. The startupProbe runs before any other probe, and,
  unless it finishes successfully, disables other probes.
- The readinessProbe now starts checking after a 30 second initial delay (from
  240 seconds) and checks every 10 seconds (from 30 seconds). It also allows
  for 15 failures before a restart is issued.
- The livenessProbes now checks every 10 seconds (from 30 seconds).
- New toggles for startupProbe and readinessProbes have been added. A unique
  flag has been added to control each probe.

## Enhanced on-demand job retries

On-demand jobs previously attempted to retry three times before finally failing
which, in some cases, could lead to situations where a job that is known to fail
would continue to re-run and consume system resources. We have refined this approach
by disabling retries by default so that jobs kicked off by the periodic scheduler
retry when the corresponding check job runs again.

Please note that this change does not affect report jobs. Report jobs will retry as
normal.

## Change to the upload cache for source code upload

NOTE: This change was part of Black Duck 2023.10.0 and was not clearly communicated
at the time.

In Black Duck 2023.4.2, a workaround was added for users running on AWS to deal with
an issue where uploading source files and using the license search feature was not
working due to file system latency and spawning of multiple du processes.

This issue was resolved in Black Duck 2023.10.0 with an architectural change to how
Black Duck uses the upload cache and storage service. The upload cache is no longer
used for the source code upload functionality in Black Duck therefore the root cause
problem was eliminated with the new architectural model of the source code upload
via the storage service.

## New Detect GUI release

Detect GUI has been updated to version 2024.1.0 which includes Black Duck Detect (CLI)
9.1.0.

## Supported browser versions

- Safari Version 17.1.2
  - Safari versions 14 and below are no longer supported
- Chrome Version 120.0.6099.216 (Official Build) (x86_64)
  - Chrome versions 91 and below are no longer supported
- Firefox Version 121.0.1 (64-bit)
  - Firefox versions 89 and below are no longer supported
- Microsoft Edge Version 120.0.2210.121 (Official build) (64-bit)
  - Microsoft Edge versions 91 and below are no longer supported

## Container versions

- blackducksoftware/blackduck-postgres:14-1.20
- blackducksoftware/blackduck-postgres-upgrader:14-1.3
- blackducksoftware/blackduck-postgres-waiter:1.0.11
- blackducksoftware/blackduck-cfssl:1.0.25
- blackducksoftware/blackduck-nginx:2.0.66
- blackducksoftware/blackduck-logstash:1.0.35
- blackducksoftware/bdba-worker:2023.12.1
- blackducksoftware/rabbitmq:1.2.36
- blackducksoftware/blackduck-webui:2024.1.0
- blackducksoftware/blackduck-authentication:2024.1.0
- blackducksoftware/blackduck-bomengine:2024.1.0
- blackducksoftware/blackduck-documentation:2024.1.0
- blackducksoftware/blackduck-integration:2024.1.0
- blackducksoftware/blackduck-jobrunner:2024.1.0
- blackducksoftware/blackduck-matchengine:2024.1.0
- blackducksoftware/blackduck-redis:2024.1.0
- blackducksoftware/blackduck-registration:2024.1.0
- blackducksoftware/blackduck-scan:2024.1.0
- blackducksoftware/blackduck-storage:2024.1.0
- blackducksoftware/blackduck-webapp:2024.1.0
