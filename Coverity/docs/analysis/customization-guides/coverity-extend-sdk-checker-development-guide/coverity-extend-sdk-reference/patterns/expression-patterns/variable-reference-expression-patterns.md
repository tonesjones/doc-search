---
title: "Variable reference expression patterns"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/variable-reference-expression-patterns.html"
content_id: "ama0JvWi_omD5BhCYkRcTg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:24.624857+00:00"
---

# Variable reference expression patterns

There are several patterns that match variable references, possibly taking into account
scope and linkage:

- `Var` — Match a variable used in an expression.
- `TempVar` — Match a use of a temporary variable inserted by
  the parser.
- `LocalVar` — Match a use of a (nonstatic) local variable.
- `StaticVar` — Match a use of a static variable.
- `GlobalVar` — Match a use of a global variable.
- `Parm` — Match a use of a formal parameter.
- `FunctionDecl` — Match a use of a function as an expression
  (either the called expression in a function call, or taking the address of a
  function).
- `FunLocal` — Match a use of a local variable, formal
  parameter, or a field of (recursively) a class/struct/union-valued local or
  parameter. This corresponds to stack-allocated storage (except arrays).
