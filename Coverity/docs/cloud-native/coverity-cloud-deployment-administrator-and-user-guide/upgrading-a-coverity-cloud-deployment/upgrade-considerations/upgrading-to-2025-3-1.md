---
title: "Upgrading to 2025.3.1"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upgrading-to-2025.3.1.html"
content_id: "njhtI9kGgRrnipxs3XDWgA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:33.999458+00:00"
---

# Upgrading to 2025.3.1

In additions to the features and changes released with 2025.3.0, the 2025.3.1 release
introduces the following changes:

- Base images for most -UBI pods are upgraded. See Docker base images.
- Documentation: NGINX Error 504 HTTP timeout error condition is described for very
  large PostgreSQL databases, along with solutions and preventive measures. See
  NGINX HTTP error 504: Gateway Timeout.
- Documentation: Created a single comprehensive PostgreSQL chapter that describes
  how to create a PostgreSQL database, migrate a PostgreSQL database, size
  PostgreSQL pod resources, use PostgreSQL read replicas, manage PostgreSQL
  databases, and statically tune a PostgreSQL database. See PostgreSQL databases and PostgreSQL pod.
- Documentation: `cim` pod and `postgres` pod
  resources clarification. New chapters are integrated immediately following the
  Infrastructure chapter. Links to the new resource chapters are added to the
  Infrastructure chapter. See the following:

  - PostgreSQL databases and PostgreSQL pod
  - Sizing a Coverity Connect (cim) pod for optimum performance
- Documentation: Removed maximum resource (CPU and memory) limitations from cim and
  postgres pod sizing. See the following:

  - PostgreSQL pod minimum resource requirements
  - Coverity Connect (cim) pod minimum resource requirements
- Important:

  Do NOT USE or CHANGE ANY `cnc` Helm chart
  `cim.commitrcp4` Helm keys. These are Black Duck
  internal use only.
