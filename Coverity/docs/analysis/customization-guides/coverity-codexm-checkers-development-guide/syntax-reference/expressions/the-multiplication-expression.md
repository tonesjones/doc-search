---
title: "The multiplication-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-multiplication-expression.html"
content_id: "LkltM4eIpfdV4Tlmbpzhfg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:50.098907+00:00"
---

# The multiplication-expression

A `multiplication-expression` multiplies ( `*` ) or
divides ( `/` ) two integer values.

## Syntax

  
 [image: Syntax diagram, multiplication-expression]   

```
multiplication-expression ::=
    expression ( '*' | '/' ) expression
```

Each operand must evaluate to an integer value.

Either operand can be a complex subexpression, as well as an integer variable or an integer literal.

If the divisor does not evenly divide the dividend, the result is a truncated value: The remainder is discarded.

Dividing by zero causes a run-time error.

As in algebraic notation and nearly all programming languages, in an expression multiplication has precedence over division, and
a unary operation has precedence over multiplication.
