---
title: "floatType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/floattype.html"
content_id: "~MAiy7Ft3baKZhIf1rFEQQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:55.135261+00:00"
---

# floatType

Matches the Java floating-point types.

## Properties

`floatType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum floatKind` | Either `` `float` `` or `` `double` ``; see floatKind |
| `alignmentInBytes` | `int` | The alignment of the type, in bytes |
| `sizeInBits` | `int` | The total size of the float, in bits. The representation is implementation-defined, so bits for exponent and mantissa are not described. |
| `sizeInBytes` | `int` | The size of the float, in bytes |

## Example

The following CodeXM pattern matches any expression that has the type `double`:

  
 [image: CXM code follows]   

```
   node matches expression { .type == floatType { .kind == `double` } };
```
