---
title: "fieldAccess"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/fieldaccess.html"
content_id: "qzNNo3E_83ROzxJYjDhRCA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:37.313768+00:00"
---

# fieldAccess

Matches expressions that access fields.

This pattern only matches nodes of type `expression`.

## Properties

`fieldAccess` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `field` | `symbol` | The symbol of the field being accessed |
| `objectExpression` | `expression` | The object that owns the field being accessed |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches all accesses to public fields:

  
 [image: CXM code follows]   

```
    pattern publicFieldAccess {
        fieldAccess {
            .field == fieldSymbol {
                .access == `public`
            }
        }
    };
```
