---
title: "Shared options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/shared-options.html"
content_id: "kkG_DsIMXukDWkXE5BxzKA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:39.192221+00:00"
---

# Shared options

The following options are common to all modes of the `cov-manage-im`
command.

--config <coverity_config.xml>

-c <coverity_config.xml>
:   Uses the specified configuration file instead of the default configuration
    file located at 
    <install_dir>/config/coverity_config.xml.

--debug

-g
:   Turn on basic debugging output.

--response-file|-rf <file>
:   Specify command line options in file. These options are
    processed as if they are specified on the command line at the same point as
    the response file is specified. Multiple response files can be used on a
    single command line, but nested response files are not allowed.

    Lines in response files starting with # are considered to be comments and are
    ignored.

--verbose <0, 1, 2, 3, 4>

-V <0, 1, 2, 3, 4>
:   Set the detail level of command messages. Higher is more verbose (more
    messages). Defaults to 1.
