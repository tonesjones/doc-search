---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "FD6xX4Qv59DNYK32FL02ZA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:16.599323+00:00"
---

# Description

Important:
If Coverity Connect is deployed in the cloud, refer
to the section Coverity tools in a Coverity cloud deployment in the
Coverity 2026.6.0 Cloud Deployment Administrator and User Guide.

The `cov-archive` commands allow you, the system administrator, to
export a set of streams into an archive file and optionally delete the exported
streams, import streams from an archive, or get information about an archive file
(its identifier, version, the date and time of creation, the streams contained, and
so on) or a cluster config file (the identifier of the corresponding archive file,
the identifier of the corresponding Coverity Connect coordinator, the date and time
of creation). You can also get help about `cov-archive` command options.

You can import an archive into a Coverity Connect instance that has the same or a
newer version as the Coverity Connect instance used to create the archive.
You can check the Coverity Connect version used to create the archive using the
cov-archive list command.

The `cov-archive` command generates a log file,
<CC_install_dir>/logs/cov-archive.log.

Important:
You can use the import-streams command of
`cov-archive` only while Coverity Connect is in maintenance mode.
You can run the export-streams command while Coverity Connect is operational.

Important:
The command import-streams has exactly two
outcomes: It either completes successfully, or it fails without making any observable
changes to the Coverity Connect database:

- If the command completes without reporting an error, then the outcome is success.
- If the command reports an error, then the outcome might be either success
  or failure. In the majority of cases the reported error means that the
  command failed, but in some rare cases (for example, if the command
  issued a commit but did not receive a response for some reason) the only
  way to tell whether the outcome is success or failure is by checking
  whether the database contains a stream from the archive, or not. Such
  checking can be done by executing the command again—if the first command
  succeeded, then the second one fails by reporting that the streams
  already exist.

## The 2026.6.0 release introduces the BIS (Binary Import/Streaming) archive format

`cov-archive export-streams` now produces archives in BIS (binary)
format instead of the previous ZIP/CSV format. BIS archives are:

- Significantly smaller: BIS stores data using more compact binary encoding as
  opposed to CSV text strings.
- Faster to import: BIS streams a binary copy directly into the PostgreSQL
  database.
- Self-describing: BIS contains schema version metadata that can be read
  without a database connection.

The `cov-archive import-streams` command automatically detects the
archive format and handles both BIS and legacy V1 ZIP/CSV archives transparently. No
flag changes are required for existing import or export workflows.
