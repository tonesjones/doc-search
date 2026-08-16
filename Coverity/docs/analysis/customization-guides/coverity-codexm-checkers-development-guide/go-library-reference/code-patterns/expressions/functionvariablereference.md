---
title: "functionVariableReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/functionvariablereference.html"
content_id: "OeeCvaegseLQdJDsioaUTw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:39.409426+00:00"
---

# functionVariableReference

Matches locations where an expression references a function variable.

This pattern only matches nodes of type `expression`.

## Properties

`functionVariableReference` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `qualifiedName` | `string` | The name of the function variable, including any scope information |
| `simpleName` | `string` | The name of the function variable, without scope information |
| `variable` | `symbol` | The symbol that represents this function variable |

**Inherits properties from:**

- astnode
- expression

## Example

The following pattern matches all references to local variables:

  
 [image: CXM code follows]   

```
    pattern variableReferenceStaticFinal {
        variableReference {
            .scope == `local`;
        }
    }
```
