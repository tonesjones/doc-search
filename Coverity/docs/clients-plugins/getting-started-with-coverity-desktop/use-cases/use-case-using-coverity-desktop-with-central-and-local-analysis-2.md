---
title: "Use case - using Coverity Desktop with central and local analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/use-case-using-coverity-desktop-with-central-and-local-analysis.html"
content_id: "_6R6Mqpx1WecQVKnC9qRQA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:48:27.958902+00:00"
---

# Use case - using Coverity Desktop with central and local analysis

**Goal:** The IDE Developer wants to see remote issues and also wants to use local
analysis before committing code to the source repository. This ensures that the IDE
Developer doesn't introduce any new defects into the source repository as a result of
their changes.

Figure 1. Central and local analysis model
[image: image]

1. Build Engineer builds and runs Coverity Analysis on the central code base.
   (This process is typically automated on some regular interval, such as
   nightly).
2. Build Engineer (or automated scripts) commits the issue results, along with function summary
   data, to Coverity Connect. (Projects and streams are already
   appropriately configured to receive issue data).
3. IDE Developer configures Coverity Desktop to connect to the central Coverity Connect server and configures local analysis
   settings.
4. IDE Developer checks out a section of the code for which they are responsible.
5. IDE Developer retrieves remote issues from the Coverity Connect server, and
   finds the file containing the defect to be fixed.
6. IDE Developer runs local analysis on the file to reproduce the defect
   locally.
7. IDE Developer fixes the defect in question.
8. IDE Developer runs local analysis again to verify that the defect is fixed.
9. IDE developer continues working on defects in individual files, or checks the
   completed code into the central repository.
