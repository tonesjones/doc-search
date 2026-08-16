---
title: "refTypeExpression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/reftypeexpression.html"
content_id: "_lJWl4OD6VHu3b9vE2RANw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:47.495492+00:00"
---

# refTypeExpression

Matches expressions that make references by using the `__reftype` construct.

The following C# code is an example of using `__reftype`:

  
 [image: C# code follows]   

```
    void Test_RefType(System.TypedReference typedRef) {
        var res01 = __reftype(typedRef);
    };
```

This pattern only matches nodes of type `expression`.

## Properties

`refTypeExpression` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression being used |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches all make-reference-type expressions from function calls:

  
 [image: CXM code follows]   

```
    pattern makeRefToFunctionCallExpression {
        refTypeExpression {
            .expression == functionCall
        }
    };
```
