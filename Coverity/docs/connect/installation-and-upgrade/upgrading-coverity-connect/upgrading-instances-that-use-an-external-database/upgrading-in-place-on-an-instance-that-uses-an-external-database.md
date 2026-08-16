---
title: "Upgrading in place on an instance that uses an external database"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upgrading-in-place-on-an-instance-that-uses-an-external-database.html"
content_id: "NKrxGYPYjmyPDTU0o6rYCA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:36.549957+00:00"
---

# Upgrading in place on an instance that uses an external database

In addition to creating a separate Coverity Connect instance, this procedure requires you
to upgrade your external database before running the installer to complete the
upgrade.

To perform an in-place upgrade on an instance that uses an external database:

1. If you need to upgrade PostgreSQL support, perform the following steps.

   Note:
   Currently supported PostgreSQL versions are listed in PostgreSQL supported versions.

   1. Either put Coverity Connect into maintenance mode or stop Coverity Connect
      completely.
      - Use the `cov-im-ctl maintenance`
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
      - Use the `cov-im-ctl stop` command to stop
        Coverity Connect:

        **For Linux:**

        ```
        > <OLD_cc_install_dir>/bin/cov-im-ctl stop
        ```

        **For Windows:**

        ```
        > <OLD_cc_install_dir>\bin\cov-im-ctl.exe stop
        ```
   2. Upgrade your external database manually.

      Note: PostgreSQL 16.9 or a later version is preferred. The minimum requirement is PostgreSQL
      16.9.

      For more
      information, see the documentation at <http://www.postgresql.org/docs/9.5/static/upgrading.html>.
2. If you want to modify the SSL configuration, you
   might need to provide the root certificate and/or the client certificate, client
   certificate key, and key password, depending on the authentication method you
   choose during the upgrade procedure. For more information, see Step 2 "Record
   the following information prior to configuring Coverity Connect" in Using an external PostgreSQL database with Coverity Connect.
3. Download and run the Coverity Platform installer for your operating system to
   install the upgraded version of Coverity Connect in the same location as the
   previous version.

   Important:
   When running the installer, it is important to select the
   new, upgraded version of your external PostgreSQL database.
   We recommend that you use the most recent version available.

   For more complete details, see the installation instructions in Installing Coverity Platform components.
