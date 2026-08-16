---
title: "classType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/classtype.html"
content_id: "4tqo0N6hcGSFHkdFVF1EEQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:25.658556+00:00"
---

# classType

Matches all `struct` and `interface` types.

This pattern only matches nodes of type `type`.

## Properties

`classType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `isAnonymous` | `bool` | `true` if the class is anonymous |
| `isComplete` | `bool` | `true` if the class is complete. |
| `kind` | `enum` | The kind of class: either `` `interface` `` or `` `struct` `` |
| `location` | `location` | The location information of the class |
| `qualifiedName` | `string` | The name of the class including the class's package |
| `scopeList` | `list<string>` | The scope of the class. This is the elements of the qualified name broken up into a list. |
| `simpleName` | `string` | The name of the class, without the package prefix |

## Example

The following CodeXM pattern matches all `interface` types:

  
 [image: CXM code follows]   

```
   c matches classType { .kind = `interface` };
```
