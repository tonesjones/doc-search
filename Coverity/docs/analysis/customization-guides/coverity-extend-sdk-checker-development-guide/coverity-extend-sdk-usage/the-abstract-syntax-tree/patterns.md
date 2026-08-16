---
title: "Patterns"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/patterns.html"
content_id: "FsfwKVSoGIZymtdDro~Utw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:29.526554+00:00"
---

# Patterns

The main method that checkers use to inspect the AST is through the use of
*patterns*, which are fragments of syntax with pattern variables (*holes*)
that can match arbitrary subtrees. The basic approach is to define a pattern with named
holes, test to see if the pattern matches some input syntax, and then use the named
holes to examine the parts of the patterns that match.
