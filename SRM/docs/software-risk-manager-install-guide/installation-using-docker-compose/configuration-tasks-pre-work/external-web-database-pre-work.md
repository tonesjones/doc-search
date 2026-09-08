---
title: "External Web Database Pre-work"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/external-web-database-pre-work.html"
content_id: "dowJPIDJ1pmq_npy2HxdOw"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:03.753529+00:00"
content_hash: "f6a197c683c65d9ee47e30d330bcbaf7ead5bbd07dd0e3fde3673bae9329a503"
---

# External Web Database Pre-work

Software Risk Manager includes a MariaDB database that requires no configuration on your
part, so you can skip this section if you do not plan to use an external database
instance.

Your MariaDB/MySQL database must be on port 3306.

If you prefer an external database, the web workload supports MariaDB version 10.6.x and
MySQL version 8.0.x. Complete the configuration tasks shown below before installing Software
Risk Manager with an external web database.

Your MariaDB/MySQL database must include the following variable configuration:

- `optimizer_search_depth=0`
- `character_set_server=utf8mb4`
- `collation_server=utf8mb4_general_ci`
- `lower_case_table_names=1`
- `log_bin_trust_function_creators=1`

The `log_bin_trust_function_creators` parameter is required when using
replication (sometimes enabled by default).

If you are using a database instance hosted by AWS, Azure, or GCP, refer to the following:

- [How to create a new AWS parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html)
- [How to configure Azure Database for MySQL parameters](https://learn.microsoft.com/en-us/azure/mysql/single-server/how-to-server-parameters)
- [How to configure GCP Cloud SQL MySQL database flags](https://cloud.google.com/sql/docs/mysql/flags).

Refer to the Web Database Workload Requirements section for database instance configuration
details.

**To create the database catalog and Software Risk Manager database user:**

Note: If you have to reinstall Software Risk Manager and delete your Software Risk Manager data,
you must repeat steps 2 and 3 below after deleting your Software Risk Manager Docker
volume.

1. Create a database user.

   You can customize the following statement to create a user
   named "srm." Remove `REQUIRE SSL` when not using TLS (your database
   instance may require security transport).

   `CREATE USER 'srm'@'%' IDENTIFIED
   BY 'enter-a-password-here' REQUIRE SSL;`
2. Create a database catalog.

   The following statement creates a catalog named srmdb:

   `CREATE DATABASE srmdb;`
3. Grant required privileges on the database catalog to the database user you created.

   The
   following statements grant permissions to the srm database user.

   `GRANT
   SELECT, INSERT, UPDATE, DELETE, CREATE, CREATE TEMPORARY TABLES, ALTER, REFERENCES,
   INDEX, DROP, TRIGGER ON srmdb.* to 'srm'@'%'; FLUSH PRIVILEGES;`

If your database configuration requires Software Risk Manager to trust a certificate (e.g.,
the [Amazon RDS root certificate](https://s3.amazonaws.com/rds-downloads/rds-ca-2019-root.pem)), follow the Trust
Certificates instructions to trust your database certificate and update the volumes
section of your `docker-compose-external-db.yml` file.
