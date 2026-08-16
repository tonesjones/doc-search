---
title: "forLoopSimple"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/forloopsimple.html"
content_id: "le40TqWiKKDOK688viNrZA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:12.718126+00:00"
---

# forLoopSimple

Matches simple `for` loops of the form `for (int i = 0; i < 10; i++)`.

This pattern only matches nodes of type `statement`.

## Properties

`forLoopSimple` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `bodyStatement` | `statement` | The body of the loop |
| `conditionDeclaration` | `variableDeclaration?` | If a variable is declared in the second clause of the loop, it is represented here; otherwise this field is `null` |
| `conditionExpression` | `statement` | The conditional clause for the loop |
| `initializationStatement` | `statement` | The initialization clause for the loop |
| `kind` | `enum ForLoopKind` | Always `` `simple` ``. See ForLoopKind. |
| `updateStatement` | `statement` | The update clause of the loop |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches a simple `for` loop that uses a postfix increment expression to update its iterations:

  
 [image: CXM code follows]   

```
    pattern postFixUpdate {
        forLoopSimple {
            .updateStatement == simpleStatement {
                .expression == incrementOperator {
                    .kind == `postfix`
                }
            }
        }
    };
```

## See also

allLoops,
forLoop
