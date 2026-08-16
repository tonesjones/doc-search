---
title: "Use case - using Coverity Desktop with central analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/use-case-using-coverity-desktop-with-central-analysis.html"
content_id: "PCnNJDcEAii~RdKYHpxMRQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:48:26.205925+00:00"
---

# Use case - using Coverity Desktop with central analysis

**Goal:** The IDE Developer wants to view and triage analysis results from the
central source code repository.

The following diagram shows a high-level view of the process:

Figure 1. Central analysis model
[image: image]

1. Build Engineer builds and runs Coverity Analysis on the
   central code base. (This process is typically automated on some regular
   interval, such as nightly).
2. Build Engineer (or automated scripts) commits the issue results to Coverity Connect. (Projects and streams are already
   appropriately configured to receive issue data).
3. IDE Developer configures Coverity Desktop to connect to the
   central Coverity Connect server.
4. IDE Developer checks out a section of the code for which they are responsible.
5. IDE Developer examines the impact of the remote issues in the code and
   triages them within the IDE.
6. IDE Developer fixes issues and checks the code into the central
   repository.
7. The nightly analysis runs.
