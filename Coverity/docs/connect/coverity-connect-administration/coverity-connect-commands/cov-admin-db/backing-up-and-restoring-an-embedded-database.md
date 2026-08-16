---
title: "Backing up and restoring an embedded database"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/backing-up-and-restoring-an-embedded-database.html"
content_id: "gXLX2xmP7rh1q_bGoUBdWQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:11.565719+00:00"
---

# Backing up and restoring an embedded database

Use the `backup` and `restore` subcommands to back up and restore
your database.

Important:
The `cov-admin-db backup` and
`cov-admin-db restore` commands work with only an embedded database.
Do not use them with an external database.

**cov-admin-db backup**

```
cov-admin-db backup 
    [<file_or_dir>] 
    [--force] 
    [--no-overwrite] 
    [-j <number_of_processors>] 
    [--debug]
```

**cov-admin-db restore**

```
cov-admin-db restore 
    [<file_or_dir>]
    [--force] 
    [--no-overwrite] 
    [-j <number_of_processors>] 
    [--debug]
```

- `backup` backs up the database to an archive file or directory.
- `restore` restores data to the embedded database, using the
  specified archive file or directory. Before you use this subcommand, run the
  `cov-im-ctl maintenance` command.

  In addition to restoring the data, this command upgrades the schema to make the
  schema compatible with the current version of Coverity Connect. The archive file
  is not modified during this process.

  CAUTION:

  Use caution when restoring a database with this command because
  it deletes all data from the current database.

With both backup and restore, you have a choice of two different formats: a file or a
directory. Files are both more convenient to work with than directories and faster for
backups and restores.

## Options

<file or dir>
:   With `Backup`: The directory where you want the database backed up.

    With `Restore`: The directory from which data is
    restored to the database.

--force
:   Suppresses user inputs during the backup and restore process to help
    automate the procedure.

--no-overwrite
:   Specifies that the following will not be overwritten:

    - An existing backup file with the backup command
    - The contents of a database with the restore command

    If you do not specify this option, you must manually answer the questions
    during the backup/restore process. All questions are skipped if
    `--force` is present.

-j number_of_processors
:   Use with either subcommand to control the level of parallelism and reduce
    the amount of time for the operation. The
    number_of_processors attribute sets the number of
    core processors available on your system.

    This setting has no effect for file backup/restore. It defaults to 4 for
    directory-based backup/restore. 2 or 3 is recommended.
