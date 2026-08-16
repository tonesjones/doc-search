---
title: "New and changed features"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features.html"
content_id: "vhm89dHU__ODa4EFEmM43A"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:34.412466+00:00"
---

# New and changed features

## New GitHub SCM repository scanning and read-only BOM

You can now integrate Black Duck with your GitHub repository, to quickly and easily
gain visibility across all the repositories in GitHub, as well as the ability to add
as a project version BOM in Black Duck.

You can now do the following:

- **Add selected main repositories as a new project in Black Duck**: This
  allows users to quickly view the security and policy violation of the GitHub
  repository.
- **Run scans at will:** You can trigger a scan from the Black Duck version
  page that is mapped to the repository, to find any new problems in your current
  libraries, for example to find critical zero-day vulnerabilities quickly. The
  result of this scan creates a lighter, read-only BOM which provides a quick
  overview of your repository detailing the components and licenses found, and any
  vulnerabilities associated to those components.

Please note that this feature is currently only supported for Hosted Black Duck
customers. SCM integration utilizes a service that runs strictly within a Kubernetes
environment, either native or Kubernetes in Docker (KinD). The helm charts will need
to be used to install Black Duck to use this feature.

## New scan auto-unmapping management page

You can now manage when scans are scheduled to be unmapped from inactive project
versions. They need to meet the project version phase and inactivity time
conditions, and will only be unmapped after the grace period. The Scan
Auto-Unmapping page is found in Black Duck by clicking the Admin button → System
Settings → Data Retention → Scan Auto-Unmapping.

## New Automatic Scan Retry Header support for Black Duck Detect

A new Retry-After header has been added in the 429 response for Detect to know when
to attempt a rate limited scan again. The following properties have been added to
the `blackduck-config.env` file:

`BLACKDUCK_USE_QUEUE_RATE_LIMITING`: Set to `true`
to enable queue base rate limiting in your environment. Default value is
`false`.

`BLACKDUCK_INITIAL_RATE_LIMIT_DURATION_BRACKET_THRESHOLD_MINUTES`:
dictates the duration the system must be rate limiting before the system moves from
the first retry duration to the second retry duration.

`BLACKDUCK_RATE_LIMIT_DURATION_THRESHOLD_BRACKET_INCREMENT_MINUTES`:
Dictates the duration that the system will stay in a rate limiting bracket before
going to the next retry duration and multiplier.

`BLACKDUCK_INITIAL_RETRY_DURATION_MINUTES`: The initial duration of
the Retry-After header in the first rate limiting bracket.

`BLACKDUCK_RETRY_DURATION_MULTIPLIER_MINUTES`: The amount to multiply
the Retry-After Duration by each time the system reaches a new rate limit duration
bracket.

## New runtime threshold environment variable

You can now configure the threshold to determine long running jobs by adding the
following variable to your `blackduck-config.env` file:

- `BLACKDUCK_DEFAULT_JOB_RUNTIME_THRESHOLD_HOURS`={value in
  hours}

The default value for this environment variable is 24 hours.

## New Include Subprojects option for reports

You can now choose to include subprojects by checking the new **Include
Subproject** checkbox in the report generation dialog box when creating the
following reports:

- Notices File
- SBOM
- Version Details

Please note that this feature is enabled by default and subprojects were already
included in report generation previous to this change. This feature now explicitly
allows you to configure this functionality.

## New Transitive Upgrade Guidance

Please note that this feature was added in Black Duck 2023.1.0 and was accidentally
left out of the release notes for that version.

The simplest way to resolve security risk is to upgrade the version of the used
component with fewer vulnerabilities. It is easier to do for components used as
direct match. It is more difficult to mitigate or remove component vulnerabilities
brought in as transitive dependencies without understanding what root direct
dependency brought in that component. The goal of this feature is more simply and
directly provide transitive upgrade guidance to provide a better developer
experience and more clear call to action.

## Enhanced Black Duck Secure Container (BDSC)

Black Duck introduces a new type of container image scan and project view to simplify
managing the risk from container images. The container project can show the
aggregated BOM and risk, but it also provides a way to view risk layer by layer,
including separating risk from the base imagine or OS and the application layers. In
addition, we've added support for viewing where and when components are added or
removed in a layer.

