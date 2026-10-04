---
title: "Localizing reports"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/localizing-reports.html"
content_id: "laeQvubOrCMvDs1G1D16JQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:43.012481+00:00"
---

# Localizing reports

You can now localize MISRA reports for Japanese, Korean, and Chinese. To localise the
report, make your selection from the Report's Locale dropdown
list in the Customization pane.

Important: You must have the same locale configured in Coverity Connect as you set for your report. Otherwise, portions of the
report will be presented in the user's locale rather than the desired one. (Use the drop
down list from Admin User > Preferences > Locale to select the desired locale.)

You can also localize MISRA reports by setting the
`locale` field in the .yaml configuration file,
or by using the `--locale` option in the comnand line.
