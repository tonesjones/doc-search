---
title: "forLoopEnhanced"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/forloopenhanced.html"
content_id: "OBKj9GgsrJvnsPdo0_qcUQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:30:57.519869+00:00"
---

# forLoopEnhanced

Matches enhanced `for` loops of the form `foreach (int i in numbers)`.

Matches only nodes of type `statement`.

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

The following pattern finds all enhanced `for` loops over an array of integers:

[image: CXM code follows]

```
    pattern enhancedForIntegers {
        forLoopEnhanced {
            .containerExpression ==
                expression {
                    .type == arrayType {
                        .elementType == integralType
                    }
                }
        }
    };
```

## See also

allLoops
forLoop,
forLoopSimple
