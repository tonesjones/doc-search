---
title: "forEachLoop"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/foreachloop.html"
content_id: "9Tpkv6z9BXK92cn~dRPLvA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:23.460026+00:00"
---

# forEachLoop

Matches `for` loop statements.

This pattern only matches nodes of type `statement`.

## Properties

`forEachLoop` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `bodyStatement` | `statement` | The statement that the loop repeatedly executes. Frequently this is a block statement. |
| `elseStatement` | `statement` | The statement executed when the loop terminates. |
| `isAsync` | `bool` | `true` if the loop is declared as `async` (Python 3) |
| `iterableExpression` | `expression` | The iterable object |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern finds all `for` loops over empty literal lists:

[image: CXM code follows]

```
    pattern forOverListLiteral {
        forEachLoop {
            .iterableExpression == listLiteral
        } as f where f.iterableExpression.expressions.empty
    };
```

## See also

breakStatement,
whileLoop
