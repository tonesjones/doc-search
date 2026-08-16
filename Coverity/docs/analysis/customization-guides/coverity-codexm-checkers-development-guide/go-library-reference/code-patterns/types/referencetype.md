---
title: "referenceType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/referencetype.html"
content_id: "hBCnXm~ywUrw7IULRSwWxw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:28.435039+00:00"
---

# referenceType

Matches reference types.

A reference type represents an object being passed by reference; for example, as an argument to a function.

This pattern only matches nodes of type `type`.

## Properties

`referenceType` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `toType` | `type` | The type the reference refers to |

## Example

The following CodeXM pattern matches all references to a structure named `MyStruct`:

  
 [image: CXM code follows]   

```
   r matches referenceType {
        .toType == classType { .simpleName == "MyStruct" }
    };
```
