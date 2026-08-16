---
title: "charType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/chartype.html"
content_id: "~2SbvhHGutUDt~xTXy7Lbw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:15.249764+00:00"
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

The following CodeXM pattern matches any expression of the type `char`:

[image: CXM code follows]

```
    node matches expression { .type == charType };
```

## See also

integralType
