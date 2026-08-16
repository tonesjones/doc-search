---
title: "Important notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/important-notes.html"
content_id: "tFaIEWHqHov7wr2Y1qzIkA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:14.131098+00:00"
---

# Important notes

- Do not perform any data definition language (DDL) or data manipulation
  language (DML) operations on the content of a Coverity Connect database
  unless Coverity Support specifically instructs you to do so. Otherwise, all
  of your Coverity Connect data may become unusable and unrecoverable.

  DDL operations include SELECT, UPDATE, INSERT, or DELETE. DML operations include DROP INDEX,
  CREATE INDEX, DROP TABLE, CREATE TABLE, CREATE FOREIGN KEY, and others. This
  restriction applies whether you are using an embedded or external
  database.
- Coverity Support will not assist you in the recovery of data that gets corrupted
  by a DDL database update.
- Use the backup and restore solution selected by your company to backup and
  restore an *external* PostgreSQL database in a stand-alone
  deployment.
- Backups can take a long time for large databases. In addition to using the
  `--dir` option to create directory backups, it is
  recommended that you place the backup file or directory on a device with
  fast read/write speeds (such as a solid state disk). The use of a fast file
  system is also recommended as it may affect performance when dealing with a
  large number of files.
- Restores can also take a long time. Backup files, databases, or directories
  can be restored more quickly if you use a faster file system.
