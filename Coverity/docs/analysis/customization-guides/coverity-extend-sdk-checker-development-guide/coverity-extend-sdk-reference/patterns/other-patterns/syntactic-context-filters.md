---
title: "Syntactic context filters"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/syntactic-context-filters.html"
content_id: "HalTwIcWciMU0JRBehZMeA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:29.154860+00:00"
---

# Syntactic context filters

- `ContainsPat (Pattern &subpattern)` — Match a tree that
  has a subtree that matches `subpattern`.
- `InContextPat (Pattern &context)` — Match a tree that has
  a parent tree that matches `context`.
- `InStatementContextPat` — Similar to
  `InContextPat`, but only searches within the closest
  enclosing statement.
- `SubTreePat (tree t)` — Match any subtree of
  `t`.
