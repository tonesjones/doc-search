---
title: "pointerType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/pointertype.html"
content_id: "pltBK2DNlpXt_HOs1xkEsA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:22.334574+00:00"
---

# pointerType

Matches C# pointer types.

C# recognizes pointer types only in unsafe mode.

This pattern only matches nodes of type `type`.

## Properties

`pointerType` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `toType` | `type` | The type of the object pointed to |

## Example

The following CodeXM pattern matches all pointers to a class named `MyClass`:

  
 [image: CXM code follows]   

```
    p matches pointerType {
        .toType == classType {
            .simpleName == "MyClass"
        }
    }
```
