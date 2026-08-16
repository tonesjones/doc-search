---
title: "boolType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/booltype.html"
content_id: "kRiEM~uH1GH_GYYAY9gF0g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:24.922151+00:00"
---

# boolType

Matches the `bool` type.

This pattern only matches nodes of type `type`.

## Properties

`boolType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `alignmentInBytes` | `int` | The alignment of the type, in bytes |
| `sizeInBits` | `int` | The size of the Boolean, in bits |
| `sizeInBytes` | `int` | The size of the Boolean, in bytes |

## Example

The following CodeXM pattern matches any expression of the type `bool`:

  
 [image: CXM code follows]   

```
   node matches expression as e where e.type matches boolType;
```

## See also

integerType
