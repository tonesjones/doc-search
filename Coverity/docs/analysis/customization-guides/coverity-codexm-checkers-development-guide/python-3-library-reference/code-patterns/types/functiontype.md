---
title: "functionType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/functiontype.html"
content_id: "nJfyqJpQgG2HmrnPyoZrgQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:34.859100+00:00"
---

# functionType

Matches function types.

This pattern only matches nodes of type `type`.

## Properties

`functionType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `isMethod` | `bool` | `true` if the function is a method |
| `parameterTypeList` | `list<type>` | The types of the function parameters |
| `returnType` | `type?` | The type that the function returns; `null` if there is no return expression |

## Example

The following CodeXM code matches any expression that has a function type:

[image: CXM code follows]

```
    node matches expression as e where e.type matches functionType;
```
