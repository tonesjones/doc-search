---
title: "anyTypeVariableReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/anytypevariablereference.html"
content_id: "VtNTTbnn5X7~wLX0UXqPew"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:31.917035+00:00"
---

# anyTypeVariableReference

Matches locations where an expression references a variable.

This pattern only matches nodes of type `expression`.

## Properties

`anyTypeVariableReference` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `variable` | `symbol` | The symbol that represents the variable |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches all references to local variables:

  
 [image: CXM code follows]   

```
    pattern variableReferenceStaticFinal {
        variableReference {
            .scope == `local`;
        }
    }
```
