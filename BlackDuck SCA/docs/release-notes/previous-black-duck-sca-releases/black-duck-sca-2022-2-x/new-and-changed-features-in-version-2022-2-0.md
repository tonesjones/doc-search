---
title: "New and Changed Features in Version 2022.2.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features-in-version-2022.2.0.html"
content_id: "leRYt~7TF~NJBl7qRmQKsA"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:45.946091+00:00"
---

# New and Changed Features in Version 2022.2.0

## Logstash Update

In order to address the [CVE-2021-44832](https://nvd.nist.gov/vuln/detail/CVE-2021-44832) vulnerability, the Logstash image used in Black Duck has
been upgraded to 7.16.3 which uses Log4j2 version 2.17.1.

## Enhanced Signature Generation

As mentioned in the Announcements, the Signature Scanner will default to generation
of signatures on the client rather than the server.

If you are using the Blackduck hosted service or if you are using the Helm Charts or
Docker Swarm ‘yaml’ files included in the release, this change will be seamless and
no manual action is required. There will not be any interruption to your
service.

However, if you have customized your Helm Charts or use an override file, please
refer to our *[Rebalancing Guidance](https://community.blackduck.com/s/article/Rebalancing-an-On-Prem-Self-Hosted-Blackduck-Instance-to-accommodate-Enhanced-Scanning)* article on Community for
additional information to assist you with the transition.

You can also find more information regarding [Monitoring Black Duck using Prometheus and Grafana](https://community.blackduck.com/s/article/Monitoring-BlackDuck-using-Prometheus-and-Grafana) on
Community.

## Rapid Scan Enhancements

The same endpoints are used but a new header was added to accept the rapid scan mode.
New HTTP header is named 'X-BD-RAPID-SCAN-MODE' and accepts the following
values:

- ALL: The default operation. It will evaluate policy rules that are RAPID or
  (RAPID and FULL). When the header is null this is the default.
- BOM_COMPARE: Will evaluate all policy rules like ALL, but will now evaluate
  differently based on the type of policy rule modes. When the policy rule is
  (RAPID and FULL) it will behave like BOM_COMPARE_STRICT but if the the
  policy rule is only (RAPID) it will behave like ALL. Policies that are only
  are RAPID will have a null policy status in the results.
- BOM_COMPARE_STRICT: Will only evaluate policy rules that are (RAPID and
  FULL). All policy rules found in the positive result will have statuses of
  NEW or RESOLVED. Policy violations are compared to the existing project
  version BOM. If the policy violation was already known and visible in the
  BOM (active or overridden) it is not part of the rapid scan positive result,
  it will still be part of the full result following existing
  restrictions.

In order to run either of the BOM_COMPARE modes there must be an existing project
version in HUB.

## PostgreSQL 11 Container Migration

The CentOS PostgreSQL 9.6 container has now been replaced by the Blackduck PostgreSQL
11 container. The new `blackduck-postgres-upgrader` container will
migrate the database from PostgresSQL 9.6 to PostgreSQL 11 and will exit upon
completion.

Customers with non-core PG extensions are STRONGLY encouraged to uninstall them
before migrating and reinstall them after the migration completes successfully;
otherwise, the migration is likely to fail.

Customers with replication set up will need to follow the instructions in [the pg_upgrade documentation](https://www.postgresql.org/docs/11/pgupgrade.html) BEFORE they migrate. If the
preparations described there are not made, the migration will likely succeed, but
the replication setup will break.

**IMPORTANT:** Before starting the migration:

- Ensure that you have an extra 10% disk space to avoid unexpected issues
  arising from disk usage due to the data copying of system catalogs.
- Review root directory space and volume mounts to avoid running out of disk
  space as this can cause Linux system disruptions.

Updating to 2022.2.0 with **synopsysctl** will perform the following tasks:

- Stop the Black Duck instance
- Run a database migration job for users of the Black Duck-supplied PG
  container
- Update and restart the instance

**For Kubernetes and OpenShift users:**

- The migration is performed by a one-time job:
  - Stop Black Duck;
    e.g.,

    ```
    kubectl scale --replicas=0 -n <your_namespace> deployments --selector app=blackduck
    ```
  - Run the upgrade job;
    e.g.,

    ```
    helm upgrade <your_deployment_name> . -n <your_namespace> <your_normal_helm_options> --set status=Stopped --set runPostgresMigration=true
    ```
  - Restart Black Duck as normal with `helm
    upgrade`.
  - This migration replaces the use of a CentOS PostgreSQL container with
    a Black Duck-provided container. Also, the
    `synopsys-init` container is replaced with the
    `blackduck-postgres-waiter` container.
- On plain Kubernetes, the container of the upgrade job will run as root.
  However, the only requirement is that the job runs as the same UID as the
  owner of the PostgreSQL data volume.
- On OpenShift, the upgrade job assumes that it will run with the same UID as
  the owner of the PostgreSQL data volume.

**For Swarm users:**

- The migration is completely automatic; no extra actions are needed beyond
  those for a standard Black Duck upgrade.
- The `blackduck-postgres-upgrader` container MUST run as root
  in order to make the layout and UID changes described above.
- On subsequent Black Duck restarts, blackduck-postgres-upgrader will determine
  that no migration is needed and immediately exit.
- OPTIONAL: After a successful migration, the blackduck-postgres-upgrader
  container no longer needs to run as root.

## Updated Security Risk Ranking

Based on general industry trend, the default security risk ranking now uses CVSS 3.0
scores as the primary score metric along with BDSA to increase vulnerability scoring
accuracy.

The new default ranking is:

- BDSA (CVSS v3.x)
- NVD (CVSS v3.x)
- BDSA (CVSS v2)
- NVD (CVSS v2)

This update will only change the ranking for new installs. Any upgrades to existing
instances should maintain whatever ranking order was previously set.

## Version Detail Component Report Enhancement

A new **Component Link** column has been added to the Version Detail Component
Report. This column will contain the component's URL as displayed when viewing the
component's details page. This report is generated by selecting the desired project
on the Dashboard, selecting a version, clicking the Reports tab, clicking the Create
button, and then selecting Version Details Report. In the following pop-up, ensure
the Component checkbox is checked to generate the components report which includes
the new Component Link column.

## Vulnerability Warning Display Enhancement

When viewing component vulnerabilities in your projects, Black Duck will now warn you
if the vulnerability in question has a linked BDSA not associated with the version
of the component used by this project version. Viewing the specified vulnerability
will display a message stating one of the following messages.

In the case where a BDSA vulnerability does not have an associated NVD record:

> *The Black Duck Security Advisory (BDSA) team mapped <vulnerability ID> to
> this component version, but it was not included in the National
> Vulnerability Database (NVD)'s associated record.*

In the case where a NVD vulnerability does not have an associated BDSA record:

> *The National Vulnerability Database (NVD) mapped <vulnerability ID> to
> this component version, but the Black Duck Security Advisory team has
> determined that it is not affected.*

Please consult the Black Duck help documentation for more details on BDSA
vulnerabilities.

## Jobrunner Heap and CPU based throttling

Starting in Blackduck 2022.2.0, jobrunner containers will monitor their heap and CPU
usage and can reduce their workload based on the current resource usage. For
example, if the heap usage surpasses 90%, the jobrunner can pause itself until the
memory resources have recovered. When resources become available, the jobrunner will
then increase its workload in proportion to available resources.

If the jobrunner pauses itself, it will be displayed on the Admin > Diagnostics >
System Information > jobruntime page. You will see an entry such as:

> 1 Active job runner endpoint(s):
>
> docker-swarm_jobrunner_1.docker-warm_default/58993e70a84c(172.23.0.15),
> paused=true

The `"paused=true"` indicates that this jobrunner is not taking any
more work as a result of resource constraints. Once the resource utilization
recovers, the entry will change to `paused=false` and the jobrunner
will start to take on new work.

## Ignored Snippets in the Source Report

You can now configure your environment to have ignored snippets included in your
Source report. This can be done by setting the environment variable
`INCLUDE_IGNORED_COMPONENTS_IN_REPORT=TRUE`.

## Component Search Version Count Enhancement

You will now be able to see how many versions a particular component has when
searching for components to add to your projects. The count will be dynamically
displayed in the search results as you type the component name.

## Security Vulnerability Remediation Enhancement

The process to remediate security vulnerabilities has been clarified to prevent
confusion when attempting to change the remediation status on projects. When viewing
a security vulnerability in a project, you may see rows that are hashed out and
cannot be selected for remediation. This is due to the project having a linked type
of security vulnerability record, either BDSA or CVE. If that vulnerability record
is not prioritized in the Security Risk Ranking, a Remediation Plan cannot be
undertaken for that project. Switching to the prioritized security vulnerability
record will allow you to update the Remediation Plan for that project.

## Project Version Cloning Enhancement

You now have the ability to include deep license data when cloning project versions.
This can be done by selecting a project on your Dashboard and clicking the Settings
tab when viewing the project's versions.

## Search by Project Tags

You now have the ability to search and select projects by tags on the Find page. This
allows the creation of saved searches for project grouped by tag - supporting
dashboards for projects which could be in a common application identified by
tag.

## New Vulnerability Condition Rule for Policies

A new policy condition for Vulnerability IDs has been added. The new policy condition
gives you the ability to create or edit a policy that allows you to target specific
vulnerability (CVE or BDSA) IDs to flag components.

## New Software Bill of Materials (SBOM) Report SPDX Format

You can now export the Software Bill of Materials report for your projects in SPDX
format. This can be done by viewing a project version, clicking the Reports tab, and
then clicking the Create Report button. We currently support SPDX 2.2 with plans to
support other formats in later Blackduck versions.

## Enhanced Signature Scanning Request Volume Management

In an effort to better manage higher request volumes that can occur for Enhanced
Signature Scanning over a specific period of time, scan services will now return a
HTTP 429 (TOO MANY REQUESTS) error that will be handled by the client if the scan
services are at maximum operating limit. The client will then retry in increments of
30 seconds for 10 minutes before declaring that the scan has failed.

## New Sorting Option on the Find Page

Projects can now be sorted by Project Group on the Find page, making it easier to
search for projects that are assigned to specific project groups within your
organization.

## New projectGroupMembership filter for /api/search/project-versions

Using this filter will return all project versions that are descendant of the given
project group and match conditions specified in the other filters. The
`projectGroupMembership` filter will only return project groups
to which the user has access. An usage example being
`/api/search/projectversions?filter=projectGroupMembership:PG~{projectGroupId)`.

## Report Database Enhancement

Added a new view has been added to the reporting schema:

- reporting.scan_view

## Secured Communication Between Blackduck and Identity Provider (IdP)

Blackduck will now create a self signed certificate with 5 years of validity to sign
SAML authentication requests. The administrator can configure whether requests
require to be signed or not by going to Admin > System Settings > User
Authentication, selecting SAML in the **External Authentication** section, and
then checking the **Send Signed Authentication Request** checkbox.

The default setting for this option is unchecked or not required. When enabled, a
link to download the Blackduck public certificate will be made available and should
be distributed to your users for their IdPs to verify authentication requests.

## Assigning Unmatched Components to Known Components

It is now possible to assign unmatched components found during a BOM scan to a known
component.

## New Rapid Scan Component Dependency Tree

We will now show the dependency tree for all instances of the vulnerable component in
the project in Rapid Scans outputs. This will allow you to clearly see how that
component is being referenced by other referenced components or by sub-projects,
etc. An example Rapid Scan output for the `jackson-core` component
with three parent dependencies:

"componentName": "jackson-core",

"versionName": "2.9.6",

"dependencyTrees": [

[

"io.jitpack:module2:2.0-SNAPSHOT:module2:maven",

"com.fasterxml.jackson.module:jackson-module-kotlin:2.9.6",

"com.fasterxml.jackson.core:jackson-databind:2.9.6",

"com.fasterxml.jackson.core:jackson-core:2.9.6"

]

],

## Updated Project Group Role Names

The name for roles associated to project groups have been updated by removing the
"project groups" wording. The roles' functionality have not been changed by this
update. See the list below for how the roles have been updated.

- Project Group Manager → Project Manager
- Project Group Security Manager → Security Manager
- Project Group BOM Annotator → BOM Annotator
- Project Group BOM Manager → BOM Manager
- Project Group Code Scanner → Project Code Scanner
- Project Group Policy Violation Reviewer → Policy Violation Reviewer
- Project Group Viewer → Project Viewer

## Project and Project Group Management Enhancements

You can now more easily add several users and project groups to projects and project
groups. Dropdown menus have been enhanced to allow multiple selections in a single
add user or project group interaction.

## Logstash Container Memory Increase

Due to potential crashing or restarts caused by out of memory issues, we have
increased the memory allocated to the Logstash container from 1024M to 2560M. This
should result in fewer webapp interruptions, impacting your operations.

## Project Group Deletion Enhancement

It is now no longer possible to delete a project group if it is referred to in any
existing policy rule expression.

## Added new extensions when searching for strings

The following extensions have been added to the list of extensions we allow to search
for strings to maintain extension compatibility with FLLD/FLCD scanning in the
KnowledgeBase.

- pkginfo
- properties
- pc

## Supported browser versions

- Safari Version 15.0 (16612.1.29.41.4, 16612)
  - Safari versions 13.0 and below are no longer supported
- Chrome Version 94.0.4606.71 (Official Build) (x86_64)
  - Chrome versions 71 and below are no longer supported
- Firefox Version 92.0.1 (64-bit)
  - Firefox versions 71 and below are no longer supported
- Microsoft Edge Version 94.0.992.38 (Official build) (64-bit)
  - Microsoft Edge versions 78 and below are no longer supported

## Container versions

- blackducksoftware/blackduck-postgres:11-2.7
- blackducksoftware/blackduck-authentication:2022.2.0
- blackducksoftware/blackduck-webapp:2022.2.0
- blackducksoftware/blackduck-scan:2022.2.0
- blackducksoftware/blackduck-jobrunner:2022.2.0
- blackducksoftware/blackduck-cfssl:1.0.5
- blackducksoftware/blackduck-logstash:1.0.16
- blackducksoftware/blackduck-registration:2022.2.0
- blackducksoftware/blackduck-nginx:2.0.12
- blackducksoftware/blackduck-documentation:2022.2.0
- blackducksoftware/blackduck-upload-cache:1.0.21
- blackducksoftware/blackduck-redis:2022.2.0
- blackducksoftware/blackduck-bomengine:2022.2.0
- blackducksoftware/blackduck-matchengine:2022.2.0
- blackducksoftware/blackduck-webui:2022.2.0
- blackducksoftware/bdba-worker:2021.12.1
- blackducksoftware/rabbitmq:1.2.6
