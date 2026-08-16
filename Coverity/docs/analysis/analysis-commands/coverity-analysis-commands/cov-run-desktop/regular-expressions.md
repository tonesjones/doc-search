---
title: "Regular expressions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/regular-expressions.html"
content_id: "srDwpCVlNU9QR8qAKQSkNw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:42:09.553676+00:00"
---

# Regular expressions

All `cov-run-desktop` options that call for a regular expression
(`regex`) follow Perl syntax. The regular expression is case
sensitive, and is considered a match if it matches a substring (i.e. full string match
requires explicit anchors).
