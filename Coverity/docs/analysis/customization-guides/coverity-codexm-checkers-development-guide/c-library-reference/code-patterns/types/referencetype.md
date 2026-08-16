---
title: "referenceType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/referencetype.html"
content_id: "YSwBR~qdxHbNWtwyUnvKAQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:23.798502+00:00"
---

# referenceType

Matches C# reference types.

A C# reference type can be declared as a `class`, `interface`, or `delegate`;
the `dynamic`, `object`, and `string` types are inherently references.

This pattern only matches nodes of type `type`.

## Properties

`referenceType` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `toType` | `type` | The type the reference refers to |

## Example

The following CodeXM pattern matches all references to a class named `MyClass`:

  
 [image: CXM code follows]   

```
    r matches referenceType {
        .toType == classType { .simpleName == "MyClass" }
    };
```

## See also

outParamReferenceType,
referenceParamType
