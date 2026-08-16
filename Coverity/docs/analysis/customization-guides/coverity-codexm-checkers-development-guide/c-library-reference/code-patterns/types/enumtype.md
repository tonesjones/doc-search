---
title: "enumType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/enumtype.html"
content_id: "RVU5yMDhr0vSEhwnx~n75A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:17.555344+00:00"
---

# enumType

Matches all kinds of C# `enum` types.

This pattern only matches nodes of type `type`.

## Properties

`enumType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `alignmentInBytes` | `int` | The alignment of the `enum`, in bytes |
| `location` | `location` | The location of the `enum` |
| `qualifiedName` | `string` | The name of the `enum` including its package |
| `scopeList` | `list<string>` | The scope of the `enum`. This is the elements of the qualified name broken up into a list. |
| `simpleName` | `string` | The name of the `enum`, without the package prefix |
| `sizeInBytes` | `int` | The size of the `enum`, in bytes |

## Example

The following CodeXM pattern matches all `enum` classes:

  
 [image: CXM code follows]   

```
    c matches enumType;
```
