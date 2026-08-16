---
title: "stripCasts( expressionString )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/stripcasts-expressionstring-.html"
content_id: "9AI9wb2KVG1fD7OBtW3XOw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:30:24.589581+00:00"
---

# stripCasts( expressionString )

Strips an outermost cast, if present, to return the underlying expression.

If the expression consists of subexpressions that themselves are being cast, those casts are also stripped.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `expressionString` | `expression` | The expression to strip casts from |
| ***return value*** | `expression` | The expression without casts |

## Example

Given the following target source:

  
 [image: C/C++ code follows]   

```
int *ptr;
void *a = (void *) ptr;
```

... the following CodeXM pattern uses `stripCasts()`
to match `*a`:

  
 [image: CXM code follows]   

```
    pattern intPointerReference {
        stripCasts( expr ) matches variableReference {
            .type == pointerType {
                .pointerToType == intType;
            }
        }
    };
```
