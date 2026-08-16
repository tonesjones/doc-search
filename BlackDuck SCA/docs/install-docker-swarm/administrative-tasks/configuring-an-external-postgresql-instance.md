---
title: "Configuring an external PostgreSQL instance"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-an-external-postgresql-instance.html"
content_id: "o_AtZwYoAxgoxglnl47~9Q"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:52.443156+00:00"
---

# Configuring an external PostgreSQL instance

Black Duck SCA supports using an external PostgreSQL instance. Please refer to
[PostgreSQL Version Upgrade Schedule](https://docs.blackduck.com/access?ft:originId=f598e2689f20062534e28c8999b4550b/4d4ac073563d23104e9e1d3c2f88a25e.topic) for more
information regarding supported PostgreSQL versions in Black Duck SCA.

Note: If you are installing using Azure PostgreSQL, a database administrator will need to enable
installation of the hstore PostgreSQL extension before installing or upgrading to
2023.4.0 or later. Additionally, ensure that the `azure.extensions` value
includes both `pgcrypto` and `hstore` to allow init
scripts to access the Azure database.

To configure an external PostgreSQL database:

1. Initialize the external PostgreSQL cluster with the UTF8 encoding. The method to
   accomplish this might depend on your external PostgreSQL provider. For example,
   when using the PostgreSQL initdb tool, run the following command:

   ```
   initdb --encoding=UTF8 -D /path/to/data
   ```
2. Create and configure database usernames and passwords. There are three users for the
   PostgreSQL database: an administrator (by default, **blackduck** is the
   username), a user (by default, **blackduck_user** is the username), and a user
   for the Black Duck reporting database (by default, **blackduck_reporter** is the
   username). You can:
   - Create accounts with the default
     usernames.
   - Create accounts with custom
     usernames.
3. Configure the PostgreSQL instance.

Creating and configuring accounts using default usernames:

Use these instructions to use the default **blackduck**, **blackduck_user**, and
**blackduck_reporter** usernames.

After completing these steps, go to Configuring the
PostgreSQL instance.

1. Create a database user named **blackduck** with administrator privileges.

   For Amazon RDS, set the "Master User" to **blackduck** when creating the
   database instance.

   No other specific values are required.
2. Replace the following in the `external-postgres-init.pgsql` file in the
   `docker-swarm`

   directory.

   Replace `POSTGRESQL_USER` with `blackduck`

   Replace `HUB_POSTGRES_USER` with `blackduck_user`

   Replace `BLACKDUCK_USER_PASSWORD` with the password that you use
   for `blackduck_user`

   Important: This step is mandatory.
3. Run the `external-postgres-init.pgsql` script, located in the
   `docker-swarm` directory, to create users, databases, and
   other necessary items. For example:

   ```
   psql -U blackduck -h <hostname> -p <port> -f external-postgres-init.pgsql postgres
   ```
4. Using your preferred PostgreSQL administration tool, configure passwords for the
   **blackduck**, **blackduck_user**, and **blackduck_reporter**
   database users.

   These users were created by the `external-postgres-init.pgsql`
   script in the previous step.
5. Go to Configuring the PostgreSQL
   instance.

Note: Black Duck makes use of the pgcrypto extension and expects it to be available. CloudSQL,
RDS, and Azure provide the pgcrypto extension by default, therefore, no further
configuration is required. Users of community PostgreSQL will need to install the
postgresql-contrib package if it is not already installed. Note that the package name
varies depending upon distribution.

## Creating and configuring accounts using custom usernames and passwords

Use these instructions to create custom database usernames.

In these instructions:

- **DBAdminName** is the new custom administrator's username.
- **DBUserName** is the new custom database user's username.
- **DBReporterName** is the new custom database reporter's username.

User names that consist of numbers only can be used for PostgreSQL user names in external
PostgreSQL instances.

The updated `external-postgres-init.pgsql` script uses double quotation
marks around the user names, so that numeric PostgreSQL user names can run successfully
in the script. In the `external-postgres-init.pgsql` script, you search
and replace the default name values for HUB_POSTGRES_USER and POSTGRESQL_USER with the
numeric user names.

After completing these steps, go to the next section, Configuring the PostgreSQL instance.

1. Create a database user named **DBAdminName** with administrator
   privileges.

   For Amazon RDS, set the "Master User" to **DBAdminName** when creating the
   database instance.

   No other specific values are required.
2. Edit the `external-postgres-init.pgsql` script, located in the
   `docker-swarm` directory with the account names you wish to
   use for **DBAdminName**, **DBUserName**, and **DBReporterName**.
3. Run the edited `external-postgres-init.pgsql` script, located in
   the `docker-swarm` directory, to create users, databases, and
   other necessary items. For example:

   ```
   psql -U DBAdminName -h <hostname> -p <port> -f external-postgres-init.pgsql postgres
   ```
4. Using your preferred PostgreSQL administration tool, configure passwords for the
   **DBAdminName**, **DBUserName**, and **DBReporterName** database
   users.

   These users were created by the `external-postgres-init.pgsql`
   script in the previous step.
5. Edit the `hub-postgres.env` environment file. The file lists the
   default usernames for HUB_POSTGRES_USER and HUB_POSTGRES_ADMIN. Replace these
   default values with your custom usernames for the database user and
   administrator.
6. Go to the next section, Configuring the
   PostgreSQL instance.

## Configuring the PostgreSQL instance

After creating users and configuring passwords, complete these steps:

1. Edit the `hub-postgres.env` environment file, located in the
   `docker-swarm` directory, to specify the database connection
   parameters. You can select to:

   - Enable SSL in database connections.

     For authentication, you can select to use certificate or username and
     password or both.
   - Disable SSL in database connections.

     If SSL is disabled, you must user username and password
     authentication.

   | Parameter | Description |
   | --- | --- |
   | HUB_POSTGRES_ENABLE_SSL | Defines the use of SSL in database connections.  - Set the value to "false" to disable using SSL in   database connections. This is the default value. - Set the value to "true" to enable using SSL in   database connections. |
   | HUB_POSTGRES_ENABLE_SSL_CERT | Defines whether a certificate is required for authentication.  - Set the value to "false" to disable client   certificate authentication. This is the default   value. - Set the value to "true" to require client certificate   authentication when using SSL in database   connections. |
   | HUB_POSTGRES_HOST | Hostname of the server with the PostgreSQL instance. |
   | HUB_POSTGRES_PORT | Database port to connect to for the PostgreSQL instance. |
2. If you are using username and password authentication, provide the PostgreSQL
   administrator and user passwords to Black Duck :

   1. Create a file named HUB_POSTGRES_USER_PASSWORD_FILE with the password for
      the database user. This is the **blackduck_user** username if you are
      using the default username, or **DBUserName** in the previous
      example.
   2. Create a file named HUB_POSTGRES_ADMIN_PASSWORD_FILE with the password
      for the database administrator user. This is the **blackduck**
      username, if using the default username or **DBAdminName** in the
      previous example.
   3. Mount a directory that contains both files to
      `/run/secrets`. Use the
      `docker-compose.local-overrides.yml` file located in
      the `docker-swarm` directory. For each service (webapp,
      jobrunner, authentication, bomengine, and scan), do the following:

      1. If necessary, remove the comment character (#) before the name of
         the service.
      2. Add the volume mount to the service.

      This example adds the volume to the webapp service:

      ```
      webapp: 
       volumes: ['directory/of/password/files:/run/secrets']
      ```

      You would also need to add this text to the authentication, jobrunner,
      bomengine, and scan services.

   Instead of Steps 2a-c, you can use the docker secret command to create a secret
   called HUB_POSTGRES_USER_PASSWORD_FILE and a secret called
   HUB_POSTGRES_ADMIN_PASSWORD_FILE.

   1. Use the docker secret command to tell Docker Swarm the secret. The name
      of the secret must include the stack name. In the following example, the
      stack name is 'hub':

      ```
      docker secret create hub_HUB_POSTGRES_USER_PASSWORD_FILE <file containing password>
      ```

      ```
      docker secret create hub_HUB_POSTGRES_ADMIN_PASSWORD_FILE <file containing password>
      ```
   2. Add the password secret to the webapp, jobrunner, authentication, bomengine, and scan
      services in the `docker-compose.local-overrides.yml`
      file. This example is for the webapp service:

      ```
      webapp:
        secrets:
         - HUB_POSTGRES_USER_PASSWORD_FILE 
         - HUB_POSTGRES_ADMIN_PASSWORD_FILE
      ```

      If necessary, remove the comment characters (#).

      Remove the comment characters and if necessary, change the stack name to
      the text at the end of the
      `docker-compose.local-overrides.yml` file:

      ```
      secrets:
        HUB_POSTGRES_USER_PASSWORD_FILE:
          external: true
          name: "hub_HUB_POSTGRES_USER_PASSWORD_FILE"
        HUB_POSTGRES_ADMIN_PASSWORD_FILE:
          external: true
          name: "hub_HUB_POSTGRES_ADMIN_PASSWORD_FILE"
      ```
3. If you are using certificate authentication, mount a directory that contains all
   certificate files (HUB_POSTGRES_CA (server CA file), HUB_POSTGRES_CRT (client
   certificate file), HUB_POSTGRES_KEY (client key file)) to
   `/run/secrets` in the webapp, jobrunner, authentication, and
   scan services by editing the `docker-compose.local-overrides.yml`
   file located in the `docker-swarm` directory. See the example in
   Step 2c.
4. To be able to use SSL with certificate *and/or* username/password
   authentication, set HUB_POSTGRES_ENABLE_SSL_CERT to "true" and complete steps 2
   *and* 3.
5. Install or upgrade Black Duck.
