---
title: "Migration With an External Database"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/migration-with-an-external-database.html"
content_id: "U7jV81t3VGLPiBs0SPGjpg"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:14.765844+00:00"
content_hash: "52089d14f9a92ba7f3fc6c1eaeb80e7a6fcf07adde77c16ecab065429c96adb3"
---

# Migration With an External Database

The following steps cover migrating data from a Software Risk Manager system installed
with the native installer to an existing Docker Compose deployment.

**To migrate data from a Software Risk Manager system installed using the native installer:**

1. Verify that your Software Risk Manager deployed with Docker Compose is running and
   using the docker-compose-external-db.yml file. The external database details will
   need to be added to this file.

   From the root of the project, the
   `up` command should look as follows:

   ```
   docker-compose -f docker-compose-external-db.yml up
   ```
2. Verify that your Software Risk Manager deployed with the native installer is
   running.
3. Verify that the version numbers of both systems match.
4. Log on to your source Software Risk Manager server whose data you want to
   migrate.
5. Run `mysqldump` to create a backup file. You can run the following
   command to create a dump-srm.sql file after specifying the parameters that work
   for your database.

   ```
   mysqldump --host=127.0.0.1 --port=3306 --user=root -p codedx -r dump-srm.sql
   ```

   Note: The
   above command uses a database named codedx. Older versions of Software Risk
   Manager may use a database named bitnami_codedx.
6. You may encounter an issue running SRM if the database dump file makes use of
   DEFINER. Run the following command with dump-srm.sql replaced with the path of your
   database dump file. This will overwrite the existing database dump file with the
   definers removed.

   ```
   (Get-Content "dump-srm.sql") -replace '\sDEFINER=`[^`]*`@`[^`]*`','' | Out-File dump-srm.sql
   ```
7. Return to the system running Software Risk Manager with Docker Compose, change
   directory to this repository (srm-docker folder), and run the migrate-data.ps1
   script with the following commands. The script will guide you through the rest
   of the procedure.

   ```
   cd /path/to/srm-docker
   pwsh ./admin/migrate-data.ps1 -externalDatabase
   ```

   Note: The above
   command will use the default values for the script parameters
   -tomcatContainerName (srm-docker-codedx-tomcat-1) and dbName (codedx). You
   can find your Docker container names by running docker ps.

Your script output should look similar to the following:

```
pwsh ./admin/migrate-data.ps1 -externalDatabase
Enter the path to your Software Risk Manager AppData folder: /path/to/codedx
VERBOSE: Checking appdata path...
VERBOSE: Checking appdata/analysis-files path...
VERBOSE: Checking PATH prerequisites...
VERBOSE: Checking running containers...
            
Since your SRM deployment uses an external database (one that you maintain on your own
that is not installed or updated by the SRM deployment script), you must restore the dump-srm.sql file you
created in Step 5 of the migration instructions.
            
You can restore mysqldump files using a command that looks like this:
            
mysql -uroot -p srmdb < dump-srm.sql
            
Note: Replace 'root' and 'srmdb' as necessary.
            
VERBOSE: Deleting directories...
VERBOSE: Deleting directory /opt/codedx/analysis-files...
VERBOSE: Deleting directory /opt/codedx/keystore...
VERBOSE: Deleting directory /opt/codedx/mltriage-files...
VERBOSE: Copying directories...
VERBOSE: Copying directory /path/to/codedx/analysis-files to /opt/codedx/analysis-files...
VERBOSE: Copying directory /path/to/codedx/mltriage-files to /opt/codedx/mltriage-files...
VERBOSE: Restarting Software Risk Manager...
Restarting srm-docker-codedx-tomcat-1 ... done
Done
```
