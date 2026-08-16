---
title: "assignmentOperatorSimple"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/assignmentoperatorsimple.html"
content_id: "r2~57dPdgAUr3XxloCAAWw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:50.281268+00:00"
---

# assignmentOperatorSimple

Matches only simple assignments such as `a = 1`.

Even though variable declarations look similar to assignment operators, this pattern does not match
variable declarations. See variableDeclaration.

This pattern only matches nodes of type `expression`.

## Properties

`assignmentOperatorSimple` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum assignKind` | Always `` `simple` ``. See assignKind. |
| `operator` | `enum` | Always `` `=` `` |
| `sourceExpression` | `expression` | The expression on the right-hand side of the assignment operator |
| `targetExpression` | `expression` | The expression on the left-hand side of the assignment operator |

**Inherits properties from:**

- astnode
- expression

## Example

## See also

assignmentOperator,
assignmentOperatorCompound
