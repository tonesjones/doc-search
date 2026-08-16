---
title: "assignmentOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/assignmentoperator.html"
content_id: "dE1mlbE0RF2gC15qjhfnzA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:49.907350+00:00"
---

# assignmentOperator

Matches all forms of the assignment operator.

This pattern only matches nodes of type `expression`.

## Properties

`assignmentOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum` (see below) | The kind of assignment operator matched |
| `operator` | `enum` (see binaryOperator) | The specific assignment operator matched |
| `sourceExpression` | `expression` | The expression that is evaluated, and that will be assigned |
| `targetExpression` | `expression` | The expression (typically a variable) that is being assigned |

These are the possible values for the `kind` property:

| Name | Description |
| --- | --- |
| `` `compound` `` | Compound assignment, as in `+=` |
| `` `simple` `` | Simple assignment via `=` |

**Inherits properties from:**

- astnode
- expression

## Example

Matches expressions such as `x = 5` or `x += 5`.
