---
title: "Uninstalling Black Duck"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/uninstalling-black-duck.html"
content_id: "b3qjK_SyUSJJ93wAJ2~69g"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:14.435098+00:00"
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

  This command removes *all* unused volumes: volumes not referenced by
  *any* container are removed. This includes unused volumes not used by
  other applications.

Note that the PostgreSQL database is not backed up. Use these instructions to back up the database.
