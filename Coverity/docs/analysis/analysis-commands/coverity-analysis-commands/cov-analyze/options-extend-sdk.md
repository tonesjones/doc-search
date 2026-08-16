---
title: "Options: Extend SDK"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options-extend-sdk.html"
content_id: "8C6byPikJ~M_yprypwJTtw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:39.376261+00:00"
---

# Options: Extend SDK

--command <checker_pathname>
:   [Extend SDK analysis option] Uses an Extend SDK checker at the specified path
    name.

--dtd <directory>
:   [Deprecated] Use the --prevent-root option instead.

--prevent-root
:   [Extend SDK analysis option] When running a Extend SDK checker, specify the
    location of the Coverity Analysis installation directory:

    ```
    --prevent-root /<install_dir>
    ```

    See Coverity Extend SDK 2026.6.0 Checker Development Guide for more information.
