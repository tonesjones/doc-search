---
title: "charType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/chartype.html"
content_id: "WdZRD7YRZlfX7kNZV1GytQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:10.941860+00:00"
---

# charType

Matches character types such as `char` or the C++ `wchar_t`.

## Properties

`charType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum` | One of `` `char` ``, `` `unsigned char` ``, `` `signed char` ``, or `` `wchar_t` `` |
| `isSigned` | `bool` | `true` if the type is signed |
| `isExplicitlySigned` | `bool` | `true` if the sign is explicitly stated (rather than being implied) |
| `alignmentInBytes` | `int?` | The alignment of the type, in bytes; `null` if the type is not aligned |
| `sizeInBytes` | `int` | The number of bytes required to store a value of this type |
| `sizeInBits` | `int` | The number of bits required to store a value of this type |

## Example

In the following source code, the pattern `charType`
matches the type of a local variable, `x`:

  
 [image: C/C++ code follows]   

```
char x = 'a';
```

The following example matches explicitly signed `char` types:

  
 [image: CXM code follows]   

```
    node matches expression {
        .type == charType {
            .isExplicitlySigned == true
        }
    };
```
