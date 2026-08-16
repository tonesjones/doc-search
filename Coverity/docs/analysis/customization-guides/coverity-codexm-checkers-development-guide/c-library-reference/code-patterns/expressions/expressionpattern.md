---
title: "expressionPattern"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/expressionpattern.html"
content_id: "VT~m~36t2OlDKjwDlAVj8g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:35.992284+00:00"
---

# expressionPattern

Matches C# query-expression patterns.

This pattern matches C# patterns (not to be confused with CodeXM patterns).
In C#, a query-expression pattern matches other portions of the C# code.

  
 [image: C# code follows]   

```
    if (o is null) return;          // Matches against the expression 'null'
```

## Properties

`expressionPattern` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The C# expression used for matching |

**Inherits properties from:**

- astnode
- expression

## Example

The following pattern matches an expression that contains the C# pattern match
expression `is null`:

  
 [image: CXM code follows]   

```
    pattern isNullMatchPattern {
        patternMatchExpression {
            .matchPattern == expressionPattern {
                .expr == nullLiteral
            }
        }
    };
```

## See also

isPattern,
namedPattern,
patternMatchExpression
