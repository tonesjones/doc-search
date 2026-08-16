---
title: "functionType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/functiontype.html"
content_id: "gzJyTlQ2~qX~MLkJF2ioSw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:55.892776+00:00"
---

# functionType

Matches function types.

This pattern only matches nodes of type `type`.

## Properties

`functionType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `declaredThrownTypeList` | `list<type>` | The types the function is declared to throw |
| `hasVariableArity` | `bool` | `true` if the function uses variable arity; for example, `method ( Type arg, ... )`. (*Arity* is the number of arguments that a function accepts.) |
| `isStatic` | `bool` | Whether the function is declared as `static` |
| `parameterTypeList` | `list<type>` | Lists the types of parameters in the call |
| `returnType` | `type` | The return type of the function |

## Example

The following CodeXM pattern matches all function types that return an `int`:

  
 [image: CXM code follows]   

```
    pattern returnsInt {
        functionType {
            .retunrnType == integerType { .kind == `int` }
        }
    };
```
