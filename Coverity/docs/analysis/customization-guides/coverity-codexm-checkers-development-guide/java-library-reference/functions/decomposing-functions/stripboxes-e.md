---
title: "stripBoxes( e )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/stripboxes-e-.html"
content_id: "RE1WeptewK~LeIb3U_XNxQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:46.719842+00:00"
---

# stripBoxes( e )

Strips an outermost box expression, if one is present, and returns the underlying expression.

If the expression consists of sub-expressions which themselves are box expressions, those expressions are also stripped.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `e` | `expression` | The expression to strip boxes from |
| ***return value*** | `expression` | The expression with the boxes removed |

## Example

In the following Java snippet:

  
 [image: Java code follows]   

```
    int[] lst = {0, 1, 2};
    Integer sum = new Integer(0);
    for (int i : lst) {
        sum += i;       // Box expression here
    };
```

... to examine the variable on the right-hand side of the `assignmentOperatorCompound` ( `+=` ),
the function `stripBoxes()` could be called, passing it the `sourceExpression` of that assignment expression.

## See also

stripCasts,
stripCastsAndBoxes
