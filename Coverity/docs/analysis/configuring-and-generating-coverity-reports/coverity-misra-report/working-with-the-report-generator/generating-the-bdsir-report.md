---
title: "Generating the BDSIR report"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/generating-the-bdsir-report.html"
content_id: "Tdxovfy_nkExBPjQUg_sZQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:50.825009+00:00"
---

# Generating the BDSIR report

The user workflow for generating the BDSIR Report is as follows:

1. Select Settings > Coverity Connect.
2. Use the Coverity Connect Project drop-down list to select a
   project in Coverity Connect. This requires a valid connection, as established in the
   previous
   step.

   Note: Before
   creating a report, make sure that the BDSIR project has been analyzed with
   Coverity Analysis version 2026.6.0 prior to commit. BDSIR analysis in previous
   versions will not work with this report.
3. In the Customization pane, enter information to customize the report.
   The names and terms you specify are used throughout the report, and the company name
   and logo (if specified) are featured on the cover page.

   If you elect to use a
   logo, click Choose File button to specify the name of an
   image file containing the logo. (Coverity can handle most standard image files.
   If it cannot handle the image you provide, it returns an error specifying the
   formats it can handle.)

   Note: The
   Project mentioned here refers to the corporate
   project name, and should not be confused with the Coverity Connect project.
4. Click File > Save to save the .yaml configuration file for future
   use.

   Note: This configuration file can be used to regenerate a report with the
   same settings whenever the analysis data is updated.
5. Click Create Report to generate the report.
