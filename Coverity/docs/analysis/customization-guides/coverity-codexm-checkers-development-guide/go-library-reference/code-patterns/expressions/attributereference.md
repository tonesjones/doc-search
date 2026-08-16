---
title: "attributeReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/attributereference.html"
content_id: "XkwXDTo9hDMJTMD1qwSoCg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:32.582512+00:00"
---

# attributeReference

Matches expressions that reference an attribute: for example, `townStructure.street`.

This pattern only matches nodes of type `expression`.

## Properties

`attributeReference` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `primaryExpression` | `expression` | The base (the left-hand side) of the attribute-reference expression |
| `propertyExpression` | `expression` | The property to access (the right-hand side) of the attribute-reference expression |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches an attribute-reference expression that accesses a property named `street`:

  
 [image: CXM code follows]   

```
    pattern customAttribute {
        attributeReference {
            .primaryExpression == stringLiteral {
                .valueString == "street"
            }
        }
    }
```
