---
title: "sizeofOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sizeofoperator.html"
content_id: "GvCoRHPjAoMfe6lZkyw~vw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:52.376977+00:00"
---

# sizeofOperator

Matches instances of the `sizeof()` operator,
regardless of whether the operand is an expression or a type.

This pattern only matches nodes of type `expression`.

## Properties

`sizeofOperator` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum sizeofKind` | `` `sizeofExpression` `` or `` `sizeofType` ``; see sizeofKind |

**Inherits properties from:**

- astnode
- expression

## See also

sizeofOperatorExpression and
sizeofOperatorType.
