---
title: "Announcements for Version 2022.4.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements-for-version-2022.4.0.html"
content_id: "7RJKpaBeX5BrtvD993nbLg"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:38.944196+00:00"
---

# Announcements for Version 2022.4.0

## Security Advisory for Spring Framework (CVE-2022-22965)

Black Duck is aware of the disclosed security issue relating to the Spring Framework
open source software, CVE-2022-22965 (tracked in the Black Duck KnowledgeBase™ as
BDSA-2022-0858), disclosed on March 30th, 2022. For more information about the
vulnerability, see the official CVE entry: <https://tanzu.vmware.com/security/cve-2022-22965>

On March 31st, 2022, Spring released Spring Framework versions 5.3.18 & 5.2.20,
which address the vulnerability described by CVE-2022-22965.

Currently, Black Duck believes there is limited exposure to Black Duck SIG products,
services, and systems. To the extent we have had exposure, we have applied
mitigations that prevent attempted exploitation. We have completed all internal
investigations and the results of those investigations can be found in the “Product
Status” section of our [Community advisory page](https://community.blackduck.com/s/article/Synopsys-Software-Integrity-Group-SIG-Advisory-Regarding-CVE-2022-22965).

Finally, to be clear, the previously mentioned investigation is focused exclusively
on CVE-2022-22965 (Spring Framework) and should not be confused with CVE-2022-22963
(Spring Cloud Function).

At the time of publication, Black Duck has not identified any exposure to
CVE-2022-22963 (tracked in the Black Duck Hub KnowledgeBase™ as BDSA-2022-0850) in
SIG products. If new details become available which change this evaluation, a
separate advisory for CVE-2022-22963 will be published.

## Upgrading to Black Duck 2022.4.0

Please note that upgrading to Black Duck 2022.4.0 may take longer than expected due
to the execution of migration scripts and other new processes introduced in this
version. More details can be found in the New and Changed Features section
below.

## Resource Guidance Changes

The default resource settings have updated and the recommended settings have
increased for all scan volumes. The previous resource settings are still available
and have been moved to new directories as described below, but their use is
discouraged.

Please note, the exact possible scan throughput will vary based on your scan size,
type and composition. However, we used this breakdown in our internal testing to
gather the information in the table below:

- 50% full signature scans
- 40% full package manager scans
- 10% developer package manager scans

## Container resource limits

Starting with Black Duck 2022.4.0, all containers will have resource limits set,
whereas previously, some containers did not. For example, previous resource
allocations did not set a CPU limit for the bomengine container, so it could use CPU
disproportionate to the containers with limits. Since the new sizes below do not
allow unbounded CPU usage, customers may see a decrease in scan throughput if they
choose one of the new sizes that looks close to the old limits.

## File organization changes

In addition to the changes mentioned above, the organization of resource override
YAML files has changed.

For Kubernetes, the organization of resource override YAML files in the Helm chart
has changed:

- The `values` folder has been renamed to
  `sizes-gen01`.
- The 4 previous t-shirt size files (`small.yaml`, etc.) have
  been moved to the new `sizes-gen02` directory.
- A new directory, `sizes-gen03`, now contains a resource
  overrides file for each of the configurations named in the table below; they
  are named `10sph.yaml`, `120sph.yaml`,
  etc.

For Swarm, Black Duck no longer allocates container resources directly in
`docker-compose.yml`. Instead, resources are specified in a
separate overrides file. The previous resource allocations, from Black Duck versions
2022.2.0 and earlier, have been moved to
`sizes-gen02/resources.yaml`. Starting with Black Duck 2022.4.0 and
later, multiple possible allocations will be provided in the `sizes-gen03
folder`.

For both Kubernetes and Swarm, there are 7 allocations based on load as measured in
average scans per hour; if your anticipated load does not match one of the
predefined allocations, round up. For example, if you anticipate 100 scans per hour,
select `sizes-gen03/120sph.yaml`.

## Resource Guidance & Container Scalability

These settings apply to both Kubernetes and Swarm installations.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Scans/Hour | Black Duck Services | PostgreSQL | Total |
| 10sph | 10 | CPU: 12 core  Memory: 30 GB | CPU: 2 core  Memory: 8 GB | CPU: 14 core  Memory: 38 GB |
| 120sph | 120 | CPU: 13 core  Memory: 46 GB | CPU: 4 core  Memory: 16 GB | CPU: 17 core  Memory: 62 GB |
| 250sph | 250 | CPU: 17 core  Memory: 118 GB | CPU: 6 core  Memory: 24 GB | CPU: 23 core  Memory: 142 GB |
| 500sph | 500 | CPU: 28 core  Memory: 210 GB | CPU: 10 core  Memory: 40 GB | CPU: 38 core  Memory: 250 GB |
| 1000sph | 1000 | CPU: 47 core  Memory: 411 GB | CPU: 18 core  Memory: 72 GB | CPU: 65 core  Memory: 483 GB |
| 1500sph | 1500 | CPU: 66 core  Memory: 597 GB | CPU: 26 core  Memory: 104 GB | CPU: 92 core  Memory: 701 GB |
| 2000sph | 2000 | CPU: 66 core  Memory: 597 GB | CPU: 34 core  Memory: 136 GB | CPU: 100 core  Memory: 733 GB |

## PostgreSQL Settings

Customers using the PostgreSQL container will need to set the values manually using
ALTER SYSTEM, and changes to `shared_buffers` won't take effect until
after the next time that PostgreSQL is restarted. These settings apply to both
Kubernetes and Swarm installations.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Scans/Hour | PostgreSQL CPU/Memory | shared_buffers (MB) | effective_cache_size (MB) |
| 10sph | 10 | CPU: 2 core  Memory: 8 GB | 2654 | 3185 |
| 120sph | 120 | CPU: 4 core  Memory: 16 GB | 5338 | 6406 |
| 250sph | 250 | CPU: 6 core  Memory: 24 GB | 8018 | 9622 |
| 500sph | 500 | CPU: 10 core  Memory: 40 GB | 13377 | 16053 |
| 1000sph | 1000 | CPU: 18 core  Memory: 72 GB | 24129 | 28955 |
| 1500sph | 1500 | CPU: 26 core  Memory: 104 GB | 34880 | 41857 |
| 2000sph | 2000 | CPU: 34 core  Memory: 136 GB | 45600 | 54720 |

## Upcoming PostgreSQL 9.6 deprecation

As previously announced, support for running Black Duck on PostgreSQL 9.6 ended with
the 2021.6.0 release of Black Duck. Starting with the 2022.7.0 release of Black
Duck, attempting to run Black Duck with PostgreSQL 9.6 will generate an error, and
Black Duck will fail to start.

## End of support for Desktop Scanner on RHEL 7 and CentOS 7

As of 2022.4.0, Black Duck will no longer build new versions of the Desktop Scanner
for Red Hat Enterprise Linux 7 and CentOS 7. Additionally in the upcoming 2022.7.0
release, the binaries will be dropped altogether.

## Updated PostgreSQL support schedule

Starting with the upcoming **2022.10.0** release, Black Duck will end support for
external PostgreSQL 11. Please see the table below for the projected dates for the
beginning and end of support for future PostgreSQL versions.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| PG Version | First Release | Last Release | BD External Support Added | BD External Support End |
| 16.x | Late 2023 | Late 2028 | 2024.7.0 | 2026.10.0 |
| 15.x | Late 2022 | Late 2027 | 2023.7.0 | 2025.10.0 |
| 14.x | September 2021 | November 2026 | 2022.7.0 | 2024.10.0 |
| 13.x | September 2020 | November 2025 | 2021.8.0 | 2023.10.0 |
| 12.x | October 2019 | November 2024 | X | X |
| 11.x | October 2018 | November 2023 | 2020.6.0 | 2022.10.0 |

## Azure PostgreSQL 13 Flex Server Configuration

When installing Black Duck, Azure users may encounter the following error message
when running the `external-postgres-init.pgsql` init script:

|  |
| --- |
| `psql:/dev/fd/63:25: ERROR: extension "pgcrypto" is not allow-listed for "azure_pg_admin" users in Azure Database for PostgreSQL` |

To prevent this error, ensure that server parameter
'`azure.extensions`' has value '`PGCRYPTO`' when
using Azure PG 13 Flex Server.

## Deprecrated APIs

The following legacy API Solr endpoints have been deprecated and will be removed in
the Black Duck 2022.7.0 release:

- GET `/api/search/components`
- GET `/api/autocomplete/component`

## Japanese language

The 2022.2.0 version of the UI, online help, and release notes has been localized to
Japanese.

## Simplified Chinese language

The 2022.2.0 version of the UI, online help, and release notes has been localized to
Simplified Chinese.
