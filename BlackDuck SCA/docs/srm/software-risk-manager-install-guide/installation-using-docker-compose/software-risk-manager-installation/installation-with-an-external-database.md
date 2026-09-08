---
title: "Installation with an External Database"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/installation-with-an-external-database.html"
content_id: "eS7oUNMX9c6A0ZqRY5UofQ"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:08.071929+00:00"
content_hash: "74f68d4754ecf0d5ea8801e2610c007bd80498ce5b8a66d9c6b0ad5a62717837"
---

# Installation with an External Database

**To install Software Risk Manager with an external database:**

1. Select a password for the Software Risk Manager admin user and edit your
   `docker-compose-external-db.yml` file by specifying the
   password for the `SUPERUSER_PASSWORD` parameter.
2. Edit the `docker-compose-external-db.yml` file by appending
   `&useSSL=true&requireSSL=true` to the
   `DB_URL` parameter.
3. Edit the `docker-compose-external-db.yml` file as follows:
   1. Enter the database username for the `DB_USER`
      parameter.
   2. Enter the database password for the `DB_PASSWORD`
      parameter.
   3. Update the `DB_URL` parameter by specifying your database
      instance hostname.
   4. Update the `DB_URL` parameter by specifying your Software
      Risk Manager database name (e.g., "srmdb").

      The following is an
      example of a `DB_URL` parameter value using hostname
      `db-hostname` and database name
      `srmdb`:

      ```
      "jdbc:mysql://db-hostname/srmdb?sessionVariables=sql_mode='STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION'&permitMysqlScheme"
      ```

      If
      you followed the steps required for secure transport, your
      connection string will look like the following:

      ```
      "jdbc:mysql://db-hostname/srmdb?sessionVariables=sql_mode='STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION'&useSSL=true&requireSSL=true&permitMysqlScheme"
      ```
4. Follow the HTTPS instructions if your deployment requires TLS/SSL.
5. Start Software Risk Manager with the following command:

   ```
   docker-compose -f ./docker-compose-external-db.yml up -d
   ```

   You
   can run the following commands to view Software Risk Manager log data
   (assumes an `srm-docker-codedx-tomcat-1` container
   name):

   ```
   docker exec srm-docker-codedx-tomcat-1 tail -f /opt/codedx/log-files/codedx.log
   docker logs srm-docker-codedx-tomcat-1
   ```

Note: If you want to migrate data from an existing Software Risk Manager system, refer to
these instructions.
