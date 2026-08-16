---
title: "parameterWithDefault"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/parameterwithdefault.html"
content_id: "bCKBXuUd0ndmu0QO7t4t~A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:36.999964+00:00"
---

# parameterWithDefault

Matches function parameters that have a default value expression.

The pattern returns the default value in `defaultExpression`.

This pattern only matches nodes of type `expression`.

## Properties

`parameterWithDefault` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `defaultExpression` | `expression` | The default value of this parameter |
| `parameter` | `expression` | The parameter |

**Inherits properties from:**

- astnode
- expression

## Example

In the following JavaScript function definition, the `parameterWithDefault` pattern matches the statement
that initializes the parameter `b`:

[image: JavaScript code follows]

```
    function defaultParam(a, b = 1) {
        return a * b;
    };
```

In this instance, the `.parameter` property is the variable reference to `b`, and
the `.defaultExpression` property is the literal `1`.
