---
title: "subscriptReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/subscriptreference.html"
content_id: "kqczRQMWu2_lTHFpmOeDOg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:06.753254+00:00"
---

# subscriptReference

Matches all uses of a subscript operator on an array.

This pattern only matches nodes of type `expression`.

## Properties

`subscriptReference` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `arrayExpression` | `expression` | The array the subscript is being used on |
| `indexExpression` | `expression` | The value inside the brackets ( `[ ]` ) |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches where a variable reference is used as the index expression of the array lookup:

  
 [image: CXM code follows]   

```
    pattern variableArrayLookup {
        subscriptReference {
            .indexExpression == variableReference
        }
    };
```
