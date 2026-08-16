---
title: "Announcements for Version 2022.2.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements-for-version-2022.2.0.html"
content_id: "eSdVOP_wXypVmbAbWUDvHg"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:45.302661+00:00"
---

# Announcements for Version 2022.2.0

## Enhanced Signature Generation

Starting with Black Duck 2022.2.0, the Signature Scanner will default to generation
of signatures on the client rather than the server.

If you are using the Blackduck hosted service or if you are using the Helm Charts or
Docker Swarm ‘yaml’ files included in the release, this change will be seamless with
no action is required on your part. There will not be any interruption to your
service.

However, if you have customized your Helm Charts or use an override file, please
refer to [Rebalancing Guidance](https://community.blackduck.com/s/article/Rebalancing-an-On-Prem-Self-Hosted-Blackduck-Instance-to-accommodate-Enhanced-Scanning) on our Community page for
additional information to assist you with the transition.

## Page Limit Maximums on API Requests

In an ongoing effort to better manage system resources, a maximum page limit has been
introduced to certain API requests. The maximum page limit will be set to 1000 pages
with the possibility of change in future Blackduck versions. See the API
Enhancements section below for a list of the affected API requests in the 2022.2.0
version.

## Deprecated APIs

With Blackduck 2022.2.0, the `/cpes/{cpeId}/variants` endpoint will be
deprecated, to be replaced with `/cpes/{cpeId}/origins`. The
`/cpes/{cpeId}/variants` will be removed in Blackduck 2022.4.0.
The API link in the metadata for `/api/cpes` has also been updated to
return `/api/cpes/{cpeId}/origins` instead of
`/api/cpes/{cpeId}/variants`.

## Upcoming Resource Guidance Changes

In the upcoming Black Duck 2022.4.0 release, the default resource settings will be
updated and the recommended settings will increase for all scan volumes. The
2022.4.0 release will be accompanied by instructions on how to continue to use the
existing settings.

Please note, the exact possible scan throughput will vary based on your scan size,
type and composition. However, we used this breakdown in our internal testing to
gather the information in the table below:

- 50% full signature scans
- 40% full package manager scans
- 10% developer package manager scans

## File Organization Changes

In addition to the changes mentioned above, starting in 2022.4.0, the organization of
resource override YAML files will change.

For Kubernetes, the organization of resource override YAML files in the Helm chart
will change.

- The `values` folder will be renamed to
  `sizes-gen01`.
- The 4 previous t-shirt size files (`small.yaml`, etc.) will be
  moved to the new `sizes-gen02` directory.
- A new directory, `sizes-gen03`, will contain a resource
  overrides file for each of the configurations named in the table below; they
  are named `10sph.yaml`, `120sph.yaml`,
  etc.

For Swarm, Black Duck will no longer allocate container resources directly in
`docker-compose.yml`. Instead, resources will be specified in a
separate overrides file. The current resource allocations will be moved to
`sizes-gen02/resources.yaml`. For Black Duck 2022.4.0 and later,
multiple possible allocations will be provided in the `sizes-gen03
folder`.

For both Kubernetes and Swarm, there will be 7 allocations based on load as measured
in average scans per hour; if your anticipated load does not match one of the
predefined allocations, round up. For example, if you anticipate 100 scans per hour,
select `sizes-gen03/120sph.yaml`.

## Resource Guidance & Container Scalability

These settings will apply to both Kubernetes and Swarm installations.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Scans/Hour | Black Duck Services | PostgreSQL | Total |
| 10sph | 10 | CPU: 10 core  Memory: 29 GB | CPU: 2 core  Memory: 8 GB | CPU: 12 core  Memory: 37 GB |
| 120sph | 120 | CPU: 12 core  Memory: 46 GB | CPU: 4 core  Memory: 16 GB | CPU: 16 core  Memory: 62 GB |
| 250sph | 250 | CPU: 16 core  Memory: 106 GB | CPU: 6 core  Memory: 24 GB | CPU: 22 core  Memory: 131 GB |
| 500sph | 500 | CPU: 27 core  Memory: 208 GB | CPU: 10 core  Memory: 40 GB | CPU: 37 core  Memory: 249 GB |
| 1000sph | 1000 | CPU: 47 core  Memory: 408 GB | CPU: 18 core  Memory: 72 GB | CPU: 65 core  Memory: 480 GB |
| 1500sph | 1500 | CPU: 66 core  Memory: 593 GB | CPU: 26 core  Memory: 104 GB | CPU: 92 core  Memory: 697 GB |
| 2000sph | 2000 | CPU: 66 core  Memory: 593 GB | CPU: 34 core  Memory: 136 GB | CPU: 100 core  Memory: 729 GB |

## PostgreSQL Settings

Customers using the PostgreSQL container will need to set the values manually using
ALTER SYSTEM, and changes to `shared_buffers` won't take effect until
after the next time that PostgreSQL is restarted. These settings will apply to both
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

## Japanese language

The 2021.10.0 version of the UI, online help, and release notes has been localized to
Japanese.

## Simplified Chinese language

The 2021.10.0 version of the UI, online help, and release notes has been localized to
Simplified Chinese.
