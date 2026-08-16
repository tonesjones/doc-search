---
title: "The switch-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-switch-expression.html"
content_id: "Dalyv_p3lcADKJFoaWQ_OA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:56.116405+00:00"
---

# The switch-expression

A `switch-expression` chooses among two or more alternatives, based on the outcome of a controlling expression.

A `switch` is a convenient way to represent a chain of conditions,
when each condition is a pattern of the same expression.

## Syntax

The `switch-expression` is introduced by the `switch` keyword,
followed by the controlling expression enclosed by parentheses.
This is followed by a match-list enclosed by curly braces
( `{` and `}` ).

The `match-list` must be followed by a required default alternative.
This alternative is also introduced by a vertical bar ( `|` ),
followed by the keyword `default`.
Then an arrow operator ( `->` ) introduces an expression that is evaluated only if no prior matching expression has been found.

  
 [image: Syntax diagram, switch-expression]   

```
switch-expression ::=
    'switch' '(' expression ')' '{'
            match-list
        '|' 'default' '->' expression
    '}'
```

## Details

The syntax and behavior of a `switch-expression` are similar to a `pattern`,
but they differ in certain ways:

- A `pattern` is written to match a specific circumstance.
  It allows other circumstances to be ignored.
  Used as an operand in a matches expression,
  a `pattern` can (deliberately) *not* match things it is not interested in.
- By contrast, a `switch` must always produce a result.
  Its `match-list` enumerates outcomes that might be found,
  and it concludes with a `default` clause to handle any outcomes that are not enumerated.
