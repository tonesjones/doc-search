---
title: "matchStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/matchstatement.html"
content_id: "S8cZw4ZjuLESsJaZ0ywoIQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:13.038949+00:00"
---

# matchStatement

This pattern matches a `match` statement, which includes all `case` statements that are for the integer value `1`.

This pattern only matches nodes of type `statement`.

## Properties

`matchStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `bodyStatement` | `statement` | The body of the `match` statement. |
| `caseList` | `list<statement>` | A list of targets for this `match` statement. |
| `conditionDeclaration` | `variableDeclaration?` | If a variable is declared in the `conditionExpression`, it is identified here. |
| `conditionExpression` | `expression` | The condition for the switch statement. |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches `match` statements:

[image: CXM code follows]

```
    pattern switchWithCaseOne {
        switchStatement as sw where
            exists stmt in sw.caseList where
                stmt matches caseStatement {
                    .valueExpression == integerLiteral { .value == 1 }
                }
    }
```

## See Also

caseStatement
