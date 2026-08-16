---
title: "Predefined pattern objects"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/predefined-pattern-objects.html"
content_id: "VxUGIQ33xwGuMdcVoOMq6w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:21.980904+00:00"
---

# Predefined pattern objects

The Extend SDK has several pattern objects predefined for convenience.

- `anyASTNode, anyExpr, anyStmt, anyType, anySymbol` — Patterns that matches
  anything in the relevant pattern hierarchy.

  Note: Do not pass
  `anyXXX` as a pattern and then try to extract the data that it last
  matched; they are global and used internally, and the last matched data
  could change at any time.
- `_` (underscore) — A pattern that matches anything in any
  pattern hierarchy. Because of potential ambiguity, it's preferable to use
  `anyXXX` described previously.
