---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "1ycyHWnFVjsaRq2qJJDT8g"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:47.331078+00:00"
---

# Options

--coverity-home <name_of_directory>
:   Specify the directory where Coverity Connect is installed, if it is
    installed in a directory other than the directory specified by `coverity-base-directory`.

-o | --output <name_of_file>
:   The destination output file. The file is in tar-bzip2 format.

--with-config
:   Include configuration files in the support archive.

--with-logs <days>
:   Include log files in the support archive for the specified number of previous days (including the current day).

-v
:   Enable verbose logging information for debugging purposes.

-vv
:   Enable very verbose logging information for tracing purposes.
