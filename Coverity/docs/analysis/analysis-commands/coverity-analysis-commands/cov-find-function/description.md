---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "UwvAD4h~Bt7qLNpcuqY8yw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:49.096868+00:00"
---

# Description

In the Extend SDK, it is relatively easy to match on a C function with a specific name by
passing the name to the Fun pattern constructor. Otherwise, the mangled name must be
used to disambiguate which overloaded function should be matched. The
`cov-find-function` command looks for all of the mangled names that
contain the given `<name>`.

For other languages, this command finds the internal representation used by the
analysis.

This command makes it easier to find the name needed for matching on a specific function
or method, even an overloaded one. The `cov-find-function` command can
accept a regular expression to denote a set of functions to display.
