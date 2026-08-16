---
title: "Performing an intermachine upgrade (standalone instances)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/performing-an-intermachine-upgrade-standalone-instances-.html"
content_id: "MuUnpQBqj66KRY6AMvT7Sw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:31.565631+00:00"
---

# Performing an intermachine upgrade (standalone instances)

This section describes how to perform an intermachine upgrade on a Coverity Connect standalone
instance that uses an embedded database.

An intermachine upgrade is required if you want to relocate an existing Coverity Connect
instance to a new host machine when you upgrade. Otherwise, perform a backup-and-restore
upgrade or an in-place upgrade. For more information, see Choosing the type of upgrade.

An intermachine upgrade resets the following to their default state (back them up if you want
to retain them):

- Truststores, keystores, and certificates
- The following properties in the `cim.properties` file:
  - `commitPort`
  - `dir.temp`
  - `embeddedDatabase`
  - `maindb.password`
  - `maindb.url`
  - `maindb.user`
- The following properties in the `system.properties` file:
  - `embedded_db`
  - `log_dir`
  - `os_user`
  - `pg_datadir`
  - `pg_port`
  - `service_number`
  - `session_cookie_name`
  - `windows_service`
- The following PostgresSQL database tuning parameters:
  - `autovacuum_max_workers`
  - `checkpoint_segments`
  - `effective_cache_size`
  - `maintenance_work_mem`
  - `shared_buffers`
  - `track_counts`
  - `work_mem`
  - `wal_buffers`

To perform an Intermachine upgrade, you will need to run the installer two times.
The first time you run the installer, use the Upgrade Preparation option to get a backup
of the database and a backup of the non-database state. The second time you run the
installer, use the Intermachine Upgrade option to install the new instance using the
backups from the Upgrade Preparation step. The procedure in this section describes all
of the steps in this process.

**To perform an Intermachine upgrade on a standalone instance that uses an embedded
database:**

Note: On Linux systems, ensure that you are not logged in as root during
the upgrade procedure.

1. Make sure you have full permissions (`rwx`) on the existing
   installation directory and the new installation directory.
2. Download the correct Coverity Platform installer file for your operating system. (The
   Coverity Platform installer installs Coverity Connect.)
3. Run the installer program for your operating system.

   **For Windows,** we recommend that you install Coverity Connect with Windows
   Administrator privileges (installing Coverity Connect as a service requires it).
   To do so, right click the installer and choose Run as
   Administrator.

   **For Linux**, run the installer script in a Bourne shell, for example:

   ```
   > ./cov-platform-linux64-[version].sh
   ```

   Note: Depending on the size of your database, the upgrade process can take a long
   time. If you are performing this operation by way of an SSH terminal, we
   recommend you use a persistent terminal (such as Screen) in case your session is
   interrupted.

   The installer uses a text-based console mode or a graphical mode. The
   installation choices for graphical and console modes are equivalent. To install
   using graphical mode on Linux, append the `–g` option to the
   command above.

   Note that you can change from graphical to silent installer (command line) as described in
   Coverity
   Platform installation modes in the Coverity 2026.6.0 Installation and Upgrade Guide. For details about the silent
   installer options and parameters, see Coverity Connect
   silent installer in the Coverity 2026.6.0 Installation and Upgrade Guide, and in particular the relevant
   sub-section for the upgrade parameters.
4. To update your existing Coverity Connect instance, complete the Upgrade Preparation
   process:

   Note: This part of the process shuts down your Coverity Connect server.
   Plan a maintenance window that covers the remainder of the upgrade
   process.

   1. Select the **Upgrade Preparation** option.
   2. Specify the current Coverity Connect installation directory, and select one
      destination directory for both the database backup and the non-database
      state backup. The backups in this directory will be used to complete the
      upgrade on the destination machine.
5. Complete the Intermachine Upgrade process:
   1. Make sure that the destination machine has access to the backups from the
      previous step. You could do that by sharing the directory containing your
      backups or by copying it over to the destination machine.
   2. On the destination machine, launch the installer and follow the on-screen
      prompts, selecting the **Intermachine Upgrade** option.
   3. Enter your desired installation directory, then specify the location of the
      directory where you saved the database backup file and non-database state
      backup (as part of the Upgrade Preparation step)
   4. Follow the on-screen prompts to complete the upgrade.
