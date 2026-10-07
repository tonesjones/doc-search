---
title: "FileCheckerOption"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/filecheckeroption.html"
content_id: "igSl6afZF2QEWhUkGXYOEA"
version: "2026.9"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-10-04T23:35:08.127130+00:00"
---

# FileCheckerOption

This object contains the contents of the file that was passed as an argument to a checker
option.

checkerName: string
:   Name of the checker to which the option was passed (e.g.
    `WRAPPER_ESCAPE`).

optionName: string
:   Name of the option (e.g. `config_file`).

fileContents: string
:   The contents of the file passed as an option.
