---
title: "Localizing reports"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/localizing-reports.html"
content_id: "Q3rh73L9aFHy0GmlJamQnA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:18.808663+00:00"
---

# Localizing reports

You can now localize Security reports for Japanese, Korean, and Chinese. To localise the
report, make your selection from the Report's Locale dropdown
list in the Customization pane.

Important: You must have the same locale configured in Coverity Connect as you set for your report. Otherwise, portions of the
report will be presented in the user's locale rather than the desired one. (Use the drop
down list from Admin User > Preferences > Locale to select the desired locale.)

You can also localize Security reports by setting the
`locale` field in the .yaml configuration file,
or by using the `--locale` option in the comnand line.
