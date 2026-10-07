---
title: "The type_of_empty_list"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/the-type_of_empty_list.html"
content_id: "Gddgcfo5Cs9XUDOMdKuejQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:13.708684+00:00"
---

# The type_of_empty_list

The `type_of_empty_list` is the type of the empty-list expression ( `[]` ).

## Syntax

  
 [image: Syntax diagram, type_of_empty_list]   

```
type_of_empty_list ::=
    '[]'
```

## Details

You can initialize a set or a list to an empty state by using the
empty list ( `[]` ).
This can be useful when you work with the for-accumulate-expression.

The empty list belongs to all list types.
