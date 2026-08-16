---
title: "Shared options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/shared-options.html"
content_id: "MZwgVToYpeMuTU~fIvUFVQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:52.125362+00:00"
---

# Shared options

--config <coverity_config.xml>

-c <coverity_config.xml>
:   Uses the specified configuration file instead of the default configuration
    file located at 
    <install_dir>/config/coverity_config.xml.

--debug

-g
:   Turn on basic debugging output.

--help

-h
:   Prints a usage message to the command console, then exits.

--info
:   Displays certain internal information (useful for debugging), including the
    temporary directory, user name and host name, and process ID.

--tmpdir <tmp>

-t <tmp>
:   Specifies the temporary directory to use.

    - On UNIX, the default is `$TMPDIR`, or
      `/tmp` if that variable does not exist.
    - On Windows, the default is to use the temporary directory specified
      by the operating system.

--verbose <0, 1, 2, 3, 4>

-V <0, 1, 2, 3, 4>
:   Set the detail level of command messages. Higher is more verbose (more
    messages). Defaults to 1.
