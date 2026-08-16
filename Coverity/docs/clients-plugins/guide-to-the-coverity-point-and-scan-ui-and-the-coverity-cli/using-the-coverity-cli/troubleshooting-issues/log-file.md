---
title: "Log file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/log-file.html"
content_id: "x6WgnY6zh9cIcRZegN_tTw"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:23.134032+00:00"
---

# Log file

The log file contains data written to the console by the Coverity CLI.
This file can be useful when you need to troubleshoot an issue where only the intermediate directory is available.

The log file is named coverity-cli-log.txt.
During analysis it is written to the coverity-cli/ subdirectory in the intermediate directory
(idir/).

Note:
This file does not include output written by the CLI during initialization.
