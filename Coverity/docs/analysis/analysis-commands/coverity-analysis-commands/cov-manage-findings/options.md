---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "UqEpvO713agslO~db~9ksw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:56.662329+00:00"
---

# Options

--action <action>
:   Specifies the action to perform. These are the possible values:

    - `readFromConnect` - Scans the intermediate directory
      and analyzes findings data for the specified stream, retrieves the
      priority filter for the specified stream from Coverity Connect (if
      one exists), applies the priority filter to the findings data, and
      generates a findings report.

      To get started, use this action to generate an initial priority filter. If Coverity
      Connect does not have a priority filter, this action generates a
      findings report containing a blank priority filter.
    - `readFromReport` - Scans the intermediate directory
      and analyzes findings data for the specified stream, applies the
      specified priority filter, and generates a findings report.
    - `sendToConnect` - Sends the specified priority filter
      to Coverity Connect. This action overwrites any existing priority
      filter for the specified stream.

    This option is required.

--dir <intermediate_directory>
:   Path name to an intermediate directory that is used to store the results of
    the build and analysis. This option is required.

--help

-h
:   Prints a usage message to the command console, then exits.

--password <password>

-pa <password>
:   You should use the `--url` option instead of this option.
    This option is deprecated and will be removed in a future release.

    Specify the password for either the current user name, or the user
    specified with the `--user` option. For security reasons,
    the password transmitted to Coverity Connect is encrypted. If
    unspecified, the default is (in order of precedence):

    1. The password from the `--url` option.
    2. The password element from the XML configuration file.
    3. The environment variable `COVERITY_PASSPHRASE`.
    4. The password in the file pointed to by the environment variable
       `COVERITY_PASSPHRASE_FILE`.

    Note: The passphrase can be stored in a file without any other
    text, such as a newline character.

    Attention: On multi-user systems, such as Linux, users can see
    the full command line of all commands that all users execute. For
    example, if a user uses the `ps -Awf` command,
    identifying information such as usernames, process identities, dates and
    times, and full command lines display.

--priority-filter <priority_filter_path>
:   Path to the Microsoft Excel file that contains the priority filter. This option is required when
    `--action` is set to `readFromReport` or
    `sendToConnect`. You can specify an absolute or relative
    path. You must specify the filename as part of the path.

--report <findings_report_path>
:   Path in which to generate the findings report. This option is required when
    `--action` is set to `readFromReport` or
    `readFromConnect`. You can specify an absolute or
    relative path. The directory must already exist. The path must include the
    findings report filename with file extension `.xlsx`.

--stream <stream_name>
:   Name of the Coverity Connect stream with which the priority filter is or will be associated. This
    option is required when `--action` is set to
    `readFromConnect` or `sendToConnect`.

--url <Connect_URL>
:   URL of the Coverity Connect server. This option is required when `--action` is set
    to `readFromConnect` or `sendToConnect`.

--user <username>
:   A Coverity Connect username. This option is required when `--action` is set to
    `readFromConnect` or `sendToConnect`.
