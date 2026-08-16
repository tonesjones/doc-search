---
title: "namedPattern"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/namedpattern.html"
content_id: "U3dfyN5nKYqvCQLWELI~Vg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:43.059131+00:00"
---

# namedPattern

Matches C# named patterns that bind names to values.

In C#, you can used a named pattern (not to be confused with a CodeXM pattern) to bind a name to a value:
usually this follows an isPattern expression, as in the following example:

  
 [image: C# code follows]   

```
    if (!(o is int i)) return;      // Two pattern matches here:
                                    //   1. is int -> isPattern
                                    //   2. is int i -> namedPattern where
                                    //      New name 'i' is bound to the
                                    //      value of o
    var z = i;                      // Using the new name 'i'
```

## Properties

`namedPattern` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `variable` | `variable` | The variable the value is being bound to |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches an expression that contains the C# pattern-match
expression `is int i`:

  
 [image: CXM code follows]   

```
    pattern isIntWithNameMatchPattern {
        patternMatchExpression {
            .matchPattern == isPattern {
                .type == integralType {
                    .kind == `int`
                }
                .subPattern = namedPattern
            }
        }
    };
```

## See also

expressionPattern,
isPattern,
patternMatchExpression
