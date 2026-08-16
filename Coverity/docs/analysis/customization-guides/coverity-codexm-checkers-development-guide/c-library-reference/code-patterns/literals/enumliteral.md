---
title: "enumLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/enumliteral.html"
content_id: "sT5mqJ4CqGFJYhm~kmdsAg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:57.662609+00:00"
---

# enumLiteral

Matches `enum` literals.

This pattern only matches nodes of type `expression`.

## Properties

`enumLiteral` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `type` | `type` | The underlying type of the `enum` |
| `value` | `int` | The underlying value |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches only `enum` literal values whose underlying type is `byte`:

  
 [image: CXM code follows]   

```
    pattern enumByteLiteral {
        enumLiteral {
            .type == integralType {
                .kind = `byte`
            }
        }
    };
```
