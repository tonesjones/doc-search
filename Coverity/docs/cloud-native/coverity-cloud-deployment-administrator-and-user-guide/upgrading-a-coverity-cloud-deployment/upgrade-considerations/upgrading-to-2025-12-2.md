---
title: "Upgrading to 2025.12.2"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upgrading-to-2025.12.2.html"
content_id: "_IQ0~KhrZ4~1RmCT92v0Nw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:29.222371+00:00"
---

# Upgrading to 2025.12.2

The 2025.12.2 release introduces the following changes:

- Documentation: In the 2025.12.2 release, for storage service custom domains, added
  further information on specifying custom domains in the
  `cim.properties` file. See Specify custom domains in the cim.properties file.
- Documentation: In the 2025.12.2 release, documented the solution to an issue where
  if Microsoft Azure PostgreSQL database environment has been recently migrated from
  Single Server to Flexible Server, or if the Flexible Server was newly provisioned,
  extensions that previously worked now fail. See Azure considerations when creating or migrating a PostgreSQL database and Microsoft Azure PostgreSQL database extensions fail.
- Important:

  Do NOT USE or CHANGE ANY `cnc` Helm chart
  `cim.commitrcp4` Helm keys. These are Black Duck
  internal use only.

Additionally, consider the following.

- As recommended, copy all container images from the new Black Duck repository to a
  local repository and use your local repository to deploy Coverity cloud. To create
  your own private Coverity cloud repository, see Create your own private Docker registry.
- Download, modify as needed, and deploy the new Helm chart for the current
  release. See Downloading the Helm chart from the Black Duck public Docker registry.
