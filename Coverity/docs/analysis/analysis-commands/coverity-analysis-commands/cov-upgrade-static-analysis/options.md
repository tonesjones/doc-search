---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "ju~j21cRKMDihyDGACtYzw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:42:52.577721+00:00"
---

# Options

## Basic options

--old-config <file>
:   The location of an old Coverity Analysis non-default configuration file
    (coverity_config.xml) that for the old release.
    Specifying the path to all configuration files referenced on a typical
    command line to the old release allows the upgrade to re-write any
    configuration files that are relevant when invoking the programs in the
    new release. Repeat this option for each configuration file.

--old-release <dir>

-or <dir>
:   The location of the old Coverity Analysis release. This should be the
    full path to the directory containing the version file, which may be the
    textual VERSION file, the XML
    VERSION.xml file, or both.

--use-existing-release
:   Upgrade an existing Coverity Analysis release in-place.

    Do not use this option if you are upgrading to the current version of
    Coverity Analysis .

--use-new-release
:   Copy settings and the database from the old Coverity Analysis release to
    the new release. Leave the old release untouched. Note that any files in
    the old release that were added by the user are added to the new release
    automatically when the upgrade is complete. This is the preferred mode
    of operation.

## Other options

--help

-h
:   Prints a usage message to the command console, then exits.

--log <file>
:   The absolute path and file name for where to save the upgrade log. The
    default log file is
    <install_dir>/bin/coverity_upgrade.log.

--pedantic
:   If the command returns with warnings, return a non-zero exit code. The
    default behavior is to return non-zero codes only when there are
    errors.