Additionally, the Black Duck KnowledgeBase will expand its inventory to cover Docker
Hub base container images and layer by layer component details to enable Black Duck
to focus is scanning on the client container.

The existing Black Duck container image scanning as part of signature scanning, binary
scanning, and Docker Inspector has not changed and will continue to be supported.
The new container image scanning feature and project view will improve the user
experience for managing risk found in containers enabling customers to manage the
risk by container layer.

Please note that in order to take advantage of this feature, you must have Black Duck
Secure Container (BDSC) enabled on your product registration key. Customers with a
Black Duck Binary Analysis integrated subscription will have this included in their
license.

## Enhanced license risk aggregation - Limited customer availability

Prior to this enhancement, license risk from subprojects were not tracked or viewable
within parent projects. This presented the possibility that license risk could be
missed when using subproject hierarchies. Now, when you enable this feature, the
License Risk displayed for a subproject in your project's BOM will be determined by
the subproject's license risk and the highest license risk of its components.

Note that this feature is not general available and it not enabled by default.
Enhanced license risk aggregation will be made generally available in an upcoming
Black Duck release and will be enabled by default at that time.

## Enhanced SBOM Import Component Visibility

You now have the ability to identify which components originated as a result of the
SBOM import vs. other types of identification/scans or other imported SBOMs. In the
Project Version's Source tab, you can identify the SBOM type (SPDX or CycloneDX),
when the SBOM was imported, who supplied the SBOM, and the version of the tool used
to create the SBOM.

## Enhanced Component Versions page

The Component Versions page now more clearly displays what you are looking as far as
security risk based on the scoring system priority set by System Administrator. The
table now indicates if a component version has other vulnerabilities and how many
that comes from another scoring system, such as CVSS v2.

## Enhanced Jobs page functionality

The Processing tab of the Jobs pages will now display a warning icon next to jobs
that are running longer than normal. You can also filter this page on Long Running
jobs to display a list of these jobs.

In addition, new Prometheus metrics are available for users to see any jobs that are
running longer than usual on the system.

## Scanning hardware requirements changes

