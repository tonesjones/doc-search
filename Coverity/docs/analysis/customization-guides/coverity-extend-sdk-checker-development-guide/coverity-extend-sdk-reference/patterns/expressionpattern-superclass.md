---
title: "ExpressionPattern Superclass"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/expressionpattern-superclass.html"
content_id: "me6WEQcLefq0dCx7XfI20Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:20.026165+00:00"
---

# ExpressionPattern Superclass

ExpressionPattern matches expressions. By default, most
ExpressionPatterns implicitly strip casts off of the expressions
they match (exceptions to this are noted), since casts are often just noise from the
point of view of program analysis; likewise for the return value of
`last_expr()` and like functions.
ExpressionPattern also has a few extra functions that are not
available in other pattern hierarchies:

- bool match(const Expression *e, bool polarity) — Matches
  an expression that is negated if and only if `polarity` is
  false. For instance, `(a == b).match(e, false)` will match
  `a != b`. Typically used in 
  `ANALYZE_CONDITION`
   and is used in the implementation of `MATCH_COND`.
- match_with_casts — Matches an expressions without first
  stripping casts. This does not affect cast stripping in subpatterns.
- field() — Returns a pattern that matches a field taken off
  an expression matched by this pattern. For instance, if `A`
  matches `foo`, then `A.field()` matches
  `foo.bar`. The method can also take a
  SymbolPattern argument to restrict the specific
  fields to match.
- method() — Same as field(), except that
  it matches a non-static method call.
- get_type() — Returns the type of the last matched
  expression.

Most C++ operators are also overloaded for class
ExpressionPattern, that allows for the construction of patterns
that match equivalent syntax. For instance, pattern `A + B` matches an
addition.
