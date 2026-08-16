---
title: "Error"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/error.html"
content_id: "~E3qTihw8zCUo~l992GbUg"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:12.366330+00:00"
---

# Error

If `cov-run-desktop` is unable to perform the requested action, the output
will include the `Error` object.

errorType: string
:   The type of the error that caused `cov-run-desktop` to
    fail.

errorSubType: string
:   The subtype of the error.

errorMessage: string
:   A message describing the nature of the error.

Note: The `Error` object may contain additional attributes, specific to
its `errorType`. Any program that reads this format must ignore any
unrecognized error attributes.
