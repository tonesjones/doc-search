---
title: "referenceType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/referencetype.html"
content_id: "ymEhkqRgCvn2p9SmuMwevA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:19.272148+00:00"
---

# referenceType

Matches C++ reference types.

A C++ reference type can be declared for *lvalue* (`&`) or *rvalue* `&&` objects.

This pattern only matches nodes of type `type`.

## Properties

`referenceType` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum` | Either `` `lvalue` `` or `` `rvalue` `` |
| `referenceOfType` | `type` | The type being referenced; for example, `X` in an `X&` declaration |
| `alignmentInBytes` | `int?` | The alignment of the type, in bytes; `null` if the type is not aligned |
| `sizeInBytes` | `int?` | The number of bytes required to store a value of this type, if known; `null` if the value is not known |

## Example

The following CodeXM pattern matches all references to a class named `MyClass`:

  
 [image: CXM code follows]   

```
    r matches referenceType {
        .referenceOfType == classType { .simpleName == "MyClass" }
    };
```
