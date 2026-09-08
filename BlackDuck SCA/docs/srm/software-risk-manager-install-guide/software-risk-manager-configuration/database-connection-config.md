---
title: "Database Connection Config"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/database-connection-config.html"
content_id: "FGE8EuGzNmwpWy9vKDx5yQ"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:19.712600+00:00"
content_hash: "27eb96be51bc3d83865973f213d0dde796a97841b62b1c34ce1a247c279ecdac"
---

# Database Connection Config

Software Risk Manager requires a [MariaDB](https://mariadb.org/) database for storage. The MariaDB database is
automatically installed and configured during installation. The following properties are
used to configure Software Risk Manager database connections and are set automatically
during installation. **Please do not modify these settings** unless there is a strong
need to setup an alternate database for use with Software Risk Manager. However, doing
so might cause problems when installing Software Risk Manager upgrades.

- `swa.db.url` - The JDBC URL of the database Software Risk Manager
  will be communicating with
- `swa.db.user` - The username that will be used to access the
  database
- `swa.db.password` - The password that will be used to access the
  database

For instance, to configure Software Risk Manager to communicate with a MariaDB database
running on the same machine as the Software Risk Manager server with a username of
"database_username" and password of "database_password," use the following
configuration:

```
swa.db.url = jdbc:mysql://localhost/codedx?permitMysqlScheme
swa.db.user = database_username
swa.db.password = database_password
```
