---
title: "addressOf"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/addressof.html"
content_id: "uJRSmlw3JGwRAVZDy6FPNA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:39.390691+00:00"
---

# addressOf

Matches instances of the `&` ("address of") operator.

This pattern only matches nodes of type `expression`.

## Properties

`addressOf` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `operandExpression` | `expression` | The operand of the `&` operator (the object whose address is being retrieved) |

**Inherits properties from:**

- astnode
- expression

## Example

The `addressOf` pattern matches the `&num` in the following C/C++ code:

  
 [image: C/C++ code follows]   

```
int *p_num = &num;
```

The following CodeXM pattern matches the `addressOf` of any global variable:

  
 [image: CXM code follows]   

```
    pattern addressOfGlobal {
        addressOf {
            .operandExpression == variableReference {
                .scope == `global`
            }
        }
    };
```
