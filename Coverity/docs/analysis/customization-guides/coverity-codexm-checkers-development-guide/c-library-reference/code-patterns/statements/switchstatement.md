---
title: "switchStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/switchstatement.html"
content_id: "cWZbPg4TZYLhxheVLsVfag"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:03.725497+00:00"
---

# switchStatement

Matches entire `switch` statements, including all the statements
contained in their `case` and `default` clauses.

This pattern only matches nodes of type `statement`.

## Properties

`switchStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `bodyStatement` | `statement` | The body of the `switch` statement |
| `caseList` | `list<statement>` | A list of the case names for the `switch` statement |
| `conditionDeclaration` | `variableDeclaration?` | If a variable is declared in the `conditionExpression`, it is identified here; if it is not, this field is `null` |
| `conditionExpression` | `expression` | The condition for the `switch` statement |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches `switch` statements that have a `default` clause:

  
 [image: CXM code follows]   

```
    pattern switchWithDefault {
        switchStatement as sw where
            exists stmt in sw.caseList where
                stmt matches defaultStatement
    };
```

## See also

caseStatement,
defaultStatement
