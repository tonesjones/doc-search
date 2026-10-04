---
title: "tupleClassType"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/tupleclasstype.html"
content_id: "3CvElV6f9Z7sspto9MR69w"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:26.891072+00:00"
---

# tupleClassType

Matches C# `System.Tuple` class types.

This pattern only matches nodes of type `type`.

## Properties

`tupleClassType` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `componentTypes` | `list<type>` | The types of the tuple's components |

## Example

The following CodeXM pattern matches all instances of `Tuple<char,bool>`:

  
 [image: CXM code follows]   

```
    t matches tupleType {
        .componentTypes == [charType, booleanType]
    };
```
