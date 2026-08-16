---
title: "assignmentOperatorCompound"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/assignmentoperatorcompound.html"
content_id: "vMEuoCsN13JDlBfzcVp06w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:50.559281+00:00"
---

# assignmentOperatorCompound

Matches only compound assignment operators such as `a += b`.

This pattern only matches nodes of type `expression`.

## Properties

`assignmentOperatorCompound` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum` | Always `` `compound` `` |
| `operator` | `enum` (see binaryOperator) | The specific assignment operator matched |
| `sourceExpression` | `expression` | The expression that is evaluated, and that will be assigned |
| `targetExpression` | `expression` | The expression (typically a variable) that is being assigned |

**Inherits properties from:**

- astnode
- expression

## Example

Matches assignments such as `x += 5`.

## See also

assignmentOperator
