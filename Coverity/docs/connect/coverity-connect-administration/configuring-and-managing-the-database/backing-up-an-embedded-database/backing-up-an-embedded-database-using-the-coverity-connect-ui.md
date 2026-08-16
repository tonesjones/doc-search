---
title: "Backing up an embedded database using the Coverity Connect UI"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/backing-up-an-embedded-database-using-the-coverity-connect-ui.html"
content_id: "7tkbQEEq905uc4qlfnbTUA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:19.874000+00:00"
---

# Backing up an embedded database using the Coverity Connect UI

The Coverity Connect Configuration menu provides a menu item for making or scheduling a
backup of the current state of your database. This feature only supports backing up an
embedded database. External database backup is not supported by this feature.

Note: If Coverity Connect is running on a Windows computer as a service, it will not be able
to backup to a drive letter. Drive letters are mapped on a per-user basis and the local
service user does not have the mappings. It can, however, backup to volumes using UNC
paths. For example:

`\\server\volume\path\to\backup`

Note: You cannot use the Connect UI to back up an external database.

**To make or schedule a database backup in a stand-alone deployment:**

1. Before you perform or schedule a backup, enter the directory location in which
   you want the backup to be saved. The default directory is:

   <install_dir>/backup

   When the backup completes, the backup file is saved with the following naming
   convention:

   <date>,<time>.backup.
2. Do one of the following:

   - To perform a backup, click the Backup Now
     button.
   - To schedule a backup, choose one or more days and set the time of the
     backup and click Done.

   When the backup is started without any errors, Coverity Connect displays a
   Success message.
