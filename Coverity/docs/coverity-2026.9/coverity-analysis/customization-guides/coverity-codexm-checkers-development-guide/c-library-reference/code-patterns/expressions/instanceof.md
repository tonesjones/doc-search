---
title: "instanceOf"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/instanceof.html"
content_id: "R7CVcp2fPnKXfDybfrxvYw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:27.895695+00:00"
---

# instanceOf

Matches the C# `instanceof()` function.

This pattern only matches nodes of type `expression`.

## Properties

`instanceOf` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression being examined |
| `referenceType` | `type` | The type the expression is being compared with |

**Inherits properties from:**

- astnode
- expression

## Example

The following pattern matches all calls to `instanceof()` for the class type `Example`:

  
 [image: CXM code follows]   

```
    pattern instanceOfExample {
        instanceOf {
            .referenceType == classType { .simpleName == "Example" }
        }
    };
```
