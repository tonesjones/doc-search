---
title: "Example: switch default"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/example-switch-default.html"
content_id: "V75c~1TghZrlKfiaYynzjQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:55.725176+00:00"
---

# Example: switch default

The SWITCH_DEFAULT checker
example (see also,
<install_dir>/sdk/samples/switch_default.cpp)
demonstrates how to match the `case` and `default`
sub-statements of a switch case statement. It reports switch statements that do not have
an explicit `default` statement and shows how it is possible to extract
the particular values in `case` statements.
