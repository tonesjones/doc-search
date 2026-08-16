---
title: "namedPattern"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/namedpattern.html"
content_id: "CEm21Ji7ySYn2ehQq82kzw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:17.820178+00:00"
---

# namedPattern

Matches a Python named pattern (not to be confused with a CodeXM pattern) that binds a name to a value.
The named pattern is often a subpattern returned by `isPattern`.

For example, `namedPattern` would match the following Python code:

[image: Python code follows]

```
    command = "laugh"
        match command:
            case "laugh" as x:
                safe_action = x
```

This pattern only matches nodes of type `statement`.

## Properties

`namedPattern` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `variable` | `variable` | The variable that has been bound |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches an expression with a Python pattern-match expression `case obj` as `x` where the value is named to
a variable for use in `case` statements:

[image: CXM code follows]

```
    pattern switchWithNamedPattern {
        matchStatement as sw where
            exists stmt in sw.caseList where
                stmt matches caseStatement {
                    .valueExpression == namedPattern 
                }
    };
```

## See Also

expressionPattern,
isPattern
