---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/options.html"
content_id: "Nha5OoHgOAKwwH__2xvSRg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:55.334678+00:00"
---

# Options

## Shared options

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

--verbose <0, 1, 2, 3, 4>

-V <0, 1, 2, 3, 4>
:   Set the detail level of command messages. Higher is more verbose (more
    messages). Defaults to 1.
