---
title: "expressionPattern"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/expressionpattern.html"
content_id: "F63ZyjQ8GpG2li5Q8pc63Q"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:53.142660+00:00"
---

# expressionPattern

Matches a Python pattern (not to be confused a CodeXM pattern) that matches a Python pattern that uses a Python expression.

For example, `expressionPattern` would match the following Python code:

[image: Python code follows]

```
    match command
        case None:           // matches against the expression 'None'
            return;
```

This pattern only matches nodes of type `statement`.

## Properties

`expressionPattern` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression used for matching. |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches an expression with a Python pattern that matches the expression `case None`, as shown above:

[image: CXM code follows]

```
    pattern switchWithCaseNone {
        matchStatement as sw where
            exists stmt in sw.caseList where
                stmt matches caseStatement {
                    .valueExpression == expressionPattern {
                        .expr == noneLiteral
                    }
                }
    };
```

## See Also

isPattern,
namedPattern
