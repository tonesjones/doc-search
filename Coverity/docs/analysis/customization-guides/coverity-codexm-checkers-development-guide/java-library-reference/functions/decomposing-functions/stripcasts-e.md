---
title: "stripCasts( e )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/stripcasts-e-.html"
content_id: "1SRF7Vdu5aSk8BCwzmXcCQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:47.447088+00:00"
---

# stripCasts( e )

Strips an outermost cast, if one is present, and returns the underlying expression.

If the expression consists of sub-expressions which themselves are being cast, those casts are also stripped.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `e` | `expression` | The expression to strip casts from |
| ***return value*** | `expression` | The expression with casts removed |

## Example

To examine the variable `i` in the Java assignment below:

  
 [image: Java code follows]   

```
    void example(int i, short s) {
        class="targetline" s = (short) i;
    };
```

... the CodeXM function `stripCasts` could be used on the `sourceExpression` of the `assignmentOperator`.

## See also

stripBoxes,
stripCastsAndBoxes
