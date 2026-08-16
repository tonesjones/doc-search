---
title: "Hardware resource properties"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/hardware-resource-properties.html"
content_id: "XXlOgv1GfcTv4OPo3PLdMQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:21.290713+00:00"
---

# Hardware resource properties

- In the tuning yaml file, replace `<PROCESSOR_COUNT>` with the
  number of CPUs in the machine where the database resides. For example,
  `4`, `8`, `16`,
  `32`, etc.
- In the tuning yaml file, replace `<PHYSICAL_MEMORY>` with the
  physical ram size of the machine where the database resides. For example,
  `4g`, `16g`, `32g`,
  `64g`, etc.
- The `OPERATING_SYSTEM` variable specifies the operating system of the
  machine where the database resides. The default value is Linux. You can enter a new
  operating system value or override as needed. Valid values are:
  - `Linux` (default)
  - `Mac`
  - `Windows`
- In the tuning yaml file, replace `<IS_SSD>` with
  `true` or `false` as described in the appropriate
  section for your cloud infrastructure provider:
  - AWS RDS IsSSD property
  - Azure flexible server IsSSD property
  - GCP Cloud SQL IsSSD property
