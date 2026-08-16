---
title: "listLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/listliteral.html"
content_id: "rAb24P8Kg9PWYIE3hHDTOg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:52.962764+00:00"
---

# listLiteral

Matches literal list expressions.

This pattern only matches nodes of type `expression`.

## Properties

`listLiteral` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expressions` | `list<expression>` | The expressions that comprise the list |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern finds empty list literals ( `[]` ):

[image: CXM code follows]

```
    pattern emptyList {
        listLiteral as lst where lst.expressions.empty
    };
```
