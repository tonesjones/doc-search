---
title: "Offline mode"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/offline-mode.html"
content_id: "brJO7Aotut44AY6K5qjneQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:49:21.908892+00:00"
---

# Offline mode

This option will run Coverity Desktop in a completely unconnected
state. When in Offline mode, Coverity Desktop will not be able to
download summary or triage data from Coverity Connect, and instead relies
on any cached data from previous local analyses. As a result, analysis summaries may be
out of date or nonexistent, and the results of local analyses could be less
accurate.

Note: Because local analysis requires summary data from Coverity Connect,
Offline mode requires that the Coverity Desktop plug-in was previously
connected to a Coverity Connect server, with a reference stream
configured.

Be sure that you are still able to connect with Coverity Connect when selecting Go Offline to
allow the summaries to be downloaded in full. This will give the best results when
doing offline analysis.
