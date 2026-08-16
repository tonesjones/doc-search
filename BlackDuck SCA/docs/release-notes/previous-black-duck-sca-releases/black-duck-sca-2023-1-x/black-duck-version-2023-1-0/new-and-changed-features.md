---
title: "New and changed features"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features.html"
content_id: "FOY9YM~4B~zWMq1i0wdARQ"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:10.057313+00:00"
---

# New and changed features

## Updated SCM integration - Phase 3

Black Duck 2023.1.0 has added two new SCM providers to the list of SCM integrations:

- GitLab Self-Managed
- Bitbucket Data Center

You can now add these authorized SCM providers which can then be selected when
creating a new project. Doing so will automatically pre-populate the repository URL
and branch version in the Project Settings page for your new project.

This feature is compatible with Detect 8.x and above, and will take effect with new
package manager scans.

Please note that SCM integration is not enabled by default in Black Duck and must be
activated by adding the following in your environment:

For Swarm users, add the following to your `blackduck-config.env` file:

```
blackduck.scan.scm.enableIntegration=true
```

For Kubernetes users, add the following to your `values.yaml` file under the environs
section:

```
environs:
                blackduck.scan.scm.enableIntegration: "true"
```

## Updated project version auto-deletion

Project version auto-deletion, formely known as automatic data removal, is now
managed in the Black Duck user interface. To do so, click Admin > System Settings >
Data Retention.

## Enhanced analysis and aggregation of file sizes during signature scan processing

Overly large scans will no longer take down the match engine service, instead it will
fail the scan with an error saying the *calculated* size is greater than the
registered limit. The calculated size is either:

- The full size of the scan if it is within the registration limit.
- The last calculated size of the scan just after it exceeds the registration
  limit. Calculation of scan size will not contunue if it has already exceeded
  the licensed limit.

## Stateless signature scan (formerly Ephemeral Signature Scan)

The Stateless Scan is a new scan mode that does not create or use any permanent
storage within Black Duck, thus there is no bill of material (BOM) stored. It is
used to quickly find policy violations within the designated scan target. In order
to use Stateless Scan, you must have the following:

• Black Duck Detect 8.2.0 or later

• Black Duck 2022.10.0 or later

• Hosted KnowledgeBase

• Match as a Service must be enabled

## Added support for Docker Swarm secrets encryption

Black Duck has added support for Docker Swarm secrets encryption to centrally manage
data such as passwords, SSH private keys, SSL certificates, or other pieces of data
and securely transmit it to only those containers that need access to it.

## Added application level encryption and key rotation

Starting in version 2023.1.0, Blackduck supports encryption of critical data, such as
Git SCM OAuth tokens, Git app secret, SAML private signing keys, and LDAP
credentials, within the system. This encryption is based upon a secret provisioned
to the Blackduck installation by the orchestration environment (Docker Swarm or
Kubernetes).

## New Component Insights page

Certain components found in scans may have additional details useful in determining
extra information for a component's origin. The Component Insights page gives you
better understanding about how components are operating and what functionality is
offered. If the component has additional insights, you can view it by going to the
project version's page, and selecting Insights in the options menu for that
component.

## New SBOM report fields for project groups

You can now add new additional SBOM fields to your project groups to include more
detail to your software bill of materials (SBOM) reports:

- **Creator**: The person(s) or organization(s) that created the SPDX file
  inlcuding email addresses.
- **Creator Comments**: An optional field for creators of the SPDX file to
  provide general comments about the creation of the SPDX file or any other
  relevant comment not included in the other fields.

## New KB license update and security update jobs

The current KB Update job will be split into KB Security Update job and KB License
Update job. The KB License Update job is scheduled to run daily by default and can
be configured to change the frequency of the job, as well as to allow you to disable
the job if needed using the following system properties:

- `KB_LICENSE_UPDATER_PERIOD_MINUTES`: Sets the job frequency in
  minutes.
- `KB_UPDATE_JOB_ENABLED`: Set to false to disable both the
  security and license update jobs.

## Updated referenceLocator URLs in SBOM reports

The `referenceLocator` field in SBOM reports will now only display the
Black Duck KB unique ID instead of the URL.

## Enhanced Rapid Scan functionality

