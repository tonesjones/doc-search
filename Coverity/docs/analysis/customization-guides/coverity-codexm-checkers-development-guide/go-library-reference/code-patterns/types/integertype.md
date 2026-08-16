---
title: "integerType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/integertype.html"
content_id: "NyJkLz98kgRYf_6EQO6lZA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:27.795935+00:00"
---

# integerType

Matches all integer types that Go recognizes.

This pattern only matches nodes of type `type`.

## Properties

`integertype` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `alignmentInBytes` | `int` | The alignment of the type, in bytes |
| `kind` | `enum intKind` | The kind of integer type: See intKind. |
| `sizeInBits` | `int` | The size of the type, in bits |
| `sizeInBytes` | `int` | The size of the type, in bytes |

## Example

The following CodeXM pattern uses the `kind` property to match a `uint8` type:

  
 [image: CXM code follows]   

```
   t matches integertype { .kind == `uint8` };
```

## See also

boolType
