---
title: "Restoring a Backup"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/restoring-a-backup.html"
content_id: "VbXNbWz8XRykZTC1qrwE5Q"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:11.728250+00:00"
content_hash: "547398605abaf73b381f3f0ad5652628ad122c998ffa66a3b38c12c268cbe6d8"
---

# Restoring a Backup

You can use the included `restore.ps1` script in your
`srm-docker/scripts` folder to restore a backup created by
`backup.ps1`. This will restore Software Risk Manager data from a provided
backup name that was either specified or generated when creating the backup.

**To restore a backup:**

1. Stop your containers using the Docker Compose `down` command for your
   deployment to avoid unexpected restore behavior.
2. Run the following command to restore a backup by entering its name from the list of
   backups:

   ```
   pwsh ./scripts/restore.ps1
   ```

   Note: You
   can use the `-BackupName` parameter to skip the backup list by specifying
   a specific backup.
3. Verify that you see the following message indicating a successful restore:

   ```
   Successfully restored backup <backup-name>
   ```
4. If you are using an external database, restore the related database backup now.

The restore command assumes no defaults have been changed about the Software Risk Manager
Docker Compose environment. If defaults were modified or for more advanced usages of the
restore script, see the help information provided by running the following command from the
`srm-docker` directory:

```
pwsh -Command get-help .\scripts\restore.ps1 -full
```
