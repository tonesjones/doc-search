---
title: "Regular expressions"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/regular-expressions.html"
content_id: "__k0OhWgv4_6ddAZ9TbTHQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:50.066012+00:00"
---

# Regular expressions

All `cov-format-errors` options that call for a regular expression
(`regex`) follow Perl syntax. The regular expression is case
sensitive, and is considered a match if it matches a substring (i.e. full string match
requires explicit anchors).
