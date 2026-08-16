---
title: "Disconnected mode"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/disconnected-mode.html"
content_id: "aVrVBbeSA16y~lkT5pXsHw"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:50.822519+00:00"
---

# Disconnected mode

It is possible to use Desktop Analysis when you are offline or otherwise unable to connect to
the Coverity Connect server. This is done by passing the `--disconnected`
option to `cov-run-desktop`. This will cause all options related to
Coverity Connect (`--stream`, `--reference-snapshot`,
etc.) to be ignored.

When in disconnected mode, `cov-run-desktop` will not be able to
download summary or triage data from Coverity Connect, and instead relies on any cached
data from previous local analyses. As a result, analysis summaries may be out of date or
nonexistent, and the results of Desktop Analysis could be less accurate.
