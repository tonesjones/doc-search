---
title: "awaitOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/awaitoperator.html"
content_id: "2jbe_K~b8lGdNX_uPLZ6yg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:29.487905+00:00"
---

# awaitOperator

Matches `await` operators.

This pattern only matches nodes of type `expression`.

## Properties

`awaitOperator` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `operandExpression` | `expression` | The thing being thrown by the operator |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern finds all `await` occurrences in a function named `example()`:

  
 [image: CXM code follows]   

```
    pattern awaitExample {
        awaitOperator {
            .operandExpression == functionCall {
                .calledFunction == functionSymbol {
                    .simpleName == "example"
                }
            }
        }
    };
```
