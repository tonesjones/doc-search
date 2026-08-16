---
title: "The lambda-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-lambda-expression.html"
content_id: "yZi0xP_L_rIL7prTxI1ZnA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:40.369946+00:00"
---

# The lambda-expression

A `lambda-expression` is an unnamed function literal, also known as an *anonymous function*.

In general, the criteria for using a `pattern-expression` also apply to a `lambda-expression`:
Use these constructs in situations where the expression is only used once, and is simple enough to convey its intent without
reducing the readability of the expression in which it appears.

## Syntax

Syntactically, a lambda is similar to a `function-definition`.
But no name appears after the `function` keyword,
and the return type is inferred from context rather than explicitly declared.

  
 [image: Syntax diagram, lambda-expression]   

```
lambda-expression ::=
    'function'
    ( '<'       type-parameter-identifier
             ( ',' type-parameter-identifier )*
      '>' )?
    '('         parameter-identifier ':' type
          ( ',' parameter-identifier ':' type )*
    ')'
    '->' expression
```

Each `type-parameter-identifier` is a generic placeholder for an actual type.
This identifier can be used within the parameter list as if it were a known type, the return type,
or any portion of the expression the function evaluates.

Each `parameter-identifier` is an identifier for an explicitly typed parameter.
Each parameter name must be unique to the function.

Each parameter's type must be one of the following:

- A type that is native to CodeXM or that has previously been defined in this CodeXM (`.cxm`) file
- A type defined by an included language library or an included `.cxm` file
- A `type-parameter-identifier` specified in this lambda definition
