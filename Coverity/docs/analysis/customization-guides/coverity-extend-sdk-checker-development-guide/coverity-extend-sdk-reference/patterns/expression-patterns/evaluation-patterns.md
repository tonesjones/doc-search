---
title: "Evaluation patterns"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/evaluation-patterns.html"
content_id: "fp87yN~1GdSRWCN3C~RtlA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:26.561968+00:00"
---

# Evaluation patterns

The evaluation patterns find the subexpression `s` of a (potentially)
larger expression `e` that specifies the value yielded by
`e`. These patterns are most easily explained in terms of the `Evals_to` function.

- `EvalPattern (Pattern &pat)` — Use
  `Evals_to` repeatedly to dig down into the matched
  expression, stopping as soon as `pat` matches a subexpression
  returned by `Evals_to`.
- `EvalsToPattern` — Use `Evals_to` to dig down
  to the smallest subexpression, then attempt to match `pat`
  against that subexpresssion.
