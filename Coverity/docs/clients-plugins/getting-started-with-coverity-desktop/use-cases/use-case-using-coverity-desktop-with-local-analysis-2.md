---
title: "Use case - using Coverity Desktop with local analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/use-case-using-coverity-desktop-with-local-analysis.html"
content_id: "HoxtxI3pBRWOCEs_y6mcoQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:48:27.050936+00:00"
---

# Use case - using Coverity Desktop with local analysis

**Goal:** The IDE Developer wants to analyze and view defect results on their local
code.

The following diagram shows a high-level view of the process:

Figure 1. Local analysis model
[image: image]

1. Build Engineer builds and runs Coverity Analysis on the
   central code base. (This process is typically automated on some regular
   interval, such as nightly).
2. Build Engineer (or automated scripts) commits the issue results, along with
   function summary data, to Coverity Connect. (Projects and
   streams are already appropriately configured to receive issue data).
3. IDE Developer configures Coverity Desktop to connect to the
   central Coverity Connect server and configures local analysis
   settings.
4. IDE Developer checks out a section of the code for which they are responsible.
5. IDE Developer runs local analysis on selected file(s).
6. IDE Developer examines and triages the defects that were found by the
   analysis.
7. IDE Developer fixes a list of defects.
8. IDE Developer runs local analysis again to ensure that the defects were
   fixed.
9. IDE Developer checks the code into the central repository.
