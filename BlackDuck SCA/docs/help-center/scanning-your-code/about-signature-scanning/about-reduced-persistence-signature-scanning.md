---
title: "About Reduced Persistence Signature Scanning"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/about-reduced-persistence-signature-scanning.html"
content_id: "KhQ7PgMoNmjbjsfQecoBeA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:41.785297+00:00"
---

# About Reduced Persistence Signature Scanning

In the source view, many users rarely look at unmatched files from signature scanning,
but all of that data is by far the biggest consumer of space in the database.
Performance testing also shows that inserting the file data into the database is a
significant fraction of scan time.

Reduced Persistence Signature Scanning aims to decrease database size and growth and also
increase scan performance by no longer saving data for files that are not matched by
signature scanning. However, if your use case requires that unmatched file data be
saved, there are settings to retain that data available at the global, project, and/or
scan levels.

There is also the option to purge existing unmatched files to further reduce database
disk usage.

## Settings

Unmatched files are no longer retained by default. However, retention policy can be changed.

- **Global setting**. In System Settings under Data Retention, there is an
  option to enable retention of unmatched files. When it is not enabled (the
  default), there is an option to purge all existing unmatched files from all
  projects. The option to purge is not presented if retention is enabled. Note
  that the global setting only applies to projects and scans that do not
  explicitly specify their own setting; similarly, changing the global setting
  does not affect projects or scans that do specify their own setting.
- **Project setting**. The Project Settings tab has similar options to
  enable retention and purge existing unmatched files, except that they only
  apply to files and scans done under the project. Other than scope, the
  primary difference from the global retention setting is that the project
  setting has three possibilities: (1) disabled, (2) enabled, and (3) use the
  global setting (the default). The global setting only affects scans under a
  project when option (3) is selected.
- **Per-scan setting**. Each individual signature scan can specify that
  unmatched files discovered by that scan be retained or not retained; see
  "Scan Options" below. If no retention option is provided by a scan,
  retention is determined by the project or global setting as described
  above.

Note that the determination of whether unmatched files resulting from a scan need to
be retained is made at the beginning of a scan and cannot be changed afterwards.

Warning: Once unmatched files are purged, they cannot be recovered except by
restoring from backup.

## Custom signature matching

When custom signatures are enabled for a project, unmatched files in that project
must be retained for the feature to work so that scans of other projects can match
against them. In such cases, retention is enabled by default and cannot be disabled
unless custom signatures are disabled first.

Note that if a project's custom signature setting is changed from disabled to
enabled, unmatched file retention will automatically be enabled as well. However, if
retention was previously disabled, unmatched files within that project will be
missing, and custom signature matching will not work as expected. In such cases, all
versions in that project will need to be rescanned so that all files can be
retained.

## Scan options

The scan CLI has two new options, `--retain-unmatched-files` and
`--discard-unmatched-files`, which will retain or discard,
respectively, any unmatched files discovered by this scan and this scan only. If
either option is supplied, project and global retention settings are ignored;
otherwise, retention is determined by project or global settings as described in
"Settings". Specifying both options with a single scan is an error.

If scanning with Detect, use one of the following arguments as appropriate:

```
--detect.blackduck.signature.scanner.arguments='--retain-unmatched-files'
```

```
--detect.blackduck.signature.scanner.arguments='--discard-unmatched-files'
```

## Use cases requiring retention

Retention must be manually enabled to support two potential use cases:

1. Snippet-only scans operating on files previously discovered by a signature scan.
   If unmatched files from that signature scan were not retained, the subsequent
   snippet-only scan will be unable to scan them.

   Note: Snippet-only scans require unmatched file retention to be enabled.
2. Workflows requiring unmatched files be examined.

## Temporary retention

Some signature scan options such as snippet matching, license search, and copyright
search will require unmatched files to be retained so that those features can
operate. However, if unmatched file retention was not enabled for such a scan, the
unmatched files will be purged within a short time after the scan is complete.

Note that these temporarily retained unmatched files may be briefly visible in the
source tree view until they are purged.
