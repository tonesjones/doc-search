---
title: "switchStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/switchstatement.html"
content_id: "ch9tksLHxWCNmHMFOfRCiw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:46.249495+00:00"
---

# switchStatement

Matches `switch` statements, including all statements contained in the various `case` and `default` clauses.

This pattern only matches nodes of type `statement`.

## Properties

`switchStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `bodyStatement` | `statement` | The body of the `switch` statement |
| `caseList` | `list<statement>` | A list of targets for this `switch` statement |
| `conditionDeclaration` | `variableDeclaration?` | If a variable is declared in the `.conditionExpression`, it is identified here; if no variable is declared, this value is `null` |
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
