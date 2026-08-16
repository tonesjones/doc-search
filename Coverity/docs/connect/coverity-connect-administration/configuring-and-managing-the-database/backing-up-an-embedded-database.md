---
title: "Backing up an embedded database"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/backing-up-an-embedded-database.html"
content_id: "SMaA5nzvl6sjsd3VBQ9Vtg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:18.632581+00:00"
---

# Backing up an embedded database

This section describes how to backup the embedded PostgreSQL database in a Coverity
Connect *stand-alone deployment*. It covers using the Coverity Connect UI or the
command line to perform or schedule the backup.

Note:

For information specific to backing up databases in *clustered deployments*, see
Managing multiple database instances.

As you would do with any system that contains important data, you should develop a
process for regularly backing-up and restoring the database. The database contains all
of the sensitive data for your system, including source code and defects, so choose an
appropriate location when creating copies for back up purposes.

It is up to you to decide the backup schedule (and this might depend on how large the
database is and how long the backup takes), but it is a good idea to always have a
relatively recent backup. For example, if anything were to go wrong with your system at
some point, you will have a successful backup that you can restore into production. It
is also important to make a backup of your database when you make changes to the system,
such as new feature implementation, major system configuration changes, major tuning
changes, upgrades, and so forth.

Once you have a process for regular backups, you should also implement a process for
periodically testing the backups by attempting to restore them to an instance of the
Coverity Connect server that is the same version the backup was created from. This
practice will verify the media reliability and information integrity in the event
restoring a backup is required.
