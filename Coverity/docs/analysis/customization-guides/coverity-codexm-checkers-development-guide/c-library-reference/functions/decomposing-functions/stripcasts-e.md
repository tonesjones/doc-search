---
title: "stripCasts( e )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/stripcasts-e-.html"
content_id: "83f1iqAI7DMEFzBzoz7e0A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:42.892408+00:00"
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

To examine the variable `i` in the assignment below:

  
 [image: C# code follows]   

```
    void example(int i, short s) {
        s = (short) i;
    }
```

... the function `stripCasts` could be used on the `sourceExpression` of the `assignmentOperator`.

## See also

stripBoxes,
stripCastsAndBoxes
