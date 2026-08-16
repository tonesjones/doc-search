---
title: "forLoopSimple"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/forloopsimple.html"
content_id: "aoO61nVovEKMviBEldfIMA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:41.336489+00:00"
---

# forLoopSimple

Matches simple `for` loops; that is, loops of the form `for (int i = 0; i < 10; i++)`.

## Properties

`forLoopSimple` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `bodyStatement` | `statement` | The body of the loop |
| `conditionDeclaration` | `variableDeclaration?` | If a variable is declared in the second clause of the loop, it is represented (returned) here |
| `conditionExpression` | `statement` | Conditional clause for the loop |
| `initializationStatement` | `statement` | Initialization clause for the loop |
| `kind` | `enum ForLoopKind` | Always `` `simple` ``; see ForLoopKind |
| `updateStatement` | `statement` | The update clause of the loop |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches a simple `for` loop that uses a postfix increment expression to update:

  
 [image: CXM code follows]   

```
    pattern postFixUpdate {
        forLoopSimple {
            .updateStatement == simpleStatement {
                .expression == incrementOperator { .kind == `postfix` }
            }
        }
    };
```

## See also

forLoop,
forLoopEnhanced
