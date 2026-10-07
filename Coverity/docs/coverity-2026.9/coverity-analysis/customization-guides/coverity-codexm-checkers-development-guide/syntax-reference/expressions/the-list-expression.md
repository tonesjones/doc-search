---
title: "The list-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/the-list-expression.html"
content_id: "7al~AXII7yh4AWdSvO~Cqg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:12.503304+00:00"
---

# The list-expression

A `list-expression` is a list of values considered to be an ordered group.

## Syntax

The list is enclosed by square brackets ( `[ ]` ).
The items in the list are separated by commas ( `,` ).

  
 [image: Syntax diagram, list-expression]   

```
list-expression ::=
    '['
        expression (',' expression )*
    ']'
```
