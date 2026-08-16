---
title: "C/C++ primitive to manage false positives"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/c/c-primitive-to-manage-false-positives.html"
content_id: "Lfl2GULP_FH5FjYJbeLu3g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:42.611845+00:00"
---

# C/C++ primitive to manage false positives

The primitive `__coverity_no_check_return__()` suppresses checking of return values to reduce
the number of reports from the CHECKED_RETURN checker.

## `__coverity_no_check_return__()`

Labels a function so that the inconsistent checking of its return value
*will not* generate CHECKED_RETURN defects.
