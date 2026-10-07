---
title: "Configuring Black Duck reporting delay"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-black-duck-reporting-delay.html"
content_id: "o3lej2FiuZ6qF5XFcrptDA"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-10-04T23:32:25.121553+00:00"
content_hash: "b94d997f4a81d5da3e86b60c0dc68139928fd4d6950a485af3eb1192477eaa7a"
---

# Configuring Black Duck reporting delay

In Black Duck2026.7.1 the reporting database job process runs every 480 minutes, which is configurable.

To configure a different reporting delay:

1. Edit the `blackduck-config.env` file in the `docker-swarm` directory and configure `BLACKDUCK_REPORTING_DELAY_MINUTES=<value in minutes>`

   For example, `BLACKDUCK_REPORTING_DELAY_MINUTES=360`
2. Restart the containers.
