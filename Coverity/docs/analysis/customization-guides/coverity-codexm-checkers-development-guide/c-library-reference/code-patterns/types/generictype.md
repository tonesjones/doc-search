---
title: "genericType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/generictype.html"
content_id: "2vnXkvur0jbMvtHLgPcOPA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:19.567555+00:00"
---

# genericType

Matches C# generic types.

This pattern only matches nodes of type `type`.

## Properties

`genericType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `genericClass` | `type` | The generic type |
| `isNullable` | `bool` | `true` if this a nullable type |
| `typeParameters` | `list<typeParameterType>` | The type parameters |

## Example

The following CodeXM pattern matches all nullable types:

  
 [image: CXM code follows]   

```
    g matches genericType {
        .isNullable == true
    };
```

## See also

typeParameterType
