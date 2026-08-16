---
title: "variableReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/variablereference.html"
content_id: "OuMNKcKqKeFgNBNDyAX4ow"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:07.798356+00:00"
---

# variableReference

Matches locations where an expression references a variable.

This pattern only matches nodes of type `expression`.

## Properties

`variableReference` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `isFinal` | `bool` | `true` if this variable is declared as `final` |
| `qualifiedName` | `string` | The name of the variable, with scope information |
| `scope` | `enum variableScopeenum` | The scope of the variable: One of `` `static` ``, `` `local` ``, or `` `tryResource` ``; see variableScopeEnum |
| `simpleName` | `string` | The name of the variable, without scope information |
| `variable` | `symbol` | The symbol that represents this variable |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches all variable references to final static variables:

  
 [image: CXM code follows]   

```
    pattern variableReferenceStaticFinal {
        variableReference {
            .scope == `global`;
            .isFinal == true;
        }
    };
```
