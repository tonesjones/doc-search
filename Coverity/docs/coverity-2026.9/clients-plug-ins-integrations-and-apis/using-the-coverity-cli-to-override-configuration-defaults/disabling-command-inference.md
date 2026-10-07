---
title: "Disabling command inference"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/disabling-command-inference.html"
content_id: "ojiQqFwzwITAB5cKOC3fIQ"
version: "2026.9"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-10-04T23:35:05.345634+00:00"
---

# Disabling command inference

Use the --disable-build-command-inference option to specify
that the Coverity CLI should not do build-command inference during capture.
This can be of use if you know that you are not scanning in a build environment.

You can use this option with the `capture` and `scan` subcommands.

## Syntax

```
--disable-build-command-inference
```

## See also

Capture configuration
