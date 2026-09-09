---
title: "Installation without an External Database"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/installation-without-an-external-database.html"
content_id: "L0bmSSn2NhHUqm92XEThZg"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:07.471465+00:00"
content_hash: "126cc4d0431abd5c724fb3e9a8cd66a523956c79844410f0fbabef068c63b5e7"
---

# Installation without an External Database

The `docker-compose.yml` file is used to install Software Risk Manager without
an external database.

**To install Software Risk Manager without an external database:**

1. Select a password for the MariaDB root user, one that does not use single quote
   characters, and edit your `docker-compose.yml` file by specifying the
   password for both the `MARIADB_ROOT_PASSWORD` and
   `DB_PASSWORD` parameters.
2. Select a password for the Software Risk Manager admin user and edit your
   `docker-compose.yml` file by specifying the password for the
   `SUPERUSER_PASSWORD` parameter.
3. Run `docker-compose -f ./docker-compose.yml up -d` to start the SRM Docker
   containers.
4. Run `docker-compose -f ./docker-compose.yml logs -f` to view log data.

   When the message "The Server is now ready!" appears in the console, you can navigate
   to either <http://hostname:8080/srm> or <https://hostname:8443/srm>
   (depending on your HTTPS
   configuration) to log into your Software Risk Manager instance.

- To stop, run `docker-compose -f ./docker-compose.yml stop`.
- To remove the Docker containers automatically created, run `docker-compose -f
  ./docker-compose.yml down`.

Note: If you want to migrate data from an existing Software Risk Manager system, refer to these instructions.
