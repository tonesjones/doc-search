---
title: "Pattern combinators"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/pattern-combinators.html"
content_id: "jARrqwyOQ3h339U7wm56ww"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:31.630791+00:00"
---

# Pattern combinators

Patterns can be combined using the following general-purpose combinators.

Table 1. Pattern combinators

|  |  |
| --- | --- |
| `And(p1,p2)` | match if p1 and p2 match the given AST |
| `Or(p1,p2)` | match if p1 or p2 matches the given AST |
| `Within(p)` | match if some enclosing (parent or ancestor of given) AST matches p |
| `Contains(p)` | match if a subtree (descendant) of the given AST matches p |

For example, given the declarations:

```
CallSite bar("bar");
Const_int ct;
LocalVar lv;
StaticVar sv;
GlobalVar gv;
```

the pattern:

```
bar(Or(ct,lv), Or(sv,gv))
```

matches any call to
bar with two arguments, where the first argument is either an
integer literal or a local variable, and the second is either a static variable or a
global variable.

The following figure illustrates how Within() looks for
parents/ancestors, and Contains() looks for descendants:

Within() and Contains() combinators example

[image: image]

Thus, the following statement

```
MATCH( Within( Contains (pat)))
```

matches the pattern
from anywhere within the current function.

See Combinators (And, Or, etc.) for more
information.
