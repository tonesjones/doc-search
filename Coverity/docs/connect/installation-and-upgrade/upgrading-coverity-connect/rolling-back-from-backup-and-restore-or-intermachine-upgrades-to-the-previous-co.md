---
title: "Rolling back from backup-and-restore or intermachine upgrades to the previous Coverity Connect version"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/rolling-back-from-backup-and-restore-or-intermachine-upgrades-to-the-previous-coverity-connect-version.html"
content_id: "py0h0zJ1ZoLTiPsAykvCog"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:40.917260+00:00"
---

# Rolling back from backup-and-restore or intermachine upgrades to the previous Coverity Connect version

After an upgrade is complete, or if an upgrade fails, you can roll back to the previous version
of Coverity Connect.

Note:

- If the same port values were used for both the old instance and the new instance
  of Coverity Connect, only one instance can be running at a time.
- When the Coverity Platform installer attempts to back up an instance of Coverity
  Connect, the installer may display an error message of "Starting the database
  failed" if a different instance that uses the same ports is currently
  running.
- It is assumed that you have not put the new instance into production yet. If you
  have already begun using the new instance, then rolling back will mean using
  Coverity Connect from the point in time when you stopped the old instance and
  thus any commits or changes made to the new instance will not have been applied
  to the old instance.

If the old instance has not been removed since the new Coverity Connect instance was installed
in a new location, the old instance can still be used. Stop the new instance by running
`cov-stop-im`; restart the old instance by running
`cov-start-im`; and you will have rolled back.

If the old instance has been removed but you have already used the Upgrade Preparation
installer type to back up the old instance's internal database, rolling back can be
achieved by reinstalling the previous version with the Intermachine Upgrade installer
type. First, stop the new instance by running `cov-stop-im`. Then,
follow the same process as an Intermachine Upgrade, except:

- Use the installer for the previous version, instead of the installer for the new
  version.
- Make sure that the database backup file was created by the previous Coverity
  Connect version, not by the new version.
- It is recommended that you use a brand new installation directory that had not
  been used by a previous instance.
