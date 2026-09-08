---
title: "Restoring to a Previous Version"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/restoring-to-a-previous-version.html"
content_id: "AD5zlN557R0h7W3x2oQt1Q"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:04:58.948808+00:00"
content_hash: "4e046fca015024bf1f622664d9a639fc6680b5b588e6136afb5ed859802f519f"
---

# Restoring to a Previous Version

In your backup folder, there’s a file called `restore-backup`, which is
used to restore to a previous version of Software Risk Manager.

## Windows

1. Navigate to the backup folder, which is in the installation folder that you
   provided during installation. The default folder is `C:\Program
   Files\Software Risk Manager\backup-<timestamp>\` where
   `<timestamp>` is the date and time the upgrade was
   performed.
2. Right-click on `restore-backup.bat` and choose "Run as
   administrator."

## Linux Root Installation

1. Navigate to the backup folder that was created during the upgrade process. The
   default folder is `/opt/srm/backup-<timestamp>/` where
   `<timestamp>` is the date and time the upgrade was
   performed.
2. Open a terminal and run `sudo chmod +x
   restore-backup.sh`.
3. Run `sudo ./restore-backup.sh`.

## Linux Non-Root Installation

1. Navigate to the backup folder that was created during the upgrade process. The
   default folder is `/home/srm/backup-<timestamp>/` where
   `<timestamp>` is the date and time the upgrade was
   performed.
2. Open a terminal and run `chmod +x restore-backup.sh`.
3. Run `./restore-backup.sh`.
