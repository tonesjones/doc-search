---
title: "Modifying the PostgreSQL usernames for an existing external database"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/modifying-the-postgresql-usernames-for-an-existing-external-database.html"
content_id: "601NRrqcBSxgfaOCer_A0w"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:53.007896+00:00"
---

# Modifying the PostgreSQL usernames for an existing external database

[HUB-15724]By default, the username of
the PostgreSQL database user is **blackduck_user** and the username of the PostgreSQL
administrator is **blackduck**.

If you are using an external PostgreSQL database, you can change these usernames.

These instructions are for an existing Black Duck instance in which the
external database currently uses the **blackduck** and **blackduck_user** user
names. To change the user names for a new configuration of an external database, follow
the instructions in the previous section.

Important: For Black Duck database users who don't have administrator
privileges, which is common with hosted providers such as GCP and RDS, connect to the
bds_hub database and run `GRANT blackduck_user TO blackduck;`

To modify the existing PostgreSQL account names:

1. Stop Black Duck.
2. Rename the users and reset the passwords In the `bds_hub`
   database.

   ```
   alter user blackduck_user rename to NewName1 ;
   alter user blackduck rename to NewName2 ;
   alter user NewName1 password 'NewName1Password' ;
   alter user NewName2 password 'NewName2Password' ;
   ```
3. In the `hub-postgres.env` file, located in the
   `docker-swarm` directory, edit the values for
   HUB_POSTGRES_USER AND HUB_POSTGRES_ADMIN. The value for HUB_POSTGRES_USER is the
   new username for **blackduck_user**. The value for HUB_POSTGRES_ADMIN is the
   new username for **blackduck**. For example:

   ```
   HUB_POSTGRES_USER=NewName1
   HUB_POSTGRES_ADMIN=NewName2
   ```
4. Restart Black Duck.

   Note: In the 2020.4.0 release, the BDIO database was removed.