Black Duck 2023.10.0 sees a number of changes in scanning hardware requirements
therefore Black Duck customers must update their environments and allocate
additional hardware resources where necessary per the guidance below. Please see
[Black Duck Hardware Scaling
Guidelines](https://docs.blackduck.com/access?ft:originId=f598e2689f20062534e28c8999b4550b/42e9daee77bcf342ae2692e1ec6e7746.topic) to
stay up-to-date when changes are made to these recommendations.

Table 1. Hardware Scaling Guidelines

| Name | Details | |
| --- | --- | --- |
| 10sph | **Scans/Hour**: 50 **SPH % Increase**: 400%  **APIs/Hour**: 2,500  **Project Versions**: 10,000 | **IOPS**: Read: 15,000 / Write: 9,000 **Black Duck Services**: CPU: 10 core / Memory: 36 GB  **PostgreSQL**: CPU: 2 core / Memory: 8 GB  **Total**: CPU: 12 core / Memory: 44 GB |
| 120sph | **Scans/Hour**: 120 **SPH % Increase**: 0%  **APIs/Hour**: 3,000  **Project Versions**: 13,000 | **IOPS**: Read: 15,000 / Write: 15,000 **Black Duck Services**: CPU: 11 core / Memory: 56 GB  **PostgreSQL**: CPU: 4 core / Memory: 16 GB  **Total**: CPU: 15 core / Memory: 72 GB |
| 250sph | **Scans/Hour**: 300 **SPH % Increase**: 20%  **APIs/Hour**: 7,500  **Project Versions**: 15,000 | **IOPS**: Read: 15,000 / Write: 15,000 **Black Duck Services**: CPU: 16 core / Memory: 85 GB  **PostgreSQL**: CPU: 6 core / Memory: 24 GB  **Total**: CPU: 22 core / Memory: 109 GB |
| 500sph | **Scans/Hour**: 650 **SPH % Increase**: 30%  **APIs/Hour**: 18,000  **Project Versions**: 18,000 | **IOPS**: Read: 25,000 / Write: 25,000 **Black Duck Services**: CPU: 23 core / Memory: 133 GB  **PostgreSQL**: CPU: 16 core / Memory: 64 GB  **Total**: CPU: 39 core / Memory: 197 GB |
| 1000sph | **Scans/Hour**: 1400 **SPH % Increase**: 40%  **APIs/Hour**: 26,000  **Project Versions**: 25,000 | **IOPS**: Read: 25,000 / Write: 25,000 **Black Duck Services**: CPU: 44 core / Memory: 367 GB  **PostgreSQL**: CPU: 22 core / Memory: 88 GB  **Total**: CPU: 66 core / Memory: 455 GB |
| 1500sph | **Scans/Hour**: 1600 **SPH % Increase**: 6%  **APIs/Hour**: 41,000  **Project Versions**: 28,000 | **IOPS**: Read: 25,000 / Write: 25,000 **Black Duck Services**: CPU: 53 core / Memory: 464 GB  **PostgreSQL**: CPU: 26 core / Memory: 104 GB  **Total**: CPU: 79 core / Memory: 568 GB |
| 2000sph | **Scans/Hour**: 2300 **SPH % Increase**: 15%  **APIs/Hour**: 50,000  **Project Versions**: 35,000 | **IOPS**: Read: 30,000 / Write: 30,000 **Black Duck Services**: CPU: 64 core / Memory: 565 GB  **PostgreSQL**: CPU: 32 core / Memory: 128 GB  **Total**: CPU: 96 core / Memory: 693 GB |

Table 2. PostgreSQL Settings

| Name | Details | |
| --- | --- | --- |
| 10sph | **Scans/Hour**: 50 **PostgreSQL CPU/Memory**: 2 core / Memory: 8 GB  `shared_buffers` (MB): 2654  `effective_cache_size` (MB): 3185 | `autovacuum_max_workers`: 4 `maintenance_work_mem` (MB): 512 `max_connections`: 400  `work_mem` (MB): 50 |
| 120sph | **Scans/Hour**: 120 **PostgreSQL CPU/Memory**: CPU: 4 core / Memory: 16 GB  `shared_buffers` (MB): 5336  `effective_cache_size` (MB): 6404 | `autovacuum_max_workers`: 4 `maintenance_work_mem` (MB): 512 `max_connections`: 400  `work_mem` (MB): 50 |
| 250sph | **Scans/Hour**: 300 **PostgreSQL CPU/Memory**: CPU: 6 core / Memory: 24 GB  `shared_buffers` (MB): 8016  `effective_cache_size` (MB): 9619 | `autovacuum_max_workers`: 6 `maintenance_work_mem` (MB): 1024 `max_connections`: 500  `work_mem` (MB): 35 |
| 500sph | **Scans/Hour**: 650 **PostgreSQL CPU/Memory**: CPU: 16 core / Memory: 64 GB  `shared_buffers` (MB): 21439  `effective_cache_size` (MB): 25727 | `autovacuum_max_workers`: 6 `maintenance_work_mem` (MB): 1024 `max_connections`: 500  `work_mem` (MB): 35 |
| 1000sph | **Scans/Hour**: 1400 **PostgreSQL CPU/Memory**: CPU: 22 core / Memory: 88 GB  `shared_buffers` (MB): 29502  `effective_cache_size` (MB): 35403 | `autovacuum_max_workers`: 6 `maintenance_work_mem` (MB): 2048 `max_connections`: 600  `work_mem` (MB): 48 |
| 1500sph | **Scans/Hour**: 1600 **PostgreSQL CPU/Memory**: 26 core / Memory: 104 GB  `shared_buffers` (MB): 34878  `effective_cache_size` (MB): 41854 | `autovacuum_max_workers`: 8 `maintenance_work_mem` (MB): 4096 `max_connections`: 800  `work_mem` (MB): 58 |
| 2000sph | **Scans/Hour**: 2300 **PostgreSQL CPU/Memory**: 32 core / Memory: 128 GB  `shared_buffers` (MB): 42974  `effective_cache_size` (MB): 51569 | `autovacuum_max_workers`: 8 `maintenance_work_mem` (MB): 4096 `max_connections`: 800  `work_mem` (MB): 58 |

## Updated policy evaluation of Archived project version phase

The following changes have been made to the Archived project version phase:

- The policy expression for project version phase no longer allows 'Archived'
  as a value.
- Existing policy rules that contain project version phase and 'Archived'
  value will be automatically disabled.
- New policy rules and expression changes will no longer be evaluated on
  project versions in 'Archived' phase.

## Updated PostgreSQL settings

Starting with Black Duck 2023.10.0, PostgreSQL settings will be automatically set in
deployments using the PostgreSQL container. Customers using external PostgreSQL will
still need to apply the settings manually.

## Updated Black Duck Hosted Detect version

Black Duck 2023.10.0 now offers support for Black Duck Detect 9 on the Black Duck Detect
page and support for Detect 7.x has ended. After upgrading to Black Duck 2023.10.0,
customers currently using Detect 7.x will see a warning indicator stating that
Detect 7.x has reached end of support and that upgrading is recommended. Please
note, you will not be able to revert to Detect 7.x after changing this
configuration.

## Updated Artifactory and SCM integrations requirements

In order to use the Artifactory and SCM integrations in your environment, you must
have these features enabled on your registration key. Once enabled, you must add the
following in your `values.yaml` file:

```
enableIntegration: true
```

## Updated SCA as a Service deployment files

The deployment files used for SCA as a Service have been updated as follows:

- Updated RabbitMQ image from 1.2.14 to 1.2.29
- Added new environment variables in order to configure the ports to
  communicate correctly:

  - `BLACKDUCK_RABBIT_LISTENERS_PORT: "5672"`
  - `BLACKDUCK_RABBIT_MANAGEMENT_PORT: "15672"`

## Updated Show Unmatched Components functionality

The `BLACKDUCK_HUB_SHOW_UNMATCHED` property used to determine whether
or not "Unmatched Components" counts will be shown in project version components
view is now enabled by default.

Please note this change was made in Black Duck 2023.7.0 and was inadvertently left
out of that version's release notes.

## Updated audit trails for SBOM fields

The Activity tab for a project will now report the addition or modification to the
following SBOM fields:

- Package Supplier Name
- Package Supplier Email
- Package Supplier Type

## Updated reporting database tables

The following tables have been updated:

- A `created_at` column has been added to the
  `component_policies` table. This column contains a list of
  times when policy violations were created.
- A `purl` column has been added to the
  `component` table. The column contains the package URL
  for the component.

## Updated reporting database

The details stored as `channel_release_external_namespace` obtained
via API is now available via the component table of the reporting database as well.
It states the general namespace for the origin (maven, debian, ubuntu, etc).

## Updated login page and frame

The login page and frame surrounding Black Duck has been updated.

## Updated container scanning feature name

Black Duck Container Scanning - Limited Customer Availability has been renamed to
Black Duck Secure Container (BDSC). Black Duck Secure Container scanning provides
capabilities to identify components within container images, their layers and base
images.

The Product Registration page has been updated accordingly.

## Increased default storage service size on Kubernetes

Black Duck 2023.10.0 increases the container size and java heap size from 1GB storage
/ 512MB memory to 2GB storage / 1GB memory.

## Container versions

- blackducksoftware/blackduck-postgres:14-1.16
- blackducksoftware/blackduck-postgres-upgrader:14-1.1
- blackducksoftware/blackduck-postgres-waiter:1.0.10
- blackducksoftware/blackduck-cfssl:1.0.23
- blackducksoftware/blackduck-nginx:2.0.60
- blackducksoftware/blackduck-logstash:1.0.34
- blackducksoftware/blackduck-upload-cache:1.0.48
- blackducksoftware/bdba-worker:2023.9.4
- blackducksoftware/rabbitmq:1.2.32
- blackducksoftware/blackduck-webui:2023.10.0
- blackducksoftware/blackduck-authentication:2023.10.0
- blackducksoftware/blackduck-bomengine:2023.10.0
- blackducksoftware/blackduck-documentation:2023.10.0
- blackducksoftware/blackduck-integration:2023.10.0
- blackducksoftware/blackduck-jobrunner:2023.10.0
- blackducksoftware/blackduck-matchengine:2023.10.0
- blackducksoftware/blackduck-redis:2023.10.0
- blackducksoftware/blackduck-registration:2023.10.0
- blackducksoftware/blackduck-scan:2023.10.0
- blackducksoftware/blackduck-storage:2023.10.0
- blackducksoftware/blackduck-webapp:2023.10.0
