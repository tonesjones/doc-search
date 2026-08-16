---
title: "handler"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/handler.html"
content_id: "K1jbUwnbuzh_xWmDdm65sw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:33.915818+00:00"
---

# handler

Represents exception handlers in a `try`/`catch` block.

## Properties

`handler` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `body` | `blockStatement` | The body of the exception handler |
| `variable` | `localVariableSymbol` | The variable that represents the exception being caught |

## Example

The following CodeXM pattern matches handlers that declare a variable named `Exception` in `catch` statements; for example, `catch ( Exception ex )`:

[image: CXM code follows]

```
    let exceptionHandleWithVar = pattern {
        handler {
            .variable == NonNull
        }
    }
    in
    pattern tryCatchWithVar {
        tryStatement as t where
            exists r in t.catchBlockList where
                r matches exceptionHandleWithVar
    };
```

## See also

tryStatement
