---
title: "Combinators (And, Or, etc.)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/combinators-and-or-etc.-.html"
content_id: "EqXsbXEE84zd0CXNPfnbhg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:31.112146+00:00"
---

# Combinators (And, Or, etc.)

- `constant(int i)` — Equivalent to
  `Const_int(i)`.
- `assign(ExpressionPattern &a, ExpressionPattern &b)` —
  Equivalent to `Assign(a, b).`
- `cast(ExpressionPattern &e)` — Equivalent to
  `Cast(e)`.
- `opt_cast(ExpressionPattern &e)` — Equivalent to `Or(e,
  Cast(e))`.
- `Const` — Build a `Const_obj` pattern.
- `And(Pattern &a, Pattern &b, ...)` — Match if
  *all* of the argument patterns match. Available for all pattern
  hierarchies.
- `Or(Pattern &b, Pattern &b, ...)` — Match if
  *any* of the argument patterns match. Available for all pattern
  hierarchies.
- `Not(Pattern &a)` — Match if `a` does
  *not* match.
- `Contains` — Build a `ContainsPat` pattern.
- `Within` — Build an `InContextPat` pattern.
- `WithinStatement` — Build an
  `InStatementContextPat` pattern.
- `Evals_to` — Look in an expression `e` to find
  the subexpression `s` that determines the value yielded by
  `e`. For example, `Evals_to(a = b`)
  returns `b`. The exact forms that are recognized are
  documented in the comments above the declaration in
  ><install_dir>/sdk/headers/patterns/extend-patterns.hpp.
