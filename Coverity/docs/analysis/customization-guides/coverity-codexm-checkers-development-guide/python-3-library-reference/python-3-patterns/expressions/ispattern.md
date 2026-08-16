---
title: "isPattern"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/ispattern.html"
content_id: "oZwPNJANuXTE7zZ3hXKbpA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:17.081410+00:00"
---

# isPattern

Matches a Python pattern (not to be confused with a CodeXM pattern) that matches by performing a dynamic type check.

For example, `isPattern` would match the following Python code:

[image: Python code follows]

```
    case [x, y]: return;
```

`isPattern` has an optional subpattern that is further matched against the expression if the type check succeeds.

This pattern only matches nodes of type `statement`.

## Properties

`isPattern` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `subPattern` | `pattern` | Further pattern matches |
| `type` | `type` | The type to match |

**Inherits properties from:**

- astnode
- statement

## Example

The following pattern matches an expression with a Python pattern that matches a `case` statement that uses a tuple expression
such as `case [x, y]`:

[image: CXM code follows]

```
    pattern switchWithTuplePattern {
        matchStatement as sw where
            exists stmt in sw.caseList where
                stmt matches caseStatement {
                    .valueExpression == isPattern {
                        .subPattern == tuplePattern
                    }
                }
    };
```

## See Also

expressionPattern,
namedPattern
