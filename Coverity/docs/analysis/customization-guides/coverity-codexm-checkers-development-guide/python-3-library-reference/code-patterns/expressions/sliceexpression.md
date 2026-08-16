---
title: "sliceExpression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sliceexpression.html"
content_id: "0KA7i7zA2vwVUUiPZ3j5eg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:45.459154+00:00"
---

# sliceExpression

Matches slice expressions.

A slice expression selects a range of items in a sequence.
It has the following form:
`[<lowerBound>:<upperBound>:<stride>]`.

This pattern only matches nodes of type `expression`.

## Properties

`sliceExpression` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `lowerBoundExpression` | `expression?` | The lower bound of the sequence; `null` if this is absent |
| `strideExpression` | `expression?` | The stride of the sequence; `null` if this is absent |
| `uppperBoundExpression` | `expression?` | The upper bound of the sequence; `null` if this is absent |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches a slice that selects a sequence that uses a stride of `1`:

[image: CXM code follows]

```
    pattern strideOfOneSlice {
        sliceExpression {
            .strideExpression == integerLiteral {
                .value == 1
            }
        }
    };
```
