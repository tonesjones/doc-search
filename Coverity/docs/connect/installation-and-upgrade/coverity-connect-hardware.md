---
title: "Coverity Connect hardware"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-connect-hardware.html"
content_id: "EcOX_610rBuVkITDlAuzTA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:51.602683+00:00"
---

# Coverity Connect hardware

The following table lists the recommended hardware configurations for Coverity Connect
deployments. Note that these are recommendations and not necessarily requirements.

The hardware recommendations take into account the following Coverity Connect deployment options:

- Coverity Connect with an embedded database. This deployment includes the PostgreSQL database
  and the Coverity Connect application installed on the same server and is a
  common Coverity Connect deployment.
- Coverity Connect with an external database. In this deployment scenario, the
  Coverity Connect server uses an external PostgreSQL database. For more
  information, see Using an external PostgreSQL database with Coverity Connect.

Table 1. Minimum hardware deployment recommendations

| Server | CPU | RAM | Storage size | Storage device | Notes |
| --- | --- | --- | --- | --- | --- |
| Embedded database | E5-16xx/26xx v3 series | 32 GB+ DDR3 1066Mhz | 512GB+ | SSD *or* HDD | SSD: Enabling of TRIM recommended  HDD: 7200 rpm recommended |
| External database | 240GB+ |

Note:

- The minimum number of CPU cores is 8 with a minimum CPU clock speed of 2GHz.
- RAM should be 32 GB+ as a starting point. For existing Coverity Connect
  databases, it is recommended that the amount of RAM be at least 25% of the
  database size. The database size can be found in Coverity Connect by navigating
  to Help > About... > Database Size.
- Recommendations based on database size are a rough estimate.
- Beware of thin provisioning.
- Performance depends on a variety of factors (commits, web access, web services traffic,
  etc.) and can't be calculated by a formula. In addition, the performance SLA
  might vary.
- Requirements vary over time as database growth and usage patterns change.
- You should monitor resource usage (Java and PostgreSQL processes) and modify
  performance and resource allocations as necessary.
- Here is an example configuration for a typical production performance host
  running Coverity Connect with an embedded database as of 2018: 24 cores, 128GB
  RAM, 2TB HDD, 1TB SSD
- Make sure that the specified CPU/RAM is available all the time.
- If you deploy to a VM, ensure that the VM is at least on par with the
  recommended minimum configuration.
- VM supervisors tend to suspend high CPU RAM users when resource request exceeds
  supply.
- Troubleshooting performance problems on a VM is difficult because of the lack of
  visibility into the VM host's resource usage. CPU cores and RAM can be limited
  on an underprovisioned VM host.
- Sharing and available IOPS should be on par with the SSD/HDD.
- Storage virtualization is not recommended. Such systems might have problems
  achieving low-latency I/O performance.
- Most RAID controllers do not support TRIM on RAID volumes.
- TRIM is required to maintain performance and longevity of the SSD.
- RAID configurations with parity (such as RAID 5) are sub-optimal for database
  I/O.
