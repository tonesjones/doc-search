---
title: "The Abstract Syntax Tree"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/the-abstract-syntax-tree.html"
content_id: "5C5qsoBWLRwlFxPov~4ZTQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:53.857323+00:00"
---

# The Abstract Syntax Tree

There are three main tasks that a checker typically performs:

1. Inspect the AST to recognize syntax of importance.
2. Update the store to reflect the effect of that syntax (simple checkers do not
   do this).
3. Output errors when appropriate.
