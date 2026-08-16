---
title: "Preparing the Connect database to send to Black Duck"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/preparing-the-connect-database-to-send-to-black-duck.html"
content_id: "JizsaAkW6QM9i~pondLpdg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:13.434382+00:00"
---

# Preparing the Connect database to send to Black Duck

You might need to send a backup of your Connect database to Coverity support. You have
two options for doing so securely:

- Remove the source code from the database before sending. Your Support
  representative can explain how you do that.
- Anonymize the database.

  This operation, called *scrambling*, not only removes source code, but
  destroys all names of items in the database (for example, users, components, and
  streams), replacing them with small numbers. Because the data is overwritten,
  there is no way to "un-scramble" a scrambled database.

Scrambling has disadvantages:

- It takes longer than removing source.
- Depending on the problem that Support needs to diagnose, you might need to work with
  Support to match a few of the scrambler-generated numbers to their unscrambled
  names.

Use the `scramble` subcommand to anonymize your database before sending
it to Coverity Support. This command works with all supported Coverity Connect version backups.

Note: The database scramble tool is not supported with Coverity cloud
deployments.

The syntax of the `scramble` command is as follows:

```
cov-admin-db scramble 
    --input-dump <file_or_dir> 
    --output-dir <output_dir> 
    [--debug]
```

Use the `--input-dump` option to specify the name of the input backup file or
directory. This is the file you want scrambled. The output of the scrambling operation
is a database backup directory, <output_dir>.

The basic workflow is as follows:

1. Run the `cov-admin-db backup` command to create a backup of your
   database.
2. To avoid impacting the resources used by your production Connect instance,
   install Connect on a different host. Use the embedded database option when
   installing.
3. On the instance installed above, run the `cov-admin-db scramble`
   command to scramble the database backup.

   The `cov-admin-db scramble` command takes the file or directory
   you provide with the `--input-dump` option, and restores it
   into a temporary database. It then scrambles information in the temporary
   database.
4. The `cov-admin-db scramble` command then backs up the stripped database to the
   directory specified by the `--output-dir` option.
5. You can now make a tar or zip archive of the <output_dir> directory and
   send it to Coverity Support.

Note: Like removing source, scrambling takes significant disk space, both for the two
backups and for the temporary database. The temporary database will consume the same
amount of disk space as the production database.
