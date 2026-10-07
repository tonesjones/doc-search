---
title: "castOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/castoperator.html"
content_id: "CWRhpG5fssFmQsgYE8aTvQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:47.835218+00:00"
---

# castOperator

Matches all kinds of casts.

This pattern only matches nodes of type `expression`.

## Properties

`castOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `isImplicitCast` | `bool` | Whether or not this cast is implicit |
| `operandExpression` | `expression` | The cast operand |

**Inherits properties from:**

- astnode
- expression
