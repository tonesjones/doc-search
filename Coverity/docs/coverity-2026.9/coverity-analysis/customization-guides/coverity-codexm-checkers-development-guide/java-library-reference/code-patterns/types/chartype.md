---
title: "charType"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/chartype.html"
content_id: "L3jp1Tes_3wn_JP3OYFFEA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:40.347209+00:00"
---

# charType

Matches the `char` type.

This pattern only matches nodes of type `type`.

## Properties

`charType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `alignmentInBytes` | `int` | The alignment of the type, in bytes |
| `sizeInBits` | `int` | The total size of the `char`, in bits |
| `sizeInBytes` | `int` | The size of the `char`, in bytes |

## Example

The following CodeXM example matches any expression with a `char` type:

  
 [image: CXM code follows]   

```
    node matches expression { .type == charType };
```

## See also

integerType
