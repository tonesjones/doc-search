---
title: "nullableType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/nullabletype.html"
content_id: "CySp6U_5AYUPAEIbhCv~Ww"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:20.936319+00:00"
---

# nullableType

Matches C# nullable types.

This pattern only matches nodes of type `type`.

## Properties

`nullableType` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `valueType` | `type` | The underlying type that can be nulled |

## Example

The following pattern matches all nullable `char` instances:

  
 [image: CXM code follows]   

```
    n matches nullableType {
        .valueType == charType
    }
```
