---
title: "sizeofOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sizeofoperator.html"
content_id: "IhiMD_lFn_9PpDltOj025w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:13.175120+00:00"
---

# sizeofOperator

Matches all size-of operations.

This pattern only matches nodes of type `expression`.

## Properties

`sizeofOperator` does not expose any new properties.

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern finds calls to `sizeof()` when the type is `int`:

  
 [image: CXM code follows]   

```
    pattern sizeOfOnInt {
        sizeofOperator {
            .operandType == integralType {
                .kind == `int`
            }
        }
    };
```

The pattern would locate the following call in C# target source:

  
 [image: C# code follows]   

```
    // Constant value 4:
    int intSize = sizeof(int);
```
