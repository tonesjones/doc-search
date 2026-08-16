---
title: "CheckerOptions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/checkeroptions.html"
content_id: "5p60DLIKqMde~HVIQoNr3w"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:29.617051+00:00"
---

# CheckerOptions

The optional `CheckerOptions` class contains option names and the option
values in the following format:

<optionName>?: <optionValue>
:   Each option value may be one of the following:

    - A number
    - The Boolean value `true` or `false`
    - A string
    - An array of strings. Whereas the previous cases all correspond to
      passing a single `--checker-option` option on the
      `cov-analyze` or `cov-run-desktop`
      command line, an array value here means the same thing as passing
      multiple `--checker-option` options.
