---
title: "pointerType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/pointertype.html"
content_id: "fVLlvwIDv3ry7VB~D4Dl_g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:17.792551+00:00"
---

# pointerType

Matches pointer types such as `int*` or `char*`.

## Properties

`pointerType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `pointerToType` | `type` | The type of the referenced value |
| `alignmentInBytes` | `int?` | The alignment of the type, in bytes; `null` if the type is not aligned |
| `sizeInBytes` | `int` | The number of bytes required to store a value of this type |

## Example

In the following source code, the pattern `pointerType`
matches the type of a local variable, `x`,
provided that the `.pointerToType` property
is `intType`:

  
 [image: C/C++ code follows]   

```
int *x = nullptr;
```

The following CodeXM pattern matches all expressions that are pointers to integers:

  
 [image: CXM code follows]   

```
    node matches expression as e
        && e.type matches pointerType {
            .pointerToType == intType
        };
```
