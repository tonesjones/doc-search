---
title: "fieldAccess"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/fieldaccess.html"
content_id: "CM~iYiKqrJzhGsGGSfM83A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:36.644868+00:00"
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

Given the following Go code:

  
 [image: Go code follows]   

```
    e Example{ MyInt: 35 }
    var i = e.MyInt
```

... the following CodeXM pattern would match the access to the `MyInt` field:

  
 [image: CXM code follows]   

```
    pattern accessToExampleMyInt {
        fieldAccess {
            .objectExpression == expression {
                .type == classType { .simpleName == "Example" }
            };
            .field == symbol { .simpleName == "myInt" }
        }
    }
```
