---
title: "stripImplicitCasts( e )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/stripimplicitcasts-e-.html"
content_id: "06nxfm8o5pcqQIginJgd7g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:48.850629+00:00"
---

# stripImplicitCasts( e )

Decomposes expressions with implicit casts; that is, casts that are not explicitly placed in the source code, but are implicitly created by Java.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `e` | `expression` | The expression to strip casts from. |
| ***return value*** | `expression` | The expression, free of casts. If the expression passed to this function is not a cast, `stripImplicitCasts` simply returns the expression itself. |

## Example

When assigning between integer kinds, Java can generate implicit casts. For example:

  
 [image: Java code follows]   

```
    short s = 5;
    long l;
    l = s;      // Implicit cast here
```

In CodeXM, to match all assignments from `short` integers, you might need to use `stripImplicitCasts` as follows:

  
 [image: CXM code follows]   

```
    pattern allAssignmentsFromShorts {
        assignmentOperator as assignment where
            stripImplicitCasts(assignment.sourceExpression) matches
                variableReference as v
                && v.type matches integerType { .kind == `short` }
    };
```