Black Duck 2021.10.0 introduced project groups defined policy rules so that customers
can scope policy rules by specific project groups which could only be used in Full
Scan mode. New in Black Duck 2023.1.0, project group based policies are now
supported in Rapid Scan mode.

Rapid Scan users can specify the scanned project's parent project group using the
following Detect parameter:

```
--detect.project.group.name=<project group name>
```

- The project group name must match exactly to an existing project group on
  Black Duck.
- If the <project group name> is provided and the project does not exist in
  Black Duck, it will be used as the project group for policy determination.

## Updated v3 signature scan failure handling

Starting in 2023.1.0, all v3 signature scans that would exceed the code location
limit or the total scanned code limit will fail on create instead of after ingress.
Failures will not be displayed in the Black Duck UI, but on the scan client instead.

## Improved performance related to searching

Searches in Black Duck use materialized views in the database that are refreshed at
regular intervals to allow for faster search results. The refresh of these views,
however, was causing problems with large databases. We analyzed all of the filters
and determined that some were not needed. From the various search categories, we
removed the following filters:

Project Version Search

- Distribution
- Tier

Component Search

- Policy Rule
- Policy Violation Severity
- Component Approval Status
- Review Status
- Vulnerability Reported
- Vulnerability CWE

Vulnerability Search

- Base Score
- Exploitability Subscore
- Impact Subscore
- Temporal Subscore
- Reachable

Saved searches will be updated via migration script to remove those filters.
Bookmarked search results will still function. However, removed filters will be
ignored, so the results will be as if the filter was never selected. Saved searches
comprised exclusively of removed filters will be removed entirely.

## New scan heatmap

You can now view an on demand heatmap which displays the total number of scans
performed on a given day and hour over the last 30 days. The color coded matrix
displays the total number of scans based on a minimum/maximum relationship, with
green values signifying lower values and red values signifying higher values. The
heatmap can be found in Black Duck by clicking the Admin button and then selecting
Heatmaps in the Diagnostics section.

## New Black Duck storage container

Black Duck 2023.1.0 introduces a new storage service which enables you to move static
files, such as SBOMs and other reports, to persistent storage, which frees up the
database and enables scan performance and scalability enhancements.

## Reporting schema change

In Black Duck 2023.1.0, the type of the `basedir` column in
`reporting.scan_view` has been changed from character varying to
text to accommodate paths longer than 255 characters.

## New Project Group Administrator role

The new Project Group Administrator role has the ability to manage project groups on
a local level. For example, they are able to create/edit/delete project groups and
add/remove members and user groups from project groups below their parent project
group.

## Supported browser versions

- Safari Version 16.2 (17614.3.7.1.7, 17614)
  - Safari versions 13.0 and below are no longer supported
- Chrome Version 109.0.5414.87 (Official Build) (x86_64)
  - Chrome versions 71 and below are no longer supported
- Firefox Version 109.0 (64-bit)
  - Firefox versions 71 and below are no longer supported
- Microsoft Edge Version 109.0.1518.55 (Official build) (64-bit)
  - Microsoft Edge versions 78 and below are no longer supported

## Container versions

- blackducksoftware/blackduck-postgres:13-2.15
- blackducksoftware/blackduck-authentication:2023.1.0
- blackducksoftware/blackduck-webapp:2023.1.0
- blackducksoftware/blackduck-scan:2023.1.0
- blackducksoftware/blackduck-jobrunner:2023.1.0
- blackducksoftware/blackduck-cfssl:1.0.15
- blackducksoftware/blackduck-logstash:1.0.26
- blackducksoftware/blackduck-registration:2023.1.0
- blackducksoftware/blackduck-nginx:2.0.31
- blackducksoftware/blackduck-documentation:2023.1.0
- blackducksoftware/blackduck-upload-cache:1.0.34
- blackducksoftware/blackduck-redis:2023.1.0
- blackducksoftware/blackduck-bomengine:2023.1.0
- blackducksoftware/blackduck-matchengine:2023.1.0
- blackducksoftware/blackduck-webui:2023.1.0
- blackducksoftware/bdba-worker:2022.12.0
- blackducksoftware/rabbitmq:1.2.15
