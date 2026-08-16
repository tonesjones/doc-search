---
title: "floatType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/floattype.html"
content_id: "VHiCXiOdJydNNYwofCHhKg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:18.225688+00:00"
---

# floatType

Matches C# floating-point types.

This pattern only matches nodes of type `type`.

## Properties

`floatType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `alignmentInBytes` | `int` | The alignment of the type, in bytes |
| `kind` | `enum floatKind` | The kind of floating-point type. See floatKind. |
| `sizeInBits` | `int` | The total size of the float, in bits |
| `sizeInBytes` | `int` | The size of the float, in bytes |

Note:
The representation of floating types is implementation-defined, so CodeXM does not show how bits are apportioned between the exponent and the mantissa.

## Example

The following pattern matches any expression that has the C# type `double`:

[image: CXM code follows]

```
   node matches expression {
        .type == floatType { .kind == `double`}
    };
```
