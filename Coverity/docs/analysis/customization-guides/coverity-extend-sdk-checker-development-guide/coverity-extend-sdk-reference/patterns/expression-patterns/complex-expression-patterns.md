---
title: "Complex expression patterns"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-expression-patterns.html"
content_id: "QEitrNXLbBnCelXosn2a4Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:25.916016+00:00"
---

# Complex expression patterns

Program analyses often need to detect certain kinds of more complex expression patterns.
Several Extend SDK patterns do just this:

- `Arg` — Match an expression used as an argument to a function
  call. Accessors are provided to navigate to the call itself, and to see
  where in the call list the matched expression appeared. Will not strip
  casts.
- `ConditionPattern` — Match an expression used as a guard for a
  control flow statement or short-circuit operator.
- `Offset` — Match an expression that is the same as or an
  offset off of a given expression (pattern). For example, if you have an AST
  `p` that denotes a pointer, then
  `Offset(Same(p))` matches an expression like
  `&p->foo` which denotes a pointer to the same
  object that `p` does, but displaced by the offset of field
  `foo`. It will also recursively handle e.g.
  `&(p + 10)->foo`.
- `AnyField` — Given an expression (pattern), match an
  expression that is formed by appending field access operators. For example,
  given `a`, `AnyField(a)` matches
  `a.b` and `a.b.c`.
- `AnySubpart` — Like `AnyField`, except also
  allow array accesses, and (optionally) pointer dereferences.
- `Lval` — Match an *lvalue*, which is an expression that
  can appear on the left-hand side of an assignment operator. For example,
  `x` and `*p` are lvalues, whereas
  `3` and `a+b` are not (assuming those
  expressions use the built-in operators). A function call
  `f()` that returns a reference is translated by the
  parser into an explicit dereference `*f()` and the latter is
  matched by `Lval`.
