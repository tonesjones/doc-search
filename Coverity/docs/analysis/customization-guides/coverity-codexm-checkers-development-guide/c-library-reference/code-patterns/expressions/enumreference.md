---
title: "enumReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/enumreference.html"
content_id: "zU_71Gh6Jm3gAAEy~wFw2A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:35.163152+00:00"
---

# enumReference

Matches expressions that reference an `enum`.

This pattern only matches nodes of type `expression`.

## Properties

`enumReference` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `enumVariableSymbol` | `symbol` | The symbol that refers to this `enum` |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches `enum` instances that have the identifer `Example`:

  
 [image: CXM code follows]   

```
    pattern enumReferenceExample {
        enumReference {
            .enumVariableSymbol == enumVariableSymbol { .simpleName == "Example" }
        }
    };
```
