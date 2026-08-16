---
title: "Creating new checkers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/creating-new-checkers.html"
content_id: "cEc9dK5~B4OP0cWQ03ychQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:13.300596+00:00"
---

# Creating new checkers

Rather than tuning or modifying the behavior of existing checkers, you might want to
tailor the analysis by adding special-purpose checkers of your own.

Coverity provides a couple of recommended ways to create checkers. These are:

- Custom dataflow and text checker
  "frameworks":
  DF.*CUSTOM_CHECKER* and
  TEXT.*CUSTOM_CHECKER*
- The domain-specific language CodeXM
