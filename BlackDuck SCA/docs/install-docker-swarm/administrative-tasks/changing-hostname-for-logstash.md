---
title: "Changing hostname for logstash"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/changing-hostname-for-logstash.html"
content_id: "M1XSlrCBNaeZB6BBQ0YMeg"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-10-04T23:32:24.675273+00:00"
content_hash: "44275f074254279d574d785d8e6774c39a8743ee48c7c93b7833dd440bab200c"
---

# Changing hostname for logstash

When you make changes to the hostname and service name for logstash, they are not pushed to the internal PostgreSQL container. For example, you might want to change the logstash hostname to bdlogstash because you're using logstash for another purpose and you now want to write PostgreSQL logs to bdlogstash; make the following changes:

1. In `blackduck-config.env` change logstash to bdlogstash `HUB_LOGSTASH_HOST=bdlogstash`.
2. Edit `docker-compose.yml` and change logstash to bdlogstash.

   bdlogstash:

   ```
   image: blackducksoftware/blackduck-logstash:1.0.9
   volumes: ['log-volume:/var/lib/logstash/data']
   env_file: [blackduck-config.env]
   ```
3. Add `env_file: [blackduck-config.env]` to the postgres container definition in `docker-compose.yml` so that it reads the hostname change.

   `env_file: [blackduck-config.env]`
