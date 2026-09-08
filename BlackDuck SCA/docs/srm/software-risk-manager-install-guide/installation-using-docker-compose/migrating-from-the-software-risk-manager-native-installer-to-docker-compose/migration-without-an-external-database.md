---
title: "Migration Without an External Database"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/migration-without-an-external-database.html"
content_id: "tFMMKAZMjmgkVhQm42OlVw"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:14.164024+00:00"
content_hash: "12e2ecc7b48020de6f30281405d6b7d4056f22320f1898dd7b5da8fc1a93e717"
---

# Migration Without an External Database

The following steps cover migrating data from a Software Risk Manager system installed with
the native installer to an existing Docker Compose deployment.

**To migrate data from a Software Risk Manager system installed using the native
installer:**

1. Verify that your Software Risk Manager deployed with Docker Compose is running.
2. Verify that your Software Risk Manager deployed with the native installer is running.
3. Verify that the version numbers of both systems match.
4. Log on to your source Software Risk Manager server whose data you want to migrate.
5. Run `mysqldump` to create a backup file. You can run the following
   command to create a `dump-srm.sql` file after specifying the parameters
   that work for your database.

   ```
   mysqldump --host=127.0.0.1 --port=3306 --user=root -p codedx -r dump-srm.sql
   ```

   Note: The
   above command uses a database named `codedx`. Older versions of Software
   Risk Manager may use a database named `bitnami_codedx`.
6. You may encounter an issue running SRM if the database dump file makes use of
   `DEFINER`. Run the following command with `dump-srm.sql`
   replaced with the path of your database dump file. This will overwrite the existing
   database dump file with the definers
   removed.

   ```
   (Get-Content "dump-srm.sql") -replace '\sDEFINER=`[^`]*`@`[^`]*`','' | Out-File dump-srm.sql
   ```
7. Locate the directory path for your Software Risk Manager AppData directory (e.g.,
   /path/to/codedx_data/codedx_appdata). The AppData directory contains your analysis-files
   and log-files directories.
8. Copy your database dump file and Software Risk Manager AppData directory to the system
   running Software Risk Manager with Docker Compose.
9. Return to the system running Software Risk Manager with Docker Compose, change directory
   to this repository (srm-docker folder), and run the `migrate-data.ps1`
   script with the following commands. When prompted, enter the path to your dump-srm.sql
   file, your Software Risk Manager AppData directory, and specify the password for the
   Docker Compose root database user.

   ```
   cd /path/to/srm-docker
   pwsh ./admin/migrate-data.ps1
   ```

   Note: The above command will use the default
   values for the script parameters `-tomcatContainerName`
   (srm-docker-codedx-tomcat-1), `-dbContainerName`
   (srm-docker-codedx-db-1), and `dbName` (codedx). You can find your Docker
   container names by running `docker ps`.

   Your script output
   should look similar to the
   following:

   ```
   pwsh ./admin/migrate-data.ps1
   Enter the path to your mysqldump file: /path/to/dump-srm.sql
   VERBOSE: Checking database dump file path...
   Enter the path to your Software Risk Manager AppData folder: /path/to/codedx
   VERBOSE: Checking appdata path...
   VERBOSE: Checking appdata/analysis-files path...
   Enter the password for the docker MariaDB root user: **********
   VERBOSE: Checking PATH prerequisites...
   VERBOSE: Checking running containers...
   VERBOSE: Dropping database named codedx...
   VERBOSE: Creating database named codedx...
   VERBOSE: Creating temporary directory...
   VERBOSE: Copying database dump file to container...
   VERBOSE: Importing database dump file (may take a while)...
   VERBOSE: Deleting database dump file...
   VERBOSE: Deleting directories...
   VERBOSE: Deleting directory /opt/codedx/analysis-files...
   VERBOSE: Deleting directory /opt/codedx/keystore...
   VERBOSE: Deleting directory /opt/codedx/mltriage-files...
   VERBOSE: Copying directories...
   VERBOSE: Copying directory /path/to/codedx/analysis-files to /opt/codedx/analysis-files...
   VERBOSE: Copying directory /path/to/codedx/mltriage-files to /opt/codedx/mltriage-files...
   VERBOSE: Restarting Software Risk Manager...
   Restarting srm-docker-codedx-tomcat-1 ... done
   Restarting srm-docker-codedx-db-1     ... done
   Done
   ```
