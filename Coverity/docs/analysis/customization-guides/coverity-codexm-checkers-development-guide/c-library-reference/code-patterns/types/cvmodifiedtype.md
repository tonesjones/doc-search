---
title: "cvModifiedType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/cvmodifiedtype.html"
content_id: "SEwG5gPfb8YUQjngvH~jMQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:16.804713+00:00"
---

# cvModifiedType

Matches `const` or `volatile` modified types in C#.

This pattern only matches nodes of type `type`.

## Properties

`cvModifiedType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `cvFlags` | `list<cvModifierKind>` | A list of the modifier types applied to the matched type |
| `toType` | `enum cvModifierKind` | The type of the object being modified. |

## Example

The following pattern:

[image: CXM code follows]

```
    c matches cvModifiedType {
        .cvFlags.contains(`const`);
        .toType == charType
    };
```

... matches `const char`.

This pattern can be used to inspect target code such as the following:

[image: C# code follows]

```
class VolatileTest {
    public volatile char c;
};
```

## See also

cvModifierKind,
getQualifiers
