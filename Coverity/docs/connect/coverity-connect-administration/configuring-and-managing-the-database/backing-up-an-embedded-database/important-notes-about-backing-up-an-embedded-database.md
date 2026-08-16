---
title: "Important notes about backing up an embedded database"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/important-notes-about-backing-up-an-embedded-database.html"
content_id: "EnUBOztyZ0AYXsjx~Kr5Sg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:19.254283+00:00"
---

# Important notes about backing up an embedded database

- Commit and backup can now run in parallel. There is no risk to the backup if a
  commit is in progress while the backup occurs. If restored, such a backup will
  show a partial commit, which will be removed by the next commit to the affected
  stream.
- Backups work the same whether performed using the Coverity Connect UI or the
  command line.
- The backup does not store a property that is used by Coverity Connect to retain passwords set up
  for Coverity Connect email or for LDAP or Jira integrations. If you are using
  any of these features, you should keep a backup of the
  `cim.ldap.key` value (in
  <install_dir>/config/cim.properties) in an
  accessible location. Otherwise, you will need to re-enter the passwords if you
  need to restore a backup of the database to a different instance of Coverity
  Connect.
- Any errors are written to cim.log. Within the file, backup
  statements are denoted by BackupJob.
