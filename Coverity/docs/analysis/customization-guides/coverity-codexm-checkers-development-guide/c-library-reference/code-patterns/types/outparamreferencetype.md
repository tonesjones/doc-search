---
title: "outParamReferenceType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/outparamreferencetype.html"
content_id: "ivBdxjVwb8e33Zv~xn7_2Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:21.685286+00:00"
---

# outParamReferenceType

Matches a C# `out` parameter.

This pattern only matches nodes of type `type`.

## Properties

`outParamReferenceType` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `toType` | `type` | The type the reference refers to |

## Example

The following CodeXM pattern:

  
 [image: CXM code follows]   

```
    o matches outParamReferenceType { .toType == integralType };
```

... matches integer `out` parameter types in C# target code; for example:

  
 [image: C# code follows]   

```
void OutArgExample(out int number) {
    number = 44;
};
```

## See also

referenceType
