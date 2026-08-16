---
title: "destructuringDeclaration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/destructuringdeclaration.html"
content_id: "OCnIandsR61vmhZj2fbb4A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:18.067605+00:00"
---

# destructuringDeclaration

Matches JavaScript destructuring declarations.

This pattern only matches nodes of type `statement`.

## Properties

`destructuringDeclaration` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `sourceExpression` | `expression` | The expression on the right side of the `=` operator |
| `targetExpressions` | `list<expression>` | The list of targets being assigned (on the left side of the `=` operator) |

**Inherits properties from:**

- astnode
- declaration

## Example

A destructuring declaration has the following form:

[image: JavaScript code follows]

```
    let [a, b] = c;
```

In this instance, the `.targetExpressions` property is the expression `[a, b]`,
and the `.sourceExpression` property is the expression `c`.
