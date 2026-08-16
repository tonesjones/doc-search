---
title: "functionType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/functiontype.html"
content_id: "IlTXVFxvUmGgZYwz96JQFg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:18.916317+00:00"
---

# functionType

Matches function types.

This pattern only matches nodes of type `type`.

## Properties

`functionType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `isStatic` | `bool` | `true` if the function is declared as static |
| `parameterTypeList` | `list<type>` | A list of all the parameter types for the function |
| `returnType` | `type` | The return type of the function |

## Example

The following CodeXM pattern matches all function types that return an `int`:

  
 [image: CXM code follows]   

```
    pattern returnsInt {
        functionType {
            .returnType == integralType { .kind == `int` }
        }
    };
```
