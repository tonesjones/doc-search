---
title: "attributeReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/attributereference.html"
content_id: "3Eq7MXHc5crWsi7EbxCkzw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:39.438073+00:00"
---

# attributeReference

Matches references to attributes; that is, expressions with dot notation such as `test.type`.

This pattern only matches nodes of type `expression`.

## Properties

`attributeReference` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `primaryExpression` | `expression` | The base (the left-hand side) of the attribute reference expression |
| `propertyExpression` | `expression` | The accessed property (the right-hand side) of the attribute reference expression |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches an attribute expression that accesses a property named `foo`:

[image: CXM code follows]

```
    pattern fooAttribute {
        attributeReference {
            .primaryExpression == stringLiteral {
                .valueString == "foo"
            }
        }
    };
```
