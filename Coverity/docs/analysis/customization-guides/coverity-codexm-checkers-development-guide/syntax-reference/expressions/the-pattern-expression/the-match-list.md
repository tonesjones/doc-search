---
title: "The match-list"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-match-list.html"
content_id: "zdVYfDS2m4DBYzvgpY3Zvg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:51.607681+00:00"
---

# The match-list

A `match-list` is a sequence of pattern expressions.

A checker evaluates the patterns in order: When a match is found, one or more expressions are evaluated,
and the remaining pattern expressions are skipped.

## Syntax

Patterns in the list are separated by a vertical bar ( `|` ).
A bar before the first pattern in the list is optional but recommended.

  
 [image: Syntax diagram, match-list]   

```
match-list ::=
    '|'? expression ( 'as' var0 )?
                    ( 'where' condition )?
                    ( '->' yields-expression )?
  ( '|' expression  ( 'as' var1 )?
                    ( 'where' condition )?
                    ( '->' yields-expression )? )*
```

`varX`
:   An identifier for a variable you can use in subsequent expressions within the `match-list`.

`condition`
:   An expression that describes an additional condition that must be matched.

`yields-expression`
:   An expression that is evaluated if the pattern matches the `condition`.

The patterns are tested in the order that they appear.
If a match is found, then the `yields-expression` is evaluated.
This becomes the value returned by the `match-list`, and no further patterns are tested.

If no `yields-expression` is specified, then the upper-level `expression`
becomes the value returned by the `match-list`.

If an `as` clause specifies a variable, that variable is available
(that is, "in scope") for use in expressions until the `match-list` has finished evaluating.
