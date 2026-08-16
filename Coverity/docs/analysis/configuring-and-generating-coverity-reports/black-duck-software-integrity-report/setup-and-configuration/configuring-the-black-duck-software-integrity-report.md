---
title: "Configuring the Black Duck Software Integrity Report"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-the-black-duck-software-integrity-report.html"
content_id: "7CSQnEU2OHnEPsWlwdkL8g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:23.503350+00:00"
---

# Configuring the Black Duck Software Integrity Report

**To configure a new Black Duck Software Integrity (BDSIR) report:**

1. Select Settings > Coverity Connect.
2. Select Coverity Connect Project. The projects available through the
   connection to Coverity Connect are displayed in the drop-down list.

   Note: Before
   creating a report, make sure that the Black Duck Software Integrity Report
   project has been analyzed with Coverity Analysis
   version 2026.6.0 prior to commit. BDSIR analysis in previous versions will not work with this
   report.
3. In the Customization pane, enter information to customize the report.
   The names and terms are used throughout the report, and the company name and logo
   are featured on the cover page. The company logo is optional.

   Note: The
   Project mentioned here refers to the corporate
   project name, and should not be confused with the Coverity Connect project.
4. Click File > Save to save the .yaml configuration file for future
   use.

   Note: This document can be used to regenerate a report with the same settings
   whenever the analysis data is updated.
5. *Optional*, edit the .yaml file in a text editor to change
   either of the following:
   - Update the SANS/OWASP report version.
   - Set `show-checker-details` key to `YES` if you
     want to display detailed information about checkers. The report will include
     two additional sections: "Enabled Checker List" and "List of Checkers Having
     a Violation". All the checkers used while running Coverity Analysis are listed in the "Enabled Checker List"
     section, and all checkers that report an issue are listed "List of Checkers
     Having a Violation".
   - Set `include-false-positive` key to `NO` to
     exclude defects marked as "intentional" or "false positive" from the
     report.

   For more details, see Black Duck Software Integrity Report configuration file.
