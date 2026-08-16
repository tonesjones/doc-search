---
title: "whileLoop"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/whileloop.html"
content_id: "8d3POEAV2ahXDAOy3jpF3g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:28.236809+00:00"
---

# whileLoop

Matches `while` loop statements.

This pattern only matches nodes of type `statement`.

## Properties

`whileLoop` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `bodyStatement` | `statement` | The statement in the loop. Often this is a block statement. |
| `conditionExpression` | `expression` | The loop condition |
| `elseStatement` | `list<statement>?` | The statements executed when the loop terminates; `null` if there are none |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern finds all `while` loops whose condition is the
Boolean value `True`:

[image: CXM code follows]

```
    pattern whileTrueLoop {
        whileLoop {
            .conditionExpression == booleanLiteral {
                .value == true
            }
        }
    };
```

## See also

breakStatement,
forEachLoop
