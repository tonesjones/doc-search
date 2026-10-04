---
title: "Uninstalling Black Duck"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/uninstalling-black-duck.html"
content_id: "wdGbE3VKa3jMslKyxxFJyA"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-10-04T23:32:25.713791+00:00"
content_hash: "f53334b6737c207922d3eed22161cf5e319b25da5b64dfb3dc2dec081bdb6534"
---

# Uninstalling Black Duck

Follow these instructions to uninstall Black Duck:

- Stop and remove the containers, networks and secrets.

  ```
  docker stack rm ${stack name}
  ```
- Remove all unused volumes:

  ```
  docker volume prune -a
  ```

  CAUTION:

  This command removes *all* unused volumes: volumes not referenced by *any* container are removed. This includes unused volumes not used by other applications.

Note that the PostgreSQL database is not backed up. Use these instructions to back up the database.
