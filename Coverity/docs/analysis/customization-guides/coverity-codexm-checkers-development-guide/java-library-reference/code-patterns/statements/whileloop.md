---
title: "whileLoop"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/whileloop.html"
content_id: "5x0hbK6YOVXfbs9Y0ZbRFA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:49.020224+00:00"
---

# whileLoop

Matches standard `while` loops.

This matches standard `while` loops, as opposed to `do ... while` and `for` loops.

This pattern only matches nodes of type `statement`.

## Properties

`whileLoop` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `bodyStatement` | `statement` | The body of the loop |
| `conditionDeclaration` | `variableDeclaration?` | If a variable is declared in the condition expression, it is represented here; `null` if there is no declaration |
| `conditionExpression` | `expression` | The expression in the condition of the loop |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches situations where a `while` loop has a Boolean constant value as its condition:

  
 [image: CXM code follows]   

```
    pattern whileLoopBoolConstantCondition {
        whileLoop {
            .conditionExpression == booleanLiteral
        }
    };
```

## See also

doWhileLoop,
forLoop,
forLoopEnhanced,
forLoopSimple
