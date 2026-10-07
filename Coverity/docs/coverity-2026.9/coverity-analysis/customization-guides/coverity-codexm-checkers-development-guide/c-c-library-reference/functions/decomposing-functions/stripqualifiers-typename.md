---
title: "stripQualifiers( typeName )"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/stripqualifiers-typename-.html"
content_id: "E7BJor5Dtmuxi8TljRlV0w"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:23.319236+00:00"
---

# stripQualifiers( typeName )

Returns the base type that is wrapped by
`typeQualifier`, `typedefType`, or `deducedType`.

This is different from `hasBaseType()`,
as it does not strip `pointerType` or `arrayType`.

## Parameters and Return Type

| Name | Type | Description |
| --- | --- | --- |
| `typeName` | `type` | The type to match |
| ***return value*** | `type` | The base type without qualifiers |

## Example

To strip qualifiers on a specific type, to any depth, you might define a CodeXM pattern such as the following:

  
 [image: CXM code follows]   

```
    pattern nonCharPointer {
        pointerType as pt
            where ! ( stripQualifiers( pt.pointerToType ) )
                matches charType
    };
```
