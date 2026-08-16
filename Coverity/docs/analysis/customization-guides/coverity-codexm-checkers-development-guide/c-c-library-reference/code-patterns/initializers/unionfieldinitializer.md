---
title: "unionFieldInitializer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/unionfieldinitializer.html"
content_id: "SBA47qukIIAJz5wiTY500Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:57.698575+00:00"
---

# unionFieldInitializer

Matches union field initializers.

## Properties

`unionFieldInitializer` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `field` | `fieldSymbol` | The field in the union being initialized |
| `initializer` | `initializer` | The initializer for this field |

**Inherits properties from:**

- astnode
- initializer

## Example

Given the following declaration in target code:

  
 [image: C/C++ code follows]   

```
union U {
    int i;
    float f;
};
```

... the `unionFieldInitializer` CodeXM pattern matches the following code,
such that the `.field` property refers to `i`,
whereas the `.initializer` property is `expressionInitializer`:

  
 [image: C/C++ code follows]   

```
union U val = { i : 0 };
```

The following CodeXM pattern matches a union initialized using `int` only; that is, it matches the initializer
`{ i: 0 }`
but does not match `{ f: 0.0 }`:

  
 [image: C/C++ code follows]   

```
    pattern UnionIntInitializer {
        unionFieldInitializer {
            .initializer == expressionInitializer {
                .expression == intLiteral
            }
        }
    };
```
