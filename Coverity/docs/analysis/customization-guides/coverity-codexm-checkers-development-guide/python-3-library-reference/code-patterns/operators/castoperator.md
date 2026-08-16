---
title: "castOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/castoperator.html"
content_id: "Ao0E9JfcWKvIOJzC8oVyMA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:59.795278+00:00"
---

# castOperator

Matches implicit cast operations.

Python does not officially support cast operations, but this pattern is included because some Python interpreters do perform casting.

This pattern only matches nodes of type `expression`.

## Properties

`castOperator` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `operandExpression` | `expression` | The expression whose type is being cast |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches a cast from an integer literal expression:

[image: CXM code follows]

```
    pattern castFromInt {
        castOperator {
            .operandExpression == integerLiteral
        }
    };
```
