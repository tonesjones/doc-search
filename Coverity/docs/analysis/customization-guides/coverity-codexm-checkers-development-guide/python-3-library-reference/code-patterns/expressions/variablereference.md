---
title: "variableReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/variablereference.html"
content_id: "BmhAEcE~nNQzov17sbDrZg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:47.484737+00:00"
---

# variableReference

Matches references to variables.

This pattern only matches nodes of type `expression`.

## Properties

`variableReference` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `qualifiedName` | `string` | The name of the variable, including scope information |
| `scope` | `enum variableScopeKind` | The scope of the variable: either `` `global` `` or `` `local` ``; see variableScopeKind |
| `simpleName` | `string` | The name of the variable, without scope information |
| `variable` | `symbol` | The symbol that represents ths variable |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches all references to global variables:

[image: CXM code follows]

```
    pattern globalVariableReference {
        variableReference {
            .scope == `global`
        }
    };
```
