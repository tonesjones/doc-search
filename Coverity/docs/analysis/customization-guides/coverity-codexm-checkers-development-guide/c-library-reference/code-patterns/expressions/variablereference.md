---
title: "variableReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/variablereference.html"
content_id: "rEIpCegu_TUKIDDKDhSLTg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:53.747061+00:00"
---

# variableReference

Matches where variables are referenced in expressions.

This pattern only matches nodes of type `expression`.

## Properties

`variableReference` produces a record that contains the following properties by variableReference:

| Name | Type | Description |
| --- | --- | --- |
| `isFinal` | `bool` | `true` if this variable is declared as `final` |
| `qualifiedName` | `string` | The name of the variable, with scope information. |
| `scope` | `enum variableDeclarationKind` | The scope of the variable: one of `` `static` ``, `` `local` ``, or `` `tryResource` ``; see variableDeclarationKind |
| `simpleName` | `string` | The name of the variable, without scope information. |
| `variable` | `symbol` | The symbol that represents this variable |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches all references to final static variables:

  
 [image: CXM code follows]   

```
    pattern variableReferenceStaticFinal {
        variableReference {
            .scope == `global`;
            .isFinal == true;
        }
    };
```
