---
title: "New and Changed Features in Version 2022.4.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features-in-version-2022.4.0.html"
content_id: "xoSM5LRfz9XMf1BPyH75xA"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:39.589354+00:00"
---

# New and Changed Features in Version 2022.4.0

## Spring Framework Update

Spring Framework has been updated to 5.3.18 to address the critical CVE-2022-22965
vulnerability.

## New vulnerability metrics comparison

This new feature makes a change to a vulnerability's Overview page so that you can
now see a side-by-side view of the metrics where applicable. When viewing a
vulnerability that has both a BDSA and NVD record, you will see a graph in the
Scores and Metrics section comparing both vulnerability types; BDSA and NVD. You can
also alternate between CVSS v2 and CVSS v3.x to get more information.

## Git repository SCM Integration - Phase 1

Black Duck 2022.4.0 is introducing a way to simplify onboarding of new projects for
customers by leveraging integrations for management of repositories, branches,
builds, and releases. Starting with Phase 1, we are adding a new SCM URL field to
the Create Project modal and Project Settings page, and a SCM Branch field to the
Project Version Settings page.

These fields are manually populated in this phase. However, in an upcoming Detect
release, they will be automatically populated after scanning a git repository.
Detect will automatically identify the associated git repository URL and branch and
then send that information to Black Duck.

Please note that this feature is not enabled by default in Black Duck and must be
activated by adding the following in your environment:

For Swarm users, add this to your `docker-compose.yml` webapp
environment:

```
webapp:
    environment: {blackduck.scan.scm.enableIntegration: true}
```

For Kubernetes users, add this to your webapp container environment:

```
containers:
- env:
  - name: blackduck.scan.scm.enableIntegration
    value: true
```

## New Components tab for BDSA vulnerabilities

A new Components tab has been added to BDSA vulnerability records. This tab will
allow you to see all known component versions affected by a particular BDSA
vulnerability.

## Enhanced Component dashboard materialized view query

All the queries relating to the SearchDashboardRefreshJob have been optimized for
better performance. The LicenseDashboardRefreshJob is longer available and the view
relating to it will be refreshed under SearchDashboardRefreshJob. This means the
counts displayed in the License Management page will now be updated as
SearchDashboardRefreshJob finishes.

**NOTE:** As a result of these changes, upgrading to Black Duck 2022.4.0 may take
longer than usual due to the execution of migration scripts.

## PostgreSQL 11 container migration

In Kubernetes and OpenShift deployments using the Black Duck-provided PostgreSQL
container, the following persistent volume claim added in 2022.2.0 is no longer
needed. It and its associated persistent volume may be safely deleted.

```
{{ .Release.Name }}-blackduck-postgres-tmp
```

## Updated Java heap size allocation and new environment variable

In previous releases, Java was allowed to slowly increase its heap size up to
`HUB_MAX_MEMORY`. Starting with Black Duck 2022.4.0, in order to
take advantage of efficiencies and predictability, we will now pre-allocate the
entire `HUB_MAX_MEMORY` on startup.

As part of this update, a new environment variable has been added:
`HUB_MIN_MEMORY`. This variable will allow you to set the lower
boundary for Java heap size.

By default and as the optimal setting, `HUB_MIN_MEMORY` is set equal
to `HUB_MAX_MEMORY`, but can be set explicitly to a smaller amount
(for example, 512m) to allow Java, once again, to acquire memory gradually starting
from `HUB_MIN_MEMORY` to no more than
`HUB_MAX_MEMORY`.

## Limit Rapid Scan policy overrides to specific vulnerabilities

In previous Black Duck versions, Rapid Scan policy violations could be overridden by
policy and component. However, if new vulnerabilities were subsequently found,
existing overrides could suppress the violation, resulting in a false negative.

Now in Black Duck 2022.4.0, you can now override a specific vulnerability in rapid
scans using the existing yaml upload mechanism.

The vulnerability Id is validated to match the expected format.

```
---
version: 1.0
policy:
  overrides:
  - policyName: policyA
    components:
    -  name: component1
       version: version1
       vulnerabilities: 
       - vulnerabilityId1 
       - vulnerabilityId2 
    - name: component2
  - policyName: policyB
    components:
    - name: component3
```

