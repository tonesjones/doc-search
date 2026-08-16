---
title: "integralType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/integraltype.html"
content_id: "fhuSXBT3Q1oyUtfME0IC7A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:20.288274+00:00"
---

# integralType

Matches all C# integer types.

This pattern only matches nodes of type `type`.

## Properties

`integralType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `alignmentInBytes` | `int` | The alignment of the type, in bytes |
| `kind` | Subset of `enum intKind` | The type of integer: `` `int` ``, `` `short` ``, `` `long` ``, or `` `byte` ``; see also intKind |
| `sizeInBits` | `int` | The size of the type, in bits |
| `sizeInBytes` | `int` | The size of the type, in bytes |

## Example

The following CodeXM pattern uses the `kind` property to match a C# `long` type:

[image: CXM code follows]

```
    t matches integralType { .kind == `long` };
```

## See also

charType,
intKind
