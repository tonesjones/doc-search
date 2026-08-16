---
title: "The if-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-if-expression.html"
content_id: "Qde05sSjGyt7Gp94cJCIYg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:38.901858+00:00"
---

# The if-expression

The `if` expression is a more versatile—and much more readable—construct
than the `conditional-expression`.

## Syntax

An `if` keyword introduces a conditional expression, followed by a
`then` clause and an optional
`else` clause.
To handle additional conditions, before the `else` clause you can
include any number of `elsif` clauses.

  
 [image: Syntax diagram, if-expression]   

```
if-expression ::=
    'if'
        condition
    'then'
        if-true-expression
        (
            'elsif'
                condition
            'then'
                if-true-expression
        )*
    'else'
        if-false-expression
    'endif'
```
