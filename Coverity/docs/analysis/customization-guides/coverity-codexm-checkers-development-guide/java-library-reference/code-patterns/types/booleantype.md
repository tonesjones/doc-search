---
title: "booleanType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/booleantype.html"
content_id: "hwRdkToiK7txozNOaymssg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:53.106787+00:00"
---

# booleanType

Matches the `boolean` type.

## Properties

`booleanType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `alignmentInBytes` | `int` | The alignment of the type, in bytes |
| `sizeInBits` | `int` | The size of the Boolean, in bits |
| `sizeInBytes` | `int` | The size of the Boolean, in bytes |

## Example

The following CodeXM example matches any expression with a `boolean` type:

  
 [image: CXM code follows]   

```
    node matches expression as e where e.type matches booleanType;
```

## See also

integerType
