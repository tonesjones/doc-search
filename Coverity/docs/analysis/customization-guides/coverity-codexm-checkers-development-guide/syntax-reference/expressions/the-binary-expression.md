---
title: "The binary-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-binary-expression.html"
content_id: "nxVeZZMW9SI5d5M0lP3Z8g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:24.619285+00:00"
---

# The binary-expression

A `binary-expression` has a single operand
infixed between two other expressions.

Binary operators include standard operations for arithmetic, comparison, and logic;
a few others have a more special-purpose use in the context of CodeXM.

## Syntax

  
 [image: Syntax diagram, binary-expression]   

```
binary-expression ::=
    expression ( '+' | '-' | '*' | '/' | '++' | '??' | '<=>' | '==' | '!=' |
                 '<' | '<=' | '>' | '>=' | '&&' | '||' | '>=>' | '%' ) expression
```
