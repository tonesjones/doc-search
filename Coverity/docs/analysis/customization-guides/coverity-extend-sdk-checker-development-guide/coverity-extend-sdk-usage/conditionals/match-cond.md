---
title: "MATCH_COND"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/match_cond.html"
content_id: "uc4mviIgEt~54BuI3obKDg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:44.074182+00:00"
---

# MATCH_COND

Within ANALYZE_CONDITION, you can use MATCH_COND to
inspect the guard expression. MATCH_COND automatically takes account
of whether the true or false branch is being taken. For example, if the code to analyze
says:

```
if (x == y) {
  // then-branch
}
else {
  // else-branch
}
```

then the checker fragment:

```
Expr a, b;
MATCH_COND(a != b)
```

matches only when the `else` branch is followed.

Note: It is important to note that `MATCH_COND` only works when matching
comparisons. For instance, `MATCH_COND(a == b)` will match a true
`a == b` condition or a false `a != b` condition.
Conditions are always comparisons *except when the condition is a non-comparison
boolean expression*. For instance, the condition in the expression `int x;
if(x) { }` will be transformed into `x != 0`, but the
condition in the expression `bool x; if(x) { }` will simply be
`x`. In the latter case, `MATCH_COND` will not work,
so you might instead check the `cov_polarity` variable, which indicates
whether the condition being evaluated is true or false. For example,
`MATCH_COND(a == b)` is equivalent to `cov_polarity ? MATCH(a
== b) : MATCH(a != b)`.
