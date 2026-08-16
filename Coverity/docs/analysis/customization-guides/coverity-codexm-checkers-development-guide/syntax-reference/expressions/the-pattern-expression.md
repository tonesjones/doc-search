---
title: "The pattern-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-pattern-expression.html"
content_id: "ioGph2W~g9~oc8pm7MAxzw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:50.746829+00:00"
---

# The pattern-expression

A `pattern-expression` allows you to define a pattern inline—that is, within another expression.
For patterns, it is the analog to a lambda (nameless) expression for functions.

In general, the criteria for using a lambda function also apply to a `pattern-expression`:
Use these constructs in situations where the expression is only used once, and is simple enough to convey its intent without
reducing the readability of the expression in which it appears.

## Syntax

A pattern definition is introduced by the `pattern` keyword,
followed by the name (an identifier) by which the pattern will be known.
This is followed by a match-list enclosed by curly braces
( `{` and `}` ).

[image: image]

```
pattern-expression ::=
    'pattern' '{'
        match-list
    '}'
```
