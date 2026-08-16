---
title: "External Postgres Database Requirements"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/external-postgres-database-requirements.html"
content_id: "qo7YCeDAHDj67_Rfz8F1Kw"
version: "8.4.0"
section: "Installation References"
scraped_at: "2026-08-08T23:46:28.767924+00:00"
---

# External Postgres Database Requirements

- PostgreSQL major release version: `15` or
  `16`

  Note: Recommended PostgreSQL for version `15`: `15.8`
- Alert follows the Black Duck SCA [PostgreSQL Version Upgrade Schedule](https://documentation.blackduck.com/bundle/blackduck-compatibility/page/topics/PostgreSQL-Version-Upgrade-Schedule.html)
- Extension: `uuid-ossp` (Note: this should be installed prior to creating the database)
- Schemas: `public`, `alert`
- Roles/Privileges: Alert requires two sets of Postgres Privileges. The
  `Alert Admin` role is required to install
  `uuid-ossp` if it doesn't already exist. The `Alert
  User` role is required for all other operations during install and
  operation of the application.

  - Ensure the DB roles have the public schema on their
    search_path(s):

    ```
    ALTER ROLE <user> SET search_path = "$user", public;
    ```
  - The `Alert User` role should have the following privileges
    on all objects in the alert schema (or the schema/database when
    relevant):

    - `SELECT`
    - `INSERT`
    - `CREATE`
    - `UPDATE`
    - `DELETE`
    - `TRUNCATE`
    - `REFERENCES`
    - `TRIGGER`
    - `TEMPORARY`
    - `EXECUTE`
    - `USAGE`
  - The `Alert User` role should have the following privileges
    on all objects in the public schema (or the schema/database when
    relevant):

    - `SELECT`
    - `INSERT`
    - `UPDATE`
    - `DELETE`
    - `EXECUTE`

Note: The Postgres Admin user must have administrative priviledge OR the extension "uuid-ossp" must be installed, AND the following permission granted to the
Postgres Admin user: `GRANT UPDATE,SELECT ON public.databasechangeloglock`
