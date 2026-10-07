---
title: "The conditional-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/the-conditional-expression.html"
content_id: "x6LAATJMR~gTJN2dyqkOKA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:11.518262+00:00"
---

# The conditional-expression

The `?:` ("ternary") operator evaluates one of two expressions,
depending on whether the specified condition is `true` or `false`.

## Syntax

  
 [image: Syntax diagram, conditional-expression]   

```
conditional-expression ::=
    condition '?' if-true-expression ':' if-false-expression
```

A `condition` is simply an expression that evaluates to either `true`
or `false`.
