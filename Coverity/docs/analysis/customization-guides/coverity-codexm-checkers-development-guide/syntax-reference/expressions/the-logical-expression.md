---
title: "The logical-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-logical-expression.html"
content_id: "XMZ3RIMnOwBCbB1nTJd4uw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:48.648232+00:00"
---

# The logical-expression

A `logical-expression` expresses logical (as opposed to bitwise) AND or OR.
The result of a logical operation is either `true`
or `false`.

## Syntax

Two expressions are conjoined using either the logical AND ( `&&` ) or the logical OR ( `||` ) operator.

  
 [image: Syntax diagram, logical-expression]   

```
logical-expression ::=
    expression ( '||' | '&&' ) expression
```

Both of these operators are *short-circuiting:*
In other words, if the overall truth of the operation can be known by evaluating the left-hand expression
(that is, if it is `true` for `||`
or `false` for `&&`)
then the right-hand expression is not evaluated.

For logical AND ( `&&` ) expressions,
if the left-hand expression defines a variable via the matches-expression
`as` keyword,
that variable remains in scope for the right-hand expression as well.
