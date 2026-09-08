---
title: "Analysis Results"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/analysis-results.html"
content_id: "Ywm0xHpwoOQQzZmpb6pJeA"
version: "latest"
section: "Software Risk Manager Plugins Guide"
scraped_at: "2026-09-08T20:05:50.107044+00:00"
content_hash: "380a5f2a45ac26be495432f2ba92b5cf4cac1f9b3c3fd7a7a2e5bcb6d463a5c3"
---

# Analysis Results

If the Software Risk Manager TeamCity plugin is configured to wait for analysis results,
and a name has been provided to the *Report archive name* field, you can configure
a build report tab for your TeamCity project.

To create a build report tab for Software Risk Manager in TeamCity, please follow these
steps:

1. Configure the Software Risk Manager build runner so that it waits for analysis
   results
2. Fill out the *Report archive name* field
3. Run the build
4. On the *Edit Build* page, add the build artifact to your build artifact
   paths. The name of the zip archive should match the configured *Report archive
   name*
5. On the *Edit Project* page, navigate to the *Report Tabs*
   section
6. On the *Report Tabs* section, click the *Create new build report tab*
   button
7. In the dialog that opens, fill out the *Tab Title* field
8. In the *Start page* field, enter the path to the report. This will look
   something like [report-archive-name].zip!codedx-teamcity-report.html
9. Click the *Save* button
10. Run a new build

The report tab will appear on the *Build Results* page. It contains a link and
tables. Clicking the link will open the latest results within the Software Risk Manager
application. The tables show the number of findings for each severity and status. If
applicable, a delta between the current build and previous build is included.
