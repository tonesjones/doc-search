---
title: "whileLoop"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/whileloop.html"
content_id: "Be~ncR8HPgBvCyp0oBj1aw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:26.039789+00:00"
---

# whileLoop

Matches standard `while` loops.

This pattern matches only `while` loops, and does not match
`do ... while` or `for` loops.

This pattern only matches nodes of type `statement`.

## Properties

`whileLoop` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `bodyStatement` | `statement` | The body of the loop |
| `conditionDeclaration` | `variableDeclaration?` | If a variable is declared in the condition expression, it is represented here; if it is not, this field is `null` |
| `conditionExpression` | `expression` | The expression in the condition of the loop |

**Inherits properties from:**

- astnode
- statement

## Example

## See also

allLoops
doWhileLoop,
forLoop,
forLoopEnhanced,
forLoopSimple
