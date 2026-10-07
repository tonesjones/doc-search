---
title: "Localizing reports"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/localizing-reports.html"
content_id: "hLLRz2untx18AY_VllYEFA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:41.465612+00:00"
---

# Localizing reports

You can localize a CVSS report either by setting the `locale` field in the
.yaml configuration file, or by using the
`--locale` option in the comnand line.

The following values are supported for the locale:

- `en_US` for English
- `ja_JP` for Japanese
- `ko_KR` for Korean
- `zh_CN` for Chinese

Important: You must have the same locale configured in
Coverity Connect as you set for your report. Otherwise, portions of the report will be
presented in the user's locale rather than the desired one.
