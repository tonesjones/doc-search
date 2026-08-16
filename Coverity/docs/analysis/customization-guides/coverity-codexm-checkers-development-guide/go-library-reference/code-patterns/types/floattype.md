---
title: "floatType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/floattype.html"
content_id: "z1n5DapbUmBrZN57DQcTuQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:26.387511+00:00"
---

# floatType

Matches the Go types `float` and `complex`.

This pattern only matches nodes of type `type`.

## Properties

`floatType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum floatKind` | The kind of floating-point value: either `` `float` `` or `` `complex` ``. See floatKind. |
| `alignmentInBytes` | `int` | The alignment of the type, in bytes |
| `sizeInBits` | `int` | The total size of the float, in bits |
| `sizeInBytes` | `int` | The size of the float, in bytes |

Note:
The representation of floating types is implementation-defined, so CodeXM does not show how bits are apportioned between the exponent
and the mantissa.

## Example

The following CodeXM pattern matches any Go expression that has the type `float`:

  
 [image: CXM code follows]   

```
  node matches expression {
        .type == floatType { .kind == `float`}
    };
```
