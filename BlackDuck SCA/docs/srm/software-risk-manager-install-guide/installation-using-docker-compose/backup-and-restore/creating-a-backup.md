---
title: "Creating a Backup"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/creating-a-backup.html"
content_id: "HnfcEgP7dFBgv82FZz~MqQ"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:10.498434+00:00"
content_hash: "d4ea1f29adcf0aafb114e6b890e6cb363a807154c642f28f9a7092cca9e80d31"
---

# Creating a Backup

Backup instructions will vary based on whether or not you are using an external database. Use
the procedures shown below to create a backup that will include the volume data for your
deployment under the name `my-srm-backup`.

## Backup without an External Database

**To create a backup without an external database:**

1. Stop your containers using the Docker Compose `down` command for your
   deployment.

   ```
   docker-compose -f /path/to/your-docker-compose-file down
   ```
2. Open a terminal window and change the directory to your `srm-docker`
   GitHub repository.

   ```
   cd /path/to/srm-docker
   ```
3. Run the `backup.ps1` script by specifying a backup name (e.g.,
   `my-srm-backup`) and the path to your Docker Compose file.

   ```
   pwsh ./scripts/backup.ps1 -BackupName my-srm-backup -ComposeConfigPath /path/to/your-docker-compose-file
   ```

   Note: Specify
   a project name using the `-p` parameter, if necessary.
4. Verify that you see the following message indicating a successful backup:

   ```
   Successfully created backup <backup-name>
   ```

## Backup with an External Database

**To create a backup with an external database:**

1. Stop your containers using the Docker Compose `down` command for your
   deployment.

   ```
   docker-compose -f /path/to/your-docker-compose-file down
   ```
2. Open a terminal window and change the directory to your `srm-docker`
   GitHub repository.

   ```
   cd /path/to/srm-docker
   ```
3. Run the `backup.ps1` script by specifying a backup name (e.g.,
   `my-srm-backup`), the path to your Docker Compose file, and the name of
   your web volume (you can list volumes with the `docker volume ls`
   command).

   ```
   pwsh ./scripts/backup.ps1 -BackupName my-srm-backup -AppDataVol srm-docker_codedx-appdata-ex-db-volume -ComposeConfigPath /path/to/your-docker-compose-file
   ```

   Note: Specify
   a project name using the `-p` parameter, if necessary.
4. Verify that you see this message indicating a successful backup:

   ```
   Successfully created backup <backup-name>
   ```
5. Back up your external database.
