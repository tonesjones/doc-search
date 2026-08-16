---
title: "Using the override file"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/using-the-override-file.html"
content_id: "YG7NkSKD5L9dnHtIBoHrQg"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:51.227500+00:00"
---

# Using the override file

You may want to override some of the default settings used by Black Duck. Instead of directly editing the `.yml` file, use the
`docker-compose.local-overrides.yml`, located in the
`docker-swarm` directory.

By using this file to modify default settings, your changes are preserved when you
upgrade: you no longer need to modify the `.yml` file after each Black Duck upgrade. T

Note in the `docker-compose` command, the
`docker-compose.local-overrides.yml` file *must* be the last
`.yml` file used. For example, the following command starts Black
Duck using an external database:

```
docker stack deploy -c docker-compose.externaldb.yml -c docker-compose.local-overrides.yml hub
```
