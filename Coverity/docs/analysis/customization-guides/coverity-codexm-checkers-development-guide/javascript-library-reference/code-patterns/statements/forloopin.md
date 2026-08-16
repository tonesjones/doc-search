---
title: "forLoopIn"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/forloopin.html"
content_id: "DTXFEhdDAB2moSea8mGabQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:06.617861+00:00"
---

# forLoopIn

Matches simple `for in` loops.

This pattern only matches nodes of type `statement`.

## Properties

`forLoopIn` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `bodyStatement` | `statement` | The statement that the loop repeatedly executes. Frequently, this is a blockStatement. |
| `containerExpression` | `expression` | The iterated container |
| `kind` | `enum` | Always `` `in` `` |

**Inherits properties from:**

- astnode
- statement

## Example

The `forLoopIn` pattern matches the following `for` loop:

[image: JavaScript code follows]

```
    for (var x in l) {
        // ...
    };
```

## See also

forLoopOf,
forLoopSimple
