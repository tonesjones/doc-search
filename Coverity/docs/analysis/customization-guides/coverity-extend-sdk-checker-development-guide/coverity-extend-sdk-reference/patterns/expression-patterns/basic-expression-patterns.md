---
title: "Basic expression patterns"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/basic-expression-patterns.html"
content_id: "JoyRIwGWTVSYpJ_0AhMpIA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:23.316281+00:00"
---

# Basic expression patterns

The basic expression patterns are those that correspond directly to primitive syntactic
expression constructors. Here's a list of some of them.

- `Binop (BinaryOp op, ExpressionPattern &a, ExpressionPattern
  &b)` — Match a binary operator, for example `a +
  b`. Typically you do not need to explicitly create a Binop,
  because there are overloaded operators on
  ExpressionPatterns that will do so automatically.
  However, there are occasions where direct use is convenient. The possible
  values for `op` are listed in
  ><install_dir>/sdk/headers/ast/cc_flags.hpp
- `SymBinop(BinaryOp op, ExpressionPattern &a, ExpressionPattern
  &b` — Match an operator that is symmetric, for example
  `a + b`. Any of the `Binop` operators can
  be used, but only the symmetric ones make sense. This is useful when the
  `a` and `b` patterns are different, as
  `SymBinop` matches both `(a,b)` and
  `(b,a)` orderings.
- `ASymBinop(BinaryOp op, ExpressionPattern &, ExpressionPattern
  &b)` — Match an anti-symmetric operator or its dual. For
  example, `a < b` or `b > a`. Only
  anti-symmetric binops (inequalities) can be used.
- `Unop(UnaryOp op, ExpressionPattern &)` — Match a unary
  operator, for example `-a`. As with `BinOp`,
  direct use of `Unop` is only occasionally useful, since
  overloaded operators are provided that cover most of the common uses. The
  possible values for `op` are listed in
  ><install_dir>/sdk/headers/ast/cc_flags.hpp
- `MapAccess(ExpressionPattern &map, ExpressionPattern
  &key)`

  This expression pattern applies only to JavaScript.

  Properties of other expressions will be represented by this. Also, global
  variables are represented by a `MapAccess` off a
  `GlobalVar` map. For example, the following will match
  all global variable expressions:

  ```
  GlobalVar global;
  MapAccess access(global, _);
  if (MATCH(access)) { ... }
  ```
- `Star` — Match a dereference, for example `*p`.
  This will *not* match if `p` is an array (see
  below).
- `ArrayIndex` — Match an array element reference, i.e.
  `a[i]` where `a` is an array. This will
  *not* match if `a` is a pointer.
- `Assign` — Match an assignment or compound assignment, for
  example `a = b` or `a *= 2`.
- `Effect` — Match an increment or decrement, for example
  `++a` or `b--`.
- `CondPattern` — Match a use of the `?:`
  operator.
- `Const_int` — Match an integer literal.
- `Const_float` — Match a floating point literal.
- `Const_string` — Match a string literal.
- `Component` — Match a use of a field of an object, for example
  `a.b`.
- `Cast` — Match a cast. The flags control whether automatic
  (implicit) casts, manual (explicit) casts, or both are matched. This
  includes C++-style casts such as `reinterpret_cast` but not
  `dynamic_cast`.
- `StmtExpr` — Match a GNU statement expression, for example
  `({ x; y; z; })`.
- `This`— Match a use, either explicit or implicit, of the
  `this` expression.
- `Addr` — Match an address-of expression, for example
  `&e`.
- `Throw` — Matches a `throw` expression.
- `NewPattern` — Matches a `new` expression.
- `DeletePattern` — Matches a `delete`
  expression.
- `DynamicCast` — Matches a `dynamic_cast`
  expression.

The two remaining primitive constructs are variable reference and function call, which
are addressed in subsequent sections.
