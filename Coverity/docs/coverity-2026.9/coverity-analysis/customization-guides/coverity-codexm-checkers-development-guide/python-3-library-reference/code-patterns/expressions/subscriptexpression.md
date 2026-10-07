---
title: "subscriptExpression"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/subscriptexpression.html"
content_id: "ZUc7eneYW22cfEDXZadGpw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:51.164019+00:00"
---

# subscriptExpression

Matches subscript expressions.

A subscript expression, enclosed in brackets ( `[ ]` ),
selects an item of a sequence (a string, tuple, or list) or a mapping (dictionary) object.

This pattern only matches nodes of type `expression`.

## Properties

`subscriptExpression` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `indexExpression` | `expression` | The expression used as a subscript |
| `primaryExpression` | `expression` | The expression in which the subscript expression appears |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches a subscript of `0`:

[image: CXM code follows]

```
    pattern subscriptOfZero {
        subscriptExpression {
            .indexExpression == integerLiteral {
                .value == 0
            }
        }
    };
```
