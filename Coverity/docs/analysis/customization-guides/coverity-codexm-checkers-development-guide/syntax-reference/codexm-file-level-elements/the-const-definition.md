---
title: "The const-definition"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-const-definition.html"
content_id: "eYsoOkKiRYbvaP7SQHCYyQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:14.414745+00:00"
---

# The const-definition

A constant is a named value.

## Syntax

A constant declaration begins with the keyword `let`,
followed by an identifer that names the constant, then an equals sign
( `=` ) followed by an expression that evaluates to the desired value.

You can optionally specify a type for the constant.
If you do not, the type is inferred from the expression.

  
 [image: Syntax diagram, const-definition]   

```
const-definition ::=
    'let' identifier ( ':' type )? '=' expression
```

## Details

If a constant is declared at the file level, its scope is global.

Expressions can use a let binding to declare a named value.
The usage is similar, but when `let` is used within an expression,
the scope of the name is limited to the portion of the expression that follows the binding.
