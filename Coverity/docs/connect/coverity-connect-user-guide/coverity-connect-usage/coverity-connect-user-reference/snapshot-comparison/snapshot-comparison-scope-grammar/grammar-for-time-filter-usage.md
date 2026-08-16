---
title: "Grammar for time filter usage"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/grammar-for-time-filter-usage.html"
content_id: "qo82gv5jmFyQl2lBd3k_cQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:31.310946+00:00"
---

# Grammar for time filter usage

- For absolute dates, if the hours are missing from the `date` expression value, Coverity Connect interprets the time of day as 12:00
  AM of that day; meaning the beginning of the specified day. For example,
  `firstAfter(2014-01-01)` returns results from the first
  snapshot of January 1, 2014 and NOT the results from the first snapshot of
  January 2, 2014.
- For relative dates, the query considers the current time of day, so `1
  days ago` means "in the last 24 hours" and NOT "since 12:00 AM
  yesterday".
