---
title: "intType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/inttype.html"
content_id: "3hBEMeaWvx4aMRfQWsdnUw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:15.559338+00:00"
---

# intType

Matches integer types, including `bool`, `char`,
`short`, `int`, `long`, and `long long` (C++).

## Properties

`intType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum intKind` | One of `` `bool` ``, `` `char` ``, `` `short` ``, `` `int` ``, `` `long` `` or `` `long long` ``; see intKind. |
| `isSigned` | `bool` | `true` if the type is signed |
| `alignmentInBytes` | `int?` | The alignment of the type, in bytes; `null` if the type is not aligned |
| `sizeInBytes` | `int` | The number of bytes required to store a value of this type |
| `sizeInBits` | `int` | The number of bits required to store a value of this type |

## Example

In the following source code, the pattern `intType` matches
the type of a local variable, `x`:

  
 [image: C/C++ code follows]   

```
int x = true;
```

The following CodeXM pattern matches all `short` types:

  
 [image: CXM code follows]   

```
    node matches expression {
        .type matches intType {
            .kind == `short`
        }
    };
```
