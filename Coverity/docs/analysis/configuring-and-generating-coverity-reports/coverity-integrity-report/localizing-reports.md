---
title: "Localizing reports"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/localizing-reports.html"
content_id: "OEhw1ebEjA~GGA_PnurxOw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:38.579800+00:00"
---

# Localizing reports

You can localize a Coverity Integrity report either by setting the
`locale` field in the .yaml configuration file,
or by using the `--locale` option in the comnand line.

The following values are supported for the locale:

- `en_US` for English
- `ja_JP` for Japanese

Important: You must have the same locale configured in
Coverity Connect as you set for your report. Otherwise, portions of the report will be
presented in the user's locale rather than the desired one.
