---
title: "Miscellaneous patterns"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/miscellaneous-patterns.html"
content_id: "2hwvDijePJ01AgH9PU~waw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:30.447124+00:00"
---

# Miscellaneous patterns

- `ExitScope` — Match a local variable going out of scope. This
  matches when exiting using a `return` statement, or any other
  way the flow goes out of a block (for example, `break` or
  `goto` statements).
- `DeadVariable` — Match a local variable becoming *dead,*
  which means that its value is not used again on the current path. The main
  purpose of this pattern is to optimize a checker's performance by removing
  useless mappings from the store.
