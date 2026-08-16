---
title: "The set-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-set-expression.html"
content_id: "9W8qf1CW~Tqe_qdVFhg3_g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:54.612804+00:00"
---

# The set-expression

A `set-expression` is created by specifying a list of values,
but a set is *not* considered to be ordered.

## Syntax

  
 [image: Syntax diagram, set-expression]   

```
set-expression ::=
    '['     expression
      ( ',' expression )*
    ']'
```

## Details

Each `expression` in the set is evaluated when the set is created.

The items in the set are not considered to have an order.

Elements do not have to be unique: More than one element can have the same value.
This is comparable to a CodeXM `list-expression`,
and differs from the usual mathematical meaning of a "set".

To access an element in a set, you can use a for-loop-expression.
You *cannot* use an element-access-expression, because the set elements are unordered.
On the other hand, you can use a set-filter-expression to retrieve members of a set that meet a particular criterion.
