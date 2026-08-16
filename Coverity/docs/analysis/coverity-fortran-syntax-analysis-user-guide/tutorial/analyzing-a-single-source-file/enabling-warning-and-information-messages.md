---
title: "Enabling Warning and Information Messages"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/enabling-warning-and-information-messages.html"
content_id: "3XYqiMMbS8wb0hSY_sqqqQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:47.854733+00:00"
---

# Enabling Warning and Information Messages

The `--impact` option provides coarse-grained control over the number of
defects included in the analysis results. It takes the values `High`,
`Medium` and `Low` and is set to `High`
by default. Warning messages are included in the analysis results if
`--impact=Medium` and information messages are additionally included
if `--impact=Low`. If a listing or report file is produced, all enabled
messages are printed, regardless of the `--impact` setting.

Users can also select the types of messages produced using the `-warn` and
`-inf` analysis options and their negations `-nwarn`
and `-ninf`.

-inf, -ninf
:   Show/do not show informational messages.

-warn, -nwarn
:   Show/do not show warnings.

These options affect the contents of the listing and report files as well as the defects
that appear in the analysis results.

Advanced users can exert fine-grained control over the impact of messages by creating and
using a custom configuration file.
