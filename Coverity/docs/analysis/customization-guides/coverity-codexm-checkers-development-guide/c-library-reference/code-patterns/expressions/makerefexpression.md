---
title: "makeRefExpression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/makerefexpression.html"
content_id: "tRbaA6urECx6x6Z4p5yDVg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:41.570226+00:00"
---

# makeRefExpression

Matches expressions that use the C# keyword `ref` to make references.

This pattern only matches nodes of type `expression`.

## Properties

`makeRefExpression` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression being used |

**Inherits properties from:**

- astnode
- expression

## Example

The following pattern matches all make reference expressions within functions:

  
 [image: CXM code follows]   

```
    pattern makeRefToFunctionCallExpression {
        makeRefExpression {
            .expression == functionCall
        }
    };
```
