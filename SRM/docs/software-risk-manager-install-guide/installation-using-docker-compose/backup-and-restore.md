---
title: "Backup and Restore"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/backup-and-restore.html"
content_id: "2hE3gGegUnRirwi6kM4BrA"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:09.257154+00:00"
content_hash: "0f7691f32f3e8a47f273d292c395e81cd47294bfae8eca1aa0f078b8bc111fe3"
---

# Backup and Restore

This section explains how to back up and restore Software Risk Manager using
`backup.ps1` and `restore.ps1` in the `scripts`
directory. Both scripts include a `-p` project name parameter that you should
specify if you used a project name with your Docker Compose `up` command.

The backup script creates a new volume named codedx-backups where each backup gets stored by
name. You can either specify a name or let the backup script generate a name for you formatted
as `backup-{date}-{time}`.

Note: Be cautious of commands such as `docker volume prune`. The volume storing
Software Risk Manager backups is not attached to a container and would be deleted.

For more
information, see the following sections:

- Backup and Restore Prerequisites
- Creating a Backup
- Backup Retention
- Restoring a Backup
