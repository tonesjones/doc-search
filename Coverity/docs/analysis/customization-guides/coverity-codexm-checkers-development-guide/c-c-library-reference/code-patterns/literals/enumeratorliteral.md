---
title: "enumeratorLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/enumeratorliteral.html"
content_id: "y34EALickHEncCgZH3ZmoQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:34.999191+00:00"
---

# enumeratorLiteral

Matches an enumerator.

In C, enumerators are integers; this pattern will match even if the enumerator is implicitly cast to
the corresponding `enum` type.

This pattern only matches nodes of type `expression`.

## Properties

`enumeratorLiteral` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `enumerator` | `enumeratorSymbol` | The enumerator being referenced. |

## Inherits properties from:

- astnode
- expression

## Example

The following pattern matches the assignment of an enumerator named `E1` in an enumeration called `E`:

  
 [image: CXM code follows]   

```
assignmentOperator {
    .sourceExpression == enumeratorLiteral {
        .enumerator == {
            .identifier == "E1";
            .ownerEnumType.identifier == "E"
        }
    }
};
```

Here is the source it would match:

  
 [image: C code follows]   

```
enum E {
    E1,
    E2
}

enum E e;
e = E1;     // <-- The pattern matches this
```

## See also

enumeratorSymbol
