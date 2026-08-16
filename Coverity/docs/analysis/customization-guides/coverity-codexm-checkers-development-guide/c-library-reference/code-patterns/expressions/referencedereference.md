---
title: "referenceDereference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/referencedereference.html"
content_id: "CzO9V6YK0TVJxEehZhohOg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:46.671048+00:00"
---

# referenceDereference

Matches locations where a reference-type expression has been dereferenced.

This pattern only matches nodes of type `expression`.

## Properties

`referenceDereference` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `referencedExpression` | `expression` | The expression being dereferenced |

**Inherits properties from:**

- astnode
- expression

## Example

For the following C# function:

  
 [image: C# code follows]   

```
    int myFunction(MyObject o) {
        return o.a + o.b;         // "o" is dereferenced twice here
    };
```

... you might use the following CodeXM pattern to match the dereferences of the parameter `o`:

  
 [image: CXM code follows]   

```
    pattern addingWithReference {
        binaryOperator as b where
            b.operation == `+`
                && ( (b.lhsExpression matches fieldAccess {
                                .objectExpression == referenceDereference 
                      } )
                ||   (b.rhsExpression matches fieldAccess {
                          .objectExpression == referenceDereference 
                      } )
                   )
    };
```

## See also

referenceType
