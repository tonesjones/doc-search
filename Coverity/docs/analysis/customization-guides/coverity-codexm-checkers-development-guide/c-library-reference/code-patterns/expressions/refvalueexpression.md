---
title: "refValueExpression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/refvalueexpression.html"
content_id: "V_lk~ky1HI4aT5wtVUKZIw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:48.326249+00:00"
---

# refValueExpression

Matches expressions that make references by using the `__refvalue` construct.

The following C# code is an example of using `__refvalue`:

  
 [image: C# code follows]   

```
    void Test_RefValue(System.TypedReference typedRef) {
                var res01 = __refvalue(typedRef, int);
                };
```

This pattern only matches nodes of type `expression`.

## Properties

`refValueExpression` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression being used |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches all make-reference-value expressions from function calls:

  
 [image: CXM code follows]   

```
    pattern makeRefToFunctionCallExpression {
        refValueExpression {
            .expression == functionCall
        }
    };
```
