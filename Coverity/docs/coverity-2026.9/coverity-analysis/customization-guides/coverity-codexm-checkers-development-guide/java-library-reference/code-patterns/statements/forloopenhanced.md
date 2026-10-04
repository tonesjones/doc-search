---
title: "forLoopEnhanced"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/forloopenhanced.html"
content_id: "JLPZ9vEIiPVg60Tfqm83jg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:39.509847+00:00"
---

# forLoopEnhanced

Matches enhanced `for` loops; that is, loops of the form `for (int i : numbers)`.

## Properties

`forLoopEnhanced` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `bodyStatement` | `statement` | The body of the loop |
| `containerExpression` | `expression` | The container being iterated |
| `kind` | `enum ForLoopKind` | Always `` `enhanced` ``; see ForLoopKind |
| `loopVariable` | `localVariableSymbol` | The iterator for the loop |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern finds all enhanced `for` loops over an array of integers:

  
 [image: CXM code follows]   

```
    pattern enhancedForIntegers {
        forLoopEnhanced {
            .containerExpression == expression {
                .type == arrayType {
                    .elementType == integerType
                }
            }
        }
    };
```

## See also

forLoop,
forLoopSimple
