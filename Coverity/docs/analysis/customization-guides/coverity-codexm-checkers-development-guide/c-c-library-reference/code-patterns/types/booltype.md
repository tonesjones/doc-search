---
title: "boolType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/booltype.html"
content_id: "Akqkyy03MqRvyDzFRBvI0g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:10.196897+00:00"
---

# boolType

Matches the Boolean types, both `bool` and `_Bool` (C11 and later).

## Properties

`boolType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum` | One of `` `bool` `` or `` `_Bool` `` |
| `alignmentInBytes` | `int?` | The alignment of the type, in bytes; `null` if the type is not aligned |
| `sizeInBytes` | `int` | The number of bytes required to store a value of this type |
| `sizeInBits` | `int` | The number of bits required to store a value of this type |

## Example

In the following source code, the pattern `boolType` matches the type of a local variable,
`x`:

  
 [image: C/C++ code follows]   

```
bool x = true;
```

The following CodeXM pattern matches all expressions with a Boolean type:

  
 [image: CXM code follows]   

```
    node matches expression {
        .type == boolType
    };
```
