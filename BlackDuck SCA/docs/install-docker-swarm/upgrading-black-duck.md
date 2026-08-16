---
title: "Upgrading Black Duck"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/upgrading-black-duck.html"
content_id: "uKlQDT7BZjtb~wg61EIoQA"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:14.996927+00:00"
---

# Upgrading Black Duck

Black Duck supports upgrading to any available version,
giving you the ability to jump multiple versions in a single upgrade.

Note: A database administrator will need to enable installation of the `hstore`
PostgreSQL extension before installing or upgrading to 2023.4.0 or later.

Note: For customers upgrading from a version prior to 2019.8.0, two jobs, the
VulnerabilityRepriortizationJob and the VulnerabilitySummaryFetchJob run at start up to
synchronize vulnerability data.

These jobs may take some time to run and the overall
vulnerability score for existing BOMs will not be available until these jobs
complete. Users with the System Administrator role can use the Black Duck Jobs page to monitor these jobs.

Note: When upgrading from a version prior to 2018.12.0, you will experience a longer than usual
upgrade time due to a data migration that is needed to support new features in this
release. Upgrade times will depend on the size of the Black Duck
database. If you would like to monitor the upgrade process, please contact Black Duck
Customer Support for instructions.
