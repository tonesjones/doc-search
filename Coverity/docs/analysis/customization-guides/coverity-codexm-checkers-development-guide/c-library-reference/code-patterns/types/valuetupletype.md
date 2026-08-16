---
title: "valueTupleType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/valuetupletype.html"
content_id: "bIgDH057vo7hzvgwbiOx8Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:26.424612+00:00"
---

# valueTupleType

Matches any C# `System.ValueTuple` type.

This pattern only matches nodes of type `type`.

## Properties

`valueTupleType` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `componentTypes` | `list<type>` | The types of the tuple's components |

## Example

The following CodeXM pattern matches all instances of `ValueTuple<char,bool>`:

  
 [image: CXM code follows]   

```
    v matches valueTupleType {
        .componentTypes == [charType, booleanType]
    };
```
