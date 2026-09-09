---
title: "Backup Retention"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/backup-retention.html"
content_id: "DjbnYiBiKi~Z2FEOVbghhg"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:11.097030+00:00"
content_hash: "31e8a358cfeea675be57835c7ae12d8de4cdcdcb67fb0b0072e2866db99afdfe"
---

# Backup Retention

Backups will be automatically removed by the backup script if they meet one of the following
criteria:

- **Older than 30 days.** The 30-day default can be changed with the
  `-Retain` backup script parameter, using `-Retain 0` to
  ignore backup age, `-Retain 5` for 5 days, and `-Retain
  10:00` for 10 hours of retention.
- **Exceeds maximum backup count.** By default, a maximum of 10 backups will be stored at
  a time. This can be configured with the `-MaximumBackups` backup script
  parameter.

For more advanced usages of the backup script, such as setting the names of your Tomcat and
DB containers if they are not the default, see the help info via the following command run
from the srm-docker directory:

```
pwsh -Command get-help .\scripts\backup.ps1 -full
```
