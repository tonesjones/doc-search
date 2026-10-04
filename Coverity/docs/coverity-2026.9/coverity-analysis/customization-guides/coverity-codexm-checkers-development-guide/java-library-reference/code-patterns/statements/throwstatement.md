---
title: "throwStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/throwstatement.html"
content_id: "QG0jGlifK46J99~YpR8llQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:39.962385+00:00"
---

# throwStatement

Matches `throw` statements.

This pattern only matches nodes of type `statement`.

## Properties

`throwStatement` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `conditionExpression` | `expression` | The thing being thrown by the statement |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches when an expression with type `MyException` is thrown:

  
 [image: CXM code follows]   

```
    pattern throwMyException {
        throwStatement {
            .expression == expression {
                .type == classType { .simpleName == "MyException" }
            }
        }
    };
```
