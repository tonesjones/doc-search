---
title: "Configuring the containers' time zone"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-the-containers-time-zone.html"
content_id: "mgTREDW8WXgrIDpv0a7EyQ"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:00.320688+00:00"
---

# Configuring the containers' time zone

By default, the time zone for Black Duck containers is UTC. For monitoring purposes, you
may want to change this value so that the timestamps shown in logs reflect the local
time zone.

To configure a different time zone:

1. Set the value of the TZ environment variable in the
   `blackduck-config.env` file in the
   `docker-swarm` directory to the new time zone. Use the values
   shown in Wikipedia, as shown [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

   For example, to change the timezone to that used in Denver, Colorado, enter:

   ```
   TZ=America/Denver
   ```
2. Restart the containers.
