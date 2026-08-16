---
title: "Functions common to all patterns"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/functions-common-to-all-patterns.html"
content_id: "xcJ_YqGchFdF4H7VCjcJ9w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:18.752657+00:00"
---

# Functions common to all patterns

Every pattern superclass exposes a number of methods suitable for use in the Extend SDK. In the
following, T is used to represent either ASTNode,
type_t, or symbol_t (as appropriate).

- bool match(const T *t) — The primary matching function.
  Call it to attempt to match a data structure `t` with the
  pattern. If the match is a success, `match` returns true.
- T last_XXX() — Returns the last T that matched the
  pattern. Use only if the match succeeded. The value for
  XXX depends on which hierarchy you're using, and
  which level you're at in this hierarchy, and can be
  astnode, type,
  symbol, expr, or
  stmt. For compatibility with previous versions of the
  Extend SDK, get_tree is equivalent to
  last_astnode.
- void print(ostream &out) const — Prints a textual
  representation of this pattern. The text does not depend on whether the
  pattern has been used to match anything; it simply describes the structure
  of the pattern itself.
- `operator const T *()` — Same as
  last_XXX(); provided as a syntactic convenience.

Patterns can also be passed to operator<<(ostream), in which
case it will print the last matched T.
