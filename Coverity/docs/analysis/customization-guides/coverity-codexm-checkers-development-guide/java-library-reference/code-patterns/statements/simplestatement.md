---
title: "simpleStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/simplestatement.html"
content_id: "jnL1Qb7ObXECFZajmyMxyw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:45.517238+00:00"
---

# simpleStatement

Matches individual execution statements.

The term *simple* derives from the fact that the these statements do not involve control flow.
Simple statements include assignments, function calls, and ordinary expressions.
They do not include variableDeclaration code.

This pattern only matches nodes of type `statement`.

## Properties

`simpleStatement` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression, such as a function call or an assignment |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches a simple statement that is a function call:

  
 [image: CXM code follows]   

```
    pattern simpleStatementFunctionCall {
        simpleStatement {
            .expression == functionCall
        }
    };
```
