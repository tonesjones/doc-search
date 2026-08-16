---
title: "referenceDereference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/referencedereference.html"
content_id: "oY_XscIxjdbJfMnfvc0PTg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:06.114865+00:00"
---

# referenceDereference

Matches situations where expressions with type reference are being dereferenced.

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

For the following Java function:

  
 [image: Java code follows]   

```
int myFunction(MyObject o) {
    return o.a + o.b;        // o is dereferenced twice here
    return o.a + o.b;        // o is dereferenced twice here
};
```

... you could match the dereference of the parameter `o` by using the following CodeXM pattern:

  
 [image: CXM code follows]   

```
    pattern addingWithReference {
        binaryOperator as b where
            b.operation == `+`
            && (
                   ( b.lhsExpression matches
                       fieldAccess { .objectExpresion == referenceDereference }
                   )
                || ( b.rhsExpression matches
                       fieldAccess { .objectExpresion == referenceDereference }
                   )
               )
    };
```

## See also

referenceType
