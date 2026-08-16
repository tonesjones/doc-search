---
title: "compositeLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/compositeliteral.html"
content_id: "USzZw3DipXc6x~XnCWPMVw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:42.745404+00:00"
---

# compositeLiteral

Matches `struct` literals.

This pattern only matches nodes of type `expression`.

## Properties

`compositeLiteral` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `targetType` | `classType` | The type of the `struct` object. |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches literal `struct` objects whose name is `Example`:

  
 [image: CXM code follows]   

```
    pattern examplecompositeLiteral {
        .targetType == classType { .simpleName == "Example" }
    }
```
