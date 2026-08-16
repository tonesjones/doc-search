---
title: "classType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/classtype.html"
content_id: "bb9R5HnC3s3EhHILuIDgEg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:54.477919+00:00"
---

# classType

Matches any kind of Java class type.

Matches the following kinds of Java classes:

- `class`
- `interface`
- `array`
- `annotation`
- `enum`

This pattern only matches nodes of type `type`.

## Properties

`classType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `isAnonymous` | `bool` | `true` if the class is anonymous |
| `isComplete` | `bool` | `true` if the class is complete |
| `kind` | `enum` | The kind of class: one of `` `class` ``, `` `interface` ``, `` `array` ``, `` `annotation` ``, or `` `enum` `` |
| `location` | `location` | The location information of the class |
| `qualifiedName` | `string` | The name of the class, including its package |
| `scopeList` | `list<string>` | The scope of the class. This is the elements of the qualified name broken up into a list. |
| `simpleName` | `string` | The name of the class, without the package prefix |

## Example

The following CodeXM pattern:

  
 [image: CXM code follows]   

```
    c matches classType { .kind = `enum };
```

... matches all `enum` classes.
