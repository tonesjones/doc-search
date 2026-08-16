---
title: "Hardware requirements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/hardware-requirements.html"
content_id: "JQVaSG3xOMr1wCWboCK7cQ"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:27.795989+00:00"
---

# Hardware requirements

## Supported systems

Black Duck supports the following systems for installation and
operation:

- 64-bit x86
- ARM64 (AArch64)

Note: BDBA and RL-service are currently not supported on ARM systems.

## Black Duck hardware scaling guidelines

For scalability sizing guidelines, see [Black Duck Hardware Scaling
Guidelines](https://docs.blackduck.com/access?ft:originId=f598e2689f20062534e28c8999b4550b/42e9daee77bcf342ae2692e1ec6e7746.topic).

## Black Duck database

DANGER

Do not delete data from the Black Duck database (`bds_hub`)
unless directed to do so by a Black Duck Technical Support representative. Be sure to
follow appropriate backup procedures. Deletion of data will cause errors ranging
from UI problems to complete failure of Black Duck to start. Black Duck Technical
Support cannot recreate deleted data. If no backups are available, Black Duck will
provide support on a best-effort basis.

## Disk space requirements

The amount of required disk space is dependent on the number of projects being managed, so
individual requirements can vary. Consider that each project requires approximately 200
MB.

Black Duck Software recommends monitoring disk utilization on Black Duck servers to
prevent disks from reaching capacity which could cause issues with Black Duck.

## BDBA scaling

BDBA scaling is done by adjusting the number of binaryscanner replicas and by adding
PostgreSQL resources based on the expected number of binary scans per hour that will be
performed. For every 15 binary scans per hour, add the following:

- One binaryscanner replica
- One CPU for PostgreSQL
- 4GB memory to PostgreSQL

If your anticipated scan rate is not a multiple of 15, round up. For example, 24 binary
scans per hour would require the following:

- Two binaryscanner replicas,
- Two additional CPUs for PostgreSQL, and
- 8GB additional memory for PostgreSQL.

This guidance is valid when binary scans are 20% or less of the total scan volume (by
count of scans).

Note: Installing Black Duck Alert requires 1 GB of additional memory.
