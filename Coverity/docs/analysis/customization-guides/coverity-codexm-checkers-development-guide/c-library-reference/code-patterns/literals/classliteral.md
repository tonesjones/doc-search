---
title: "classLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/classliteral.html"
content_id: "HmbiCOwxJeYJpaLNYcRTOA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:57.002077+00:00"
---

# classLiteral

Matches `class` literals.

This pattern only matches nodes of type `expression`.

## Properties

`classLiteral` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `targetType` | `type` | The type of the class |

**Inherits properties from:**

- astnode
- expression

## Example

To match literals for the class `Example`, you might use the following CodeXM pattern:

  
 [image: CXM code follows]   

```
    pattern boolTypeLiteral {
        classLiteral {
            .targetType == booleanType
        }
    };
```
