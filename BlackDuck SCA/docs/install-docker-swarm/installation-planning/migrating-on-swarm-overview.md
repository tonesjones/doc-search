---
title: "Migrating on Swarm Overview"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/migrating-on-swarm-overview.html"
content_id: "czywzJG6t5wF_hBWWgEjYg"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:31.750425+00:00"
---

# Migrating on Swarm Overview

- The migration is completely automatic; no additional actions are needed beyond
  those for a standard Black Duck upgrade.
- The blackduck-postgres-upgrader container MUST run as root to make the layout and
  UID changes described above.
- On subsequent Black Duck restarts, blackduck-postgres-upgrader will determine
  that no migration is needed and immediately exit.
- OPTIONAL: After a successful migration, the blackduck-postgres-upgrader container
  no longer needs to run as root.

Refer to Chapter 6, Upgrading Black Duck, for database migration instructions if
upgrading from a pre-4.2.0 version of Black Duck.
