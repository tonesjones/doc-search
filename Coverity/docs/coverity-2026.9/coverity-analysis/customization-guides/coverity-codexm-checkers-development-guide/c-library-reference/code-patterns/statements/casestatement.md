---
title: "caseStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/casestatement.html"
content_id: "PXVHgY7sGAe2f3m7bPjwHg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:25.077385+00:00"
---

# caseStatement

Matches individual `case` statements.

This pattern *does not* match the `default` statement.
See the defaultStatement pattern.

This pattern only matches nodes of type `statement`.

## Properties

`caseStatement` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `valueExpression` | `expression` | The value associated with the case |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches all `case` statements that have a case for the integer value `1`:

  
 [image: CXM code follows]   

```
    pattern caseOne {
        caseStatement {
            .valueExpression == integerLiteral { .value == 1 }
        }
    };
```

## See also

defaultStatement,
switchStatement
