---
title: "caseStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/casestatement.html"
content_id: "WmWnNEui71zuGs1M1TKfrg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:52.832085+00:00"
---

# caseStatement

Matches individual `case` statements.

This pattern only matches nodes of type `statement`.

## Properties

`caseStatement` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `valueExpression` | `expression` | The value associated with the case. |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches all `case` statements that are for the integer value `1`:

[image: CXM code follows]

```
    pattern caseOne {
        caseStatement {
            .valueExpression == integerLiteral { .value == 1 }
        }
    }
```

## See Also

matchStatement
