---
title: "throwStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/throwstatement.html"
content_id: "WpytsZtANJE33Fm8gvLX6A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:13.700041+00:00"
---

# throwStatement

Matches `throw` statements.

A `throw` statement must have an explicit expression as an argument.

This pattern only matches nodes of type `statement`.

## Properties

`throwStatement` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `thrownExpression` | `expression` | The expression to be thrown by this statement |

**Inherits properties from:**

- astnode
- statement

## Example

The `throwStatement` pattern matches the following case:

[image: JavaScript code follows]

```
    throw 1;
```

In this instance, the `.thrownExpression` property is the literal `1`.
