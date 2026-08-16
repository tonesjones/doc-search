---
title: "isPattern"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/ispattern.html"
content_id: "dyl2ZVyHfzftgdRnDkj35A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:40.906653+00:00"
---

# isPattern

Matches C# patterns that perform dynamic type checks.

In C#, you can used an `is` pattern (not to be confused with a CodeXM pattern) to perform a dynamic type check.
The C# pattern can have an optional subpattern: If the type check succeeds, the subpattern is matched against the expression.
This pattern is usually followed by a namedPattern.

For example, the following C# snippet matches the variable `o` against the type `int`.
If the variable is *not* an integer, the function containing this statement returns:

  
 [image: C# code follows]   

```
    if ( !(o is int) ) return;
```

## Properties

`isPattern` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `subPattern` | `pattern` | The subpattern to match if the type check succeeds |
| `type` | `type` | The type to match against |

**Inherits properties from:**

- astnode
- expression

## Example

The following pattern matches an expression that contains the C# pattern-match
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
namedPattern,
patternMatchExpression
