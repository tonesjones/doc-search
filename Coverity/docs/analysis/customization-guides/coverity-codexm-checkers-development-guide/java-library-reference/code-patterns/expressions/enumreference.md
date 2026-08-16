---
title: "enumReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/enumreference.html"
content_id: "X3z_fd8fBGS_OtwWbwZDJA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:01.937339+00:00"
---

# enumReference

Matches expressions that refer to an `enum`.

This pattern only matches nodes of type `expression`.

## Properties

`enumReference` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `enumVariableSymbol` | `symbol` | The enum symbol that refers to this enum |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches `enum` occurrences that have the identifier `Example`:

  
 [image: CXM code follows]   

```
    pattern enumReferenceExample {
        enumReference {
            .enumVariableSymbol == enumVariableSymbol { .simpleName == "Example" }
        }
    };
```
