---
title: "arrayType"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/arraytype.html"
content_id: "m~TYf8Cwliv6cC87LXqycQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:40.262270+00:00"
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

The following CodeXM `match` statement finds all arrays whose elements are integers:

  
 [image: CXM code follows]   

```
    t matches arrayType {
        .elementType == integerType
    }
```
