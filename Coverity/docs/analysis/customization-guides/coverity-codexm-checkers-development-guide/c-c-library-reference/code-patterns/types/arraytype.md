---
title: "arrayType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/arraytype.html"
content_id: "JtsF1qqlLmQWEhC~AgkZMA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:09.443740+00:00"
---

# arrayType

Matches arrays.

## Properties

`arrayType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `elementType` | `type` | The type of the elements in the array |
| `elementCount` | `int?` | The number of elements in the array; `null` if the array is uninitialized |
| `alignmentInBytes` | `int?` | The alignment of the type, in bytes; `null` if the type is not aligned |
| `sizeInBytes` | `int?` | The number of bytes required to store a value of this type, if known; `null` if the value is not known |

## Example

In the following source code, the pattern `arrayType`
matches the type of a local variable `x` in the assignment statement,
provided that `.elementType` is `intType`
and `.elementCount` is `10`:

  
 [image: C/C++ code follows]   

```
int x[10];
x[0] = 1;
```

The following CodeXM pattern detects an expression that is an array type:

  
 [image: CXM code follows]   

```
    node matches expression {
        .type == arrayType
    };
```
