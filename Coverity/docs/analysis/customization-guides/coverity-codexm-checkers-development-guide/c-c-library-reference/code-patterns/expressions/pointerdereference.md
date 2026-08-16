---
title: "pointerDereference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/pointerdereference.html"
content_id: "jjDRSd4rzHagJQnDYyAErQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:29.851407+00:00"
---

# pointerDereference

Matches pointer dereference (`*p`) expressions.

## Properties

`pointerDereference` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `pointerExpression` | `expression` | The pointer being dereferenced |

**Inherits properties from:**

- astnode
- expression

## Example

The `pointerDereference` pattern matches the dereference in the following target C/C++ code:

  
 [image: C/C++ code follows]   

```
int n = *p_m;
```

The `.pointerExpression` property is a `variableReference` to `p_m`.
