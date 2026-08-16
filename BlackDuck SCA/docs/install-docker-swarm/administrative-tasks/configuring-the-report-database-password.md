---
title: "Configuring the report database password"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-the-report-database-password.html"
content_id: "pEYUR6segUtIbxaoYrMTdg"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:54.746742+00:00"
---

# Configuring the report database password

This section provides instructions on configuring the report database password.

Use the `hub_reportdb_changepassword.sh` script, located in the
`docker-swarm/bin` directory to set or change the report database
password.

Note: This script sets or changes the report database password when using the database container
that is automatically installed by Black Duck. If you are using an
external PostgreSQL database, use your preferred PostgreSQL administration tool to
configure the password.

Note that to run the script to set or change the password:

- You may need to be a user in the docker group, a root user, or have
  `sudo` access.
- You must be on the Docker host that is running the PostgreSQL database
  container.

In the following example, the report database password is set to 'blackduck':

```
./bin/hub_reportdb_changepassword.sh blackduck
```
