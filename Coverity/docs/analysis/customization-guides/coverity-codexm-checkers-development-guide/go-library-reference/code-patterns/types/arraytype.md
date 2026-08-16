---
title: "arrayType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/arraytype.html"
content_id: "IlM0d5rJkJZX3DkAAJWZdw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:24.253813+00:00"
---

# arrayType

Matches all array types.

This pattern only matches nodes of type `type`.

## Properties

`arrayType` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `elementType` | `type` | The type of the elements in the array |

## Example

The following CodeXM pattern finds all arrays whose elements are any type of integer:

  
 [image: CXM code follows]   

```
   t matches arrayType {
        .elementType == integerType
    };
```
