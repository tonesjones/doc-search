---
title: "The unary-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/the-unary-expression.html"
content_id: "sRU3ndAAiV~p90imGuQupw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:13.392916+00:00"
---

# The unary-expression

The `unary-expression` takes a single operand.
A unary operation negates its operand—either numerically or logically.

## Syntax

A numerical expression is negated by prefixing a minus sign ( `-` ).
A logical expression is negated by prefixing the logical NOT operator, represented by an exclamation point ( `!` ).

  
 [image: Syntax diagram, unary-expression]   

```
unary-expression ::=
    ( '!' | '-' ) expression
```
