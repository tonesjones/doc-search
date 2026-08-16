---
title: "patternMatchExpression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/patternmatchexpression.html"
content_id: "e4_1LyjD3Std6~1LIKAPvA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:44.439228+00:00"
---

# patternMatchExpression

Matches C# pattern-match expressions.

This pattern matches a C# pattern-match expression (not to be confused with
a CodeXM pattern). Pattern matching can be used in `if`
and `switch` statements.

## Properties

`patternMatchExpression` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression to be matched by the pattern |
| `matchPattern` | `pattern` | The pattern to match |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches an expression that contains the C# pattern-match
expression `is int`:

  
 [image: CXM code follows]   

```
    pattern isIntMatchPattern {
        patternMatchExpression {
            .matchPattern == isPattern {
                .type == integralType {
                    .kind == `int`
                }
            }
        }
    };
```

## See also

expressionPattern,
isPattern,
namedPattern
