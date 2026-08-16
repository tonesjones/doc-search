---
title: "arrayType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/arraytype.html"
content_id: "nRLMJ9iF0Q0sk5wcL5q1ew"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:13.941016+00:00"
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

The following pattern finds all arrays whose elements are any type of integer:

  
 [image: CXM code follows]   

```
    t matches arrayType {
        .elementType == integralType
    };
```
