---
title: "handler"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/handler.html"
content_id: "UTCTpU82swA6GFgD6lOQHQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:40.666864+00:00"
---

# handler

Represents exception handlers in `try/catch` blocks.

## Properties

`handler` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `body` | `blockStatement` | The body of the exception handler |
| `variable` | `localVariableSymbol` | The variable representing the exception caught |

## Example

The following CodeXM pattern matches handlers that declare a variable named `Exception` in `catch` statements;
for example, `catch ( Exception ex )`:

  
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
