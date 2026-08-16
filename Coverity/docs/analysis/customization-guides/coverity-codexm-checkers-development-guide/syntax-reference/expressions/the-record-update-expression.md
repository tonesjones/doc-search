---
title: "The record-update-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-record-update-expression.html"
content_id: "f8RdDJnD6kpXCCNWwUg4Cw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:53.867865+00:00"
---

# The record-update-expression

A `record-update-expression` permits the contents of the indicated record expression to be updated with new values.

This expression can update the value of existing properties, but it cannot
add new properties to a record structure.

## Syntax

The syntax of a record update is similar to that of a `record-expression`.
Property specifications are also enclosed by matching curly braces
( `{` and `}` ),
but the update expression begins by specifying an existing record, followed by the keyword `with`.

The final semicolon ( `;` ) is optional.

  
 [image: Syntax diagram, record-update-expression]   

```
record-update-expression ::=
    '{'
        record-producing-expression
        'with'  property-name '=' expression
            ( ';' property-name '=' expression )*
              ';'?
    '}'
```

The `record-producing-expression` is an expression that refers to a
record that has already been created.

Each `property-name` in this expression must correspond to a property that was declared for the
`record-producing-expression`.

## Details

The result of this expression is a record that has the same type as the original `record-producing-expression`,
but with the specified properties assigned new values.
