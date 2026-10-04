---
title: "integerType"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/integertype.html"
content_id: "fMs2h6PzzCOTFaAAAxNBjA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:40.531069+00:00"
---

# integerType

Matches all integer types that Java recognizes.

This pattern only matches nodes of type `type`.

## Properties

`integerType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `alignmentInBytes` | `int` | The alignment of the type, in bytes |
| `kind` | `enum intKind` | The kind of integer type: `` `byte` ``, `` `int` ``, `` `long` ``, or `` `short` ``; see intKind |
| `sizeInBits` | `int` | The size of the type, in bits |
| `sizeInBytes` | `int` | The size of the type, in bytes |

## Example

The following snippet of CodeXM matches a `long` type, using the `kind` property:

  
 [image: CXM code follows]   

```
    t matches integerType { .kind == `long` };
```

## See also

booleanType,
charType
