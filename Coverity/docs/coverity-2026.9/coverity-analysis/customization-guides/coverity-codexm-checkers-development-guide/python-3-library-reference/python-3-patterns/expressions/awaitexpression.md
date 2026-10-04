---
title: "awaitExpression"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/awaitexpression.html"
content_id: "JcF_1Fbs8IDJHLjLqg7XuQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:53.094025+00:00"
---

# awaitExpression

This pattern matches the Python 3 `await` expression.

This pattern only matches nodes of type `expression`.

## Properties

`awaitExpression` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression being awaited |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches an `await` expression
that calls a function named `ping()`:

[image: CXM code follows]

```
    pattern awaitPing {
        awaitExpression {
            .expression == functionCall {
                .simpleName == "ping"
            }
        }
    };
```
