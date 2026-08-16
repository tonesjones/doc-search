---
title: "caseStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/casestatement.html"
content_id: "ubHwacpM7M~O73sO2vXZig"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:36.250060+00:00"
---

# caseStatement

Matches individual `case` statements.

This pattern does *not* match the `default` case.
See defaultStatement.

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

The following CodeXM pattern matches all case statements that are for the integer value `1`:

  
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
