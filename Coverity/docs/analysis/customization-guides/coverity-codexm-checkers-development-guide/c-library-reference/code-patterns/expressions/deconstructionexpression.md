---
title: "deconstructionExpression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/deconstructionexpression.html"
content_id: "qJzbhomMepfdsy2U4zUxQQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:33.198834+00:00"
---

# deconstructionExpression

Matches deconstruction expressions.

This pattern only matches nodes of type `expression`.

## Properties

`deconstructionExpression` produces a record that contains the following properties:

|  |  |  |
| --- | --- | --- |
| `sourceExpression` | `expression` | The source of the deconstruction |
| `targetStatements` | `list<statement>` | The targets of the deconstruction |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches the deconstruction of value tuples:

  
 [image: CXM code follows]   

```
    pattern tupleDeconstruction {
        deconstructionExpression {
            .sourceExpression == expression {
                .type = valueTupleType
            }
        }
    };
```
