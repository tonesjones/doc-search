---
title: "selectStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/selectstatement.html"
content_id: "roNg4CiieKt3g6Qi45WfeA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:18.902875+00:00"
---

# selectStatement

Matches `select` statements.

This pattern only matches nodes of type `statement`.

## Properties

`selectStatement` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `branchStatement` | `statement` | The body of the `select` statement, including all the statements contained in its `case` and `default` clauses. |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches `select` statements that have
a `default` clause:

  
 [image: CXM code follows]   

```
    pattern selectWithDefault {
        selectStatement as sw where
            exists stmt in sw.caseList where
                stmt matches defaultStatement
    }
```

## See also

caseStatement,
defaultStatement
