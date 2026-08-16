---
title: "Options: Shared"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options-shared.html"
content_id: "i9ciOf3iYfFqIlw8UVbDGA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:43.273567+00:00"
---

# Options: Shared

--config <coverity_config.xml>

-c <coverity_config.xml>
:   Uses the specified configuration file instead of the default configuration
    file located at 
    <install_dir>/config/coverity_config.xml.

--debug

-g
:   Turn on basic debugging output.

--ident
:   Displays the version of Coverity Analysis and build number.

--info
:   Displays certain internal information (useful for debugging), including the
    temporary directory, user name and host name, and process ID.

--redirect stdout|stderr,<filename>

-rd stdout|stderr,<filename>
:   Redirects either the `stdout` or the `stderr`
    stream to the specified file.

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
