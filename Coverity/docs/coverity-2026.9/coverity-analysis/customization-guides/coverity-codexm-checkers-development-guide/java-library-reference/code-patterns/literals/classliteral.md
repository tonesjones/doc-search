---
title: "classLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/classliteral.html"
content_id: "u2bpq~QQWKFn0uw_wXTXjA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:41.402138+00:00"
---

# classLiteral

Matches class literals.

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

To match literals for the class `Example`, you could use the following CodeXM pattern:

  
 [image: CXM code follows]   

```
    pattern exampleClassLiteral {
        .targetType == classType { .simpleName == "Example"}
    };
```
