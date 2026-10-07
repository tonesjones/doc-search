---
title: "builtinFunctionExpression"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/builtinfunctionexpression.html"
content_id: "ryQaPBQvGG4DCOE54M~olA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:35.208854+00:00"
---

# builtinFunctionExpression

Matches calls to built-in functions.

This pattern only matches nodes of type `expression`.

## Properties

`builtinFunctionExpression` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `args` | `list<expression>` | A list that contains the arguments passed to the function |
| `name` | `string` | The name of the built-in function |

**Inherits properties from:**

- astnode
- expression
