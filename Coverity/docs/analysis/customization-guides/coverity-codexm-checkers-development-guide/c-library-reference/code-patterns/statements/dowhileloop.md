---
title: "doWhileLoop"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/dowhileloop.html"
content_id: "7BudoTE6d5Jyunus22d~mQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:30:54.619606+00:00"
---

# doWhileLoop

Matches `do ... while` loops.

This pattern only matches nodes of type `statement`.

## Properties

`doWhileLoop` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `bodyStatement` | `statement` | The body of the loop |
| `conditionExpression` | `expression` | The condition expression of the loop |

**Inherits properties from:**

- astnode
- statement

## Example

The following pattern matches locations where a `do ... while` loop has a Boolean constant value as its condition:

  
 [image: CXM code follows]   

```
    pattern doWhileLoopBoolConstantCondition {
        doWhileLoop {
            .conditionExpression == booleanLiteral
        }
    };
```

## See also

allLoops
forLoop,
forLoopEnhanced,
forLoopSimple,
whileLoop
