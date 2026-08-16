---
title: "Upgrading with backup-and-restore on an instance that uses an external database"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upgrading-with-backup-and-restore-on-an-instance-that-uses-an-external-database.html"
content_id: "3UCqXuSoxQrwELFHtfkD9A"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:37.163094+00:00"
---

# Upgrading with backup-and-restore on an instance that uses an external database

This procedure requires you to create a new external database and to manually restore
your old external database into it. You will also upgrade the database schema
manually.

1. If you are backing up and restoring a version of Coverity Connect that has
   configured Coverity Connect email or set up an LDAP or Jira integration, you should
   save a copy of the `cim.ldap.key` value found in the
   cim.properties file now.

   Later in this procedure, you
   will supply this value to the new Coverity Connect instance you create in order
   to preserve any email, Jira, or LDAP passwords that were set up in the old
   Coverity Connect instance. Note that if this value is not available for some
   reason, you can simply provide the passwords to the new Coverity Connect
   instance after completing the upgrade.
2. If you want to modify the SSL configuration, you
   might need to provide the root certificate and/or the client certificate, client
   certificate key, and key password, depending on the authentication method you
   choose during the upgrade procedure. For more information, see Step 2 "Record
   the following information prior to configuring Coverity Connect" in Using an external PostgreSQL database with Coverity Connect.
3. Use the following steps to back up your external database in
   preparation for the upgrade:
   1. Use the `cov-im-ctl maintenance`
      command to put your existing Coverity Connect instance into maintenance
      mode.

      **For Linux:**

      ```
      > <OLD_cc_install_dir>/bin/cov-im-ctl maintenance
      ```

      **For Windows:**

      ```
      > <OLD_cc_install_dir>\bin\cov-im-ctl.exe maintenance
      ```
   2. Using your preferred method, create a backup of the external database that
      you are using with Coverity Connect.

      You will use the backup file later in
      the upgrade procedure.
   3. Use the `cov-im-ctl stop` command to stop
      Coverity Connect:

      **For Linux:**

      ```
      > <OLD_cc_install_dir>/bin/cov-im-ctl stop
      ```

      **For Windows:**

      ```
      > <OLD_cc_install_dir>\bin\cov-im-ctl.exe stop
      ```
   4. (Optional) Use the `cov-im-ctl status` command to verify
      the status:

      **For Linux:**

      ```
      > <OLD_cc_install_dir>/bin/cov-im-ctl status
      ```

      **For Windows:**

      ```
      > <OLD_cc_install_dir>\bin\cov-im-ctl.exe status
      ```
   5. Stop the external database that was running with Coverity Connect.
   6. (Windows only)

      If you are running Coverity Connect as a service, you must
      remove the service from the
      <OLD_cc_install_dir>\bin directory. To do
      so, run the following command as Administrator:

      ```
      > sc delete cov-im-service
      ```
4. Use the following commands to create a *new* PostgreSQL
   database into which you will later restore the backup. The
   `username`, `host`, `port`, and
   `db` (cim) options use values for a default Coverity Connect
   installation with an embedded database.
   1. `pg_dump --no-owner --no-acl --host localhost --port=5432 -username
      coverity -Fc -f <filename> cim`
   2. `dropdb -host localhost --port=5432 -username=coverity
      cim`
   3. `createdb -host localhost --port=5432 -username=coverity -T template0
      cim`

   For more information about creating an external database, see Using an external PostgreSQL database with Coverity Connect. For
   supported versions, see PostgreSQL supported versions.
5. Download and run the Coverity Platform
   installer for your operating system to create a new instance of Coverity Connect
   that uses your newly created external database.

   Important: When running
   the installer, select your newly created external database, not the old external
   database. Later in this upgrade procedure, you will restore your backup into
   this empty database.
6. Use the following steps to restore the backup of your old database into
   the new database.

   Note: At this point, your new database should still be
   empty.

   1. Stop your *new* database.
   2. `dropdb -host localhost --port=5432 -username=coverity
      cim`
   3. `createdb -host localhost --port=5432 -username=coverity -T template0
      cim`
   4. Restore the previously created backup to the new Postgres format using a
      tool such as `psql` or `pg_upgrade`. For more
      information, see the documentation at <http://www.postgresql.org/docs/9.5/static/upgrading.html>.

      For compatibility settings,
      see:

      <http://www.postgresql.org/docs/9.5/static/runtime-config-compatible.html>.
   5. Restart the new database.

      It now contains the data from your old
      database.
7. Use the following steps to upgrade your database schema.
   1. Put your new Coverity Connect instance into maintenance mode.

      **For
      Linux:**

      ```
      > <NEW_cc_install_dir>/bin/cov-im-ctl maintenance>
      ```

      **For Windows:**

      ```
      > <NEW_cc_install_dir>\bin\cov-im-ctl.exe maintenance>
      ```
   2. Upgrade the PostgreSQL schema with the `cov-admin-db upgrade-schema`
      command.

      **For Linux:**

      ```
      > NEW_cc_install_dir/bin/cov-admin-db upgrade-schema
      ```

      **For Windows:**

      ```
      > NEW_cc_install_dir\bin\cov-admin-db.exe upgrade-schema
      ```

      For more information about `cov-admin-db upgrade-schema`, see the
      Coverity 2026.6.0 Command Reference.
8. If you saved a copy of the `cim.ldap.key` value in the first step,
   copy it over to the cim.properties file for your new Coverity
   Connect instance.

   The value you copied over should replace the
   `cim.ldap.key` value that was automatically generated when
   you installed the new Coverity Connect instance.

   This step will prevent
   the need to reset passwords for your Coverity Connect email, Jira plugin, and/or
   LDAP server functionality through the Coverity Connect configuration screens
   after you restart your new Coverity Connect instance.
9. Restart the new Coverity Connect instance:

   **For Linux:**

   ```
   > NEW_cc_install_dir/bin/cov-im-ctl start
   ```

   **For Windows:**

   ```
   > NEW_cc_install_dir\bin\cov-im-ctl.exe start
   ```
10. After integrating the upgraded Coverity Connect into your production environment,
    you can remove or archive the old instance.

Note: The backup-and-restore upgrade does not transfer certificates that are associated with SSL,
settings related to SSL, or custom settings that you might have made to certain files in
your installation directory. If you need to perform a backup-and-restore upgrade, you
can file a support ticket here: <https://community.blackduck.com/s/contactsupport>.
