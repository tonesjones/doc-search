---
title: "The expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-expression.html"
content_id: "b4GqMg7tzUbVj5Li_UpWRw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:20.920394+00:00"
---

# The expression

After the file-level elements, expressions are the main building blocks of a CodeXM program.

## Syntax

  
 [image: Syntax diagram, expression]   

```
expression ::=
      ( '(' expression ')' )
    | addition-expression
    | binary-expression
    | call-expression
    | comparison-expression
    | conditional-expression
    | decomposing-pattern-expression
    | element-access-expression
    | exists-expression
    | for-accumulate-expression
    | for-loop-expression
    | happens-before-expression
    | if-exists-expression
    | if-expression
    | lambda-expression
    | let-binding-expression
    | list-expression
    | literal-expression
    | logical-expression
    | matches-expression
    | multiplication-expression
    | pattern-expression
    | property-access-expression
    | record-expression
    | record-update-expression
    | set-expression
    | set-filter-expression
    | switch-expression
    | unary-expression
    | variable-expression
```
