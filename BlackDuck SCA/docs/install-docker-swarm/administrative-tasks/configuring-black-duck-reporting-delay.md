---
title: "Configuring Black Duck reporting delay"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-black-duck-reporting-delay.html"
content_id: "XGeu45GAw_DllXIebEp_0g"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:59.760472+00:00"
---

# Configuring Black Duck reporting delay

In Black Duck
2026.7.0 the reporting database job process runs every 480 minutes, which
is configurable.

To configure a different reporting delay:

1. Edit the `blackduck-config.env` file in the `docker-swarm`
   directory and configure `BLACKDUCK_REPORTING_DELAY_MINUTES=<value in
   minutes>`

   For example, `BLACKDUCK_REPORTING_DELAY_MINUTES=360`
2. Restart the containers.
