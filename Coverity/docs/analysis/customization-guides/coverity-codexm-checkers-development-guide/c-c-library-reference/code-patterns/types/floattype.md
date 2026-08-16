---
title: "floatType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/floattype.html"
content_id: "SznQy4lZ5GmZcJ5xJ1QNSA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:13.987636+00:00"
---

# floatType

Matches primitive floating-point types such as `float`,
`double`, or `long double`.

Remember:
The precision of floating-point representations depends on the target system's implementation.

## Properties

`floatType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum floatKind` | One of `` `float` ``, `` `double` ``, or `` `long double` ``; see floatKind |
| `alignmentInBytes` | `int?` | The alignment of the type, in bytes; `null` if the type is not aligned |
| `sizeInBytes` | `int` | The number of bytes required to store a value of this type |
| `sizeInBits` | `int` | The number of bits required to store a value of this type |

## Example

In the following source code, the pattern `floatType` matches the type
of a local variable, `x`:

  
 [image: C/C++ code follows]   

```
float x = 1.0;
```

The following CodeXM pattern matches `float` types,
but does not match `double` or `long double`:

  
 [image: CXM code follows]   

```
    node matches expression {
        .type == floatType {
            .kind == `float`
        }
    };
```
