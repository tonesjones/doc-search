---
title: "referencedTypesType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/referencedtypestype.html"
content_id: "ZhELQ4oaGUmjCEOLkr~ncA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:18.539522+00:00"
---

# referencedTypesType

(C++) Matches types that instantiate a template.

This pattern only matches nodes of type `type`.

## Properties

`referencedTypesType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `referencedTypes` | `list<type>` | The types that the template instance references. |
| `targetType` | `type` | The type of the template instance. |

## Example

Suppose you had a C++ program with the following declarations:

  
 [image: C++ code follows]   

```
template< typename T1, typename T2 >
class myClass {
}

myClass< int, bool > cls;
```

... then `referencedTypesType` would match `cls`.
Its `.referencedTypes` property would contain
`intType` and `boolType`, and the value of
`.targetType` would be `"myClass"`.
