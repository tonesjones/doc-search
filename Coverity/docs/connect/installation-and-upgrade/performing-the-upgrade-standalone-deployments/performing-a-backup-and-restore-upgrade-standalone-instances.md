---
title: "Performing a backup-and-restore upgrade (standalone instances)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/performing-a-backup-and-restore-upgrade-standalone-instances-.html"
content_id: "fe5qb7X~DqxzX3rAUZsQUg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:30.950114+00:00"
---

# Performing a backup-and-restore upgrade (standalone instances)

This section describes how to perform a backup-and-restore upgrade on a Coverity Connect
standalone instance that uses an embedded database.

Note:

- This type of upgrade does not affect your truststores, keystores, or
  certificates. You can continue using them without modification.
- Make sure you have read the preceding sections in this chapter before proceeding. You can
  skip "Performing an in-place upgrade".
- A backup-and-restore upgrade might fail if the path to the
  `cov-platform` installation directory is overly long. As
  reference, an upgrade on Windows can succeed with paths up to 107 characters,
  including slash characters. On Linux, 85 characters might be too long. This
  restriction is due to PostgreSQL.
- On Linux systems, do not attempt to perform the upgrade while logged in as
  root.
- Make sure you know the location for the new Coverity Connect installation
  directory prior to launching the installer.

**To perform a backup-and-restore upgrade on a standalone instance that uses an embedded
database:**

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
4. Complete the installation process:
   1. Select and accept the license agreement for your region of the world.
   2. Select the **Backup-and-restore** option.
   3. Follow the prompts, selecting the **Automated backup and non-database
      gathering** option when it becomes available to you.

      Important: When you are prompted to choose a
      performance configuration, you can choose Production or Restore. If you choose
      Production, the installer runs `cov-admin-db tune`. This can
      improve Coverity Connect performance by re-tuning database performance. If you
      choose Restore, the installer does not run `cov-admin-db tune`.
      For details about `cov-admin-db
      tune`, see the Coverity 2026.6.0 Command Reference.
5. Copy modifications from your old to your new `server.xml` file.

   If
   you made any modifications to the `<install_dir>/server/base/conf/server.xml`
   file of your existing installation (for example, if you modified the
   `keystoreFile` or `keystorePass` properties),
   copy those modifications to your new installation.

   Note: Copy only the
   modifications; do not overwrite the entire file.
