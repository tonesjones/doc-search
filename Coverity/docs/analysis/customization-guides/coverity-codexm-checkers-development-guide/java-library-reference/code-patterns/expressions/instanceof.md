---
title: "instanceOf"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/instanceof.html"
content_id: "R6vP6dr49jB3lUQKOYxV1g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:05.389122+00:00"
---

# instanceOf

Matches `instanceof` expressions.

This pattern only matches nodes of type `expression`.

## Properties

`instanceOf` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression being examined by `instanceof` |
| `referenceType` | `type` | The type the expression is being compared with |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches all calls to `instanceof` for the class type `Example`:

  
 [image: CXM code follows]   

```
    pattern instanceOfExample {
        instanceOf {
            .referenceType == classType { .simpleName == "Example" }
        }
    };
```
