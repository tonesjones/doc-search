---
title: "Upgrade Prerequisites for standalone deployments"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upgrade-prerequisites-for-standalone-deployments.html"
content_id: "Qwxiqtn0MlMCs_9FF1MdrA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:29.689069+00:00"
---

# Upgrade Prerequisites for standalone deployments

Make sure the instance you want to upgrade meets the following prerequisites:

- **Important:** Make sure you are not running anti-virus software on a system
  with a Coverity Connect database because it impacts performance and can even
  interfere with correct functioning of the database, possibly including data
  corruption. If you must run anti-virus software, disable it for the duration of
  the upgrade or exempt the
  <cc_install_dir>/<database> directory from
  anti-virus inspection.
- Make sure there is sufficient free space in these locations:
  - The location for the backup if one is needed
  - The volume where the new instance will be installed (if you are not
    doing an In-place upgrade)

  The free space should be roughly 4x the size of the database, as
  determined by the size of the
  <cc_install_dir>/<database> directory’s
  contents.
- Make sure you have enough disk space for the upgrade.
- Make sure that you have the following information prior to launching the installer:
  - Existing Coverity Connect installation directory
  - Destination installation directory (if you plan to perform a
    Backup-and-restore or Intermachine upgrade)
  - Desired backup directory location (if you plan to create a database
    backup)
  - Location of your Coverity Connect license file
  - Desired ports for Coverity Connect communications (for
    Backup-and-restore and Intermachine upgrades)
- When upgrading from PostgreSQL 16 to PostgreSQL 18, make sure that OpenSSL 3 is
  installed. This requirement applies to classic external deployments only.
