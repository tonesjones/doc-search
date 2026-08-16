---
title: "Setting up the Black Duck Software Integrity Report generator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/setting-up-the-black-duck-software-integrity-report-generator.html"
content_id: "dcSr2oDLavhMhdZBJIQ4xw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:22.849712+00:00"
---

# Setting up the Black Duck Software Integrity Report generator

To set up the Black Duck Software Integrity Report generator, perform the following
steps:

1. Navigate to the Coverity Reports installation directory.
2. In the bin/ subdirectory, launch `bd-integrity-report`.
3. On the Report Settings tab, in the
   Tools subtab, select the contributing tools to use
   for the report.

     
    [image: image]
4. Select Cover Page, and enter information on terminology to
   use in the report.
5. Select Legal Text, and enter or upload any legal
   disclaimers to be shown on the summary page of the report.
6. Select the tab for each enabled analysis tool.
7. In the Connection page, enter the
   URL and Username for the
   tool's server (Coverity Connect). Click Check Connection
   to test.
8. In the Settings page, click Refresh
   to get a list of projects from the server. Select the desired project or product
   from the drop-down menu.
9. Repeat the settings for each enabled tool.
