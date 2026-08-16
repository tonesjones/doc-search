---
title: "The record-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-record-expression.html"
content_id: "h4aUVep2SekhUBcdaTyMfA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:53.032083+00:00"
---

# The record-expression

A *record* is a collection of property-value pairs.

Remember:
In CodeXM, a checker takes the form of a `record-expression` that
contains records nested in a particular way, with specific `property-name` values,
some of them required.

## Syntax

A `record-expression` consists of a list of one or more properties,
separated by semicolons ( `;` ).
Each property consists of a name, an equals sign ( `=` ),
and an expression that represents the value of that property.
The entire `record-expression` is enclosed by
curly braces ( `{`
and `}` ).

  
 [image: Syntax diagram, record-expression]   

```
record-expression ::=
    '{'
                  property-name '=' expression
            ( ';' property-name '=' expression )*
              ';'?                              // The final semicolon is optional,
    '}'
```

## Details

Each `property-name` is an identifier.

Each record has its own particular record-type.
