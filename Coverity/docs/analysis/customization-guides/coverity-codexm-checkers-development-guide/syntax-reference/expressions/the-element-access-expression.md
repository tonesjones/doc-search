---
title: "The element-access-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-element-access-expression.html"
content_id: "r6s~2Yu40mTmnJtTLjSc1g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:29.459961+00:00"
---

# The element-access-expression

This expression allows you to access individual elements within a list.

## Syntax

The notation is probably familiar to you from working with arrays in other programming languages:
It is simply the name of the list followed by square brackets ( `[ ]` ) that enclose an index value that
specifies a particular list entry.

  
 [image: Syntax diagram, element-access-expression]   

```
element-access-expression ::=
    list-producing-expression '[' index-expression ']'
```

The `list-producing-expression` is an expression that has already created a list.

The `index-expression` is a valid index to the list.
The first element in the list is element zero (`0`), so the index of the last entry is one less than
the list's `length` property.

Remember:
This expression is available to lists but not to sets or enums.
Sets and enums are considered to be unordered.
You can convert a list into a set, but the reverse is not true.