## New Rapid Scan vulnerability properties added

The following properties have been added to vulnerabilities in the output of Rapid
Scans:

- publishedDate (Date value)
- vendorFixDate (Date value)
- workaround (String value)
- solution (String value)

## New BDSA Automatic Remediation setting (Beta)

When the Black Duck Security Advisory (BDSA) team analyzes a CVE vulnerability, they
check to see what component versions are affected by the vulnerability. Sometimes
they find that the vulnerability applies to a different set of versions. This new
feature will give you the ability to automatically ignore CVE vulnerabilities if the
BDSA team has found that the vulnerability does not apply to that component version.
This only affects vulnerabilities with the NEW status.

The BDSA Automatic Remediation is a **beta feature** and is **not** enabled by
default. To enable this feature, the following environment variable must be set:

```
BDSA_AUTO_REMEDIATION=true
```

The BDSA Auto Remediation setting can then be changed on the Admin > System Settings > BDSA Auto Remediation page.

Note: Whenever the user saves the setting, the system checks and may update
vulnerabilities for all projects. On large systems, this can take a long time and
have an impact on Black Duck performance.

## Updated Users & Groups management display

The look and feel of the Users and Groups tabs under Admin > Users & Groups
have been updated to display more cleanly by breaking up the various sections
(User/Group Details, Overall Roles, Project Groups, Projects, Users/User Groups)
into their own individual pages making it easier to manage your users and
groups.

## New Component Condition rule for policies

A new component condition for Unconfirmed Snippets has been added. The new policy
condition gives you the ability to create or edit a policy that allows you to
trigger a policy violation for snippets that have not been reviewed.

## New Software Bill of Materials (SBOM) Report CycloneDX v1.3 export format

You can now export the Software Bill of Materials report for your projects in
CycloneDX v1.3 format. This can be done by viewing a project version, clicking the
Reports tab, clicking the Create Report button, and then selecting CycloneDX v1.3 -
JSON. For more information on CycloneDX v1.3, please visit the [CycloneDX v1.3
reference page](https://cyclonedx.org/docs/1.3/json/).

## New Component Dependency Duplication Sensitivity system property

A new system property has been added to Black Duck to control the maximum number of
nodes (matches) per component added to resulting dependency tree in package manager
scan:

```
blackduck.match.limit.per.component
```

The default value of this system property is 10, thus the number of duplicated
components in the tree can not exceed the
`blackduck.match.limit.per.component` value (match limit per
component).

## Supported browser versions

- Safari Version 15.4 (16613.1.17.1.13, 16613)
  - Safari versions 13.0 and below are no longer supported
- Chrome Version 100.0.4896.75 (Official Build) (x86_64)
  - Chrome versions 71 and below are no longer supported
- Firefox Version 99.0 (64-bit)
  - Firefox versions 71 and below are no longer supported
- Microsoft Edge Version 100.0.1185.36 (Official build) (64-bit)
  - Microsoft Edge versions 78 and below are no longer supported

## Container versions

- blackducksoftware/blackduck-postgres:11-2.11
- blackducksoftware/blackduck-authentication:2022.4.0
- blackducksoftware/blackduck-webapp:2022.4.0
- blackducksoftware/blackduck-scan:2022.4.0
- blackducksoftware/blackduck-jobrunner:2022.4.0
- blackducksoftware/blackduck-cfssl:1.0.7
- blackducksoftware/blackduck-logstash:1.0.18
- blackducksoftware/blackduck-registration:2022.4.0
- blackducksoftware/blackduck-nginx:2.0.14
- blackducksoftware/blackduck-documentation:2022.4.0
- blackducksoftware/blackduck-upload-cache:1.0.23
- blackducksoftware/blackduck-redis:2022.4.0
- blackducksoftware/blackduck-bomengine:2022.4.0
- blackducksoftware/blackduck-matchengine:2022.4.0
- blackducksoftware/blackduck-webui:2022.4.0
- blackducksoftware/bdba-worker:2021.12.2
- blackducksoftware/rabbitmq:1.2.7
